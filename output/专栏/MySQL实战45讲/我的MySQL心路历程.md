# 我的MySQL心路历程 

Source: https://learn.lianglianglee.com/专栏/MySQL实战45讲/我的MySQL心路历程.md

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# 我的MySQL心路历程

在专栏上线后的 11 月 21 日，我来到极客时间做了一场直播，主题就是“我的 MySQL 心路历程”。今天，我特意将这个直播的回顾文章，放在了专栏下面，希望你可以从我这些年和 MySQL 打交道的经历中，找到对你有所帮助的点。

这里，我先和你说一下，在这个直播中，我主要分享的内容：

1. 我和 MySQL 打交道的经历；
2. 你为什么要了解数据库原理；
3. 我建议的 MySQL 学习路径；
4. DBA 的修炼之道。

# 我的经历

## 以丰富的经历进入百度

我是福州大学毕业的，据我了解，那时候我们学校的应届生很难直接进入百度，都要考到浙江大学读个研究生才行。没想到的是，我投递了简历后居然进了面试。

入职以后，我跑去问当时的面试官，为什么我的简历可以通过筛选？他们说：“因为你的简历厚啊”。我在读书的时候，确实做了很多项目，也实习过不少公司，所以简历里面的经历就显得很丰富了。

在面试的时候，有个让我印象很深刻的事儿。面试官问我说，你有这么多实习经历，有没有什么比较好玩儿的事？我想了想答道，跟你说个数据量很大的事儿 ，在跟移动做日志分析的时候我碰到了几千万行的数据。他听完以后就笑了。

后来，我进了百度才知道，几千万行那都是小数据。

## 开始尝试看源码解决问题

加入百度后，我是在贴吧做后端程序，比如权限系统等等。其实很简单，就是写一个 C 语言程序，响应客户端请求，然后返回结果。

那个时候，我还仅仅是个 MySQL 的普通用户，使用了一段时间后就出现问题了：一个跑得很快的请求，偶尔会又跑得非常慢。老板问这是什么原因，而我又不好意思说不知道，于是就自己上网查资料。

但是，2008 年那会儿，网上资料很少，花了挺长时间也没查出个所以然。最终，我只好去看源码。翻到源码，我当时就觉得它还蛮有意思的。而且，源码真的可以帮我解决一些问题。

于是一发不可收拾，我从那时候就入了源码的“坑”。

## 混社区分享经验

2010 年的时候，阿里正好在招数据库的开发人员。虽然那时我还只是看得懂源码，没有什么开发经验，但还是抱着试试看的态度投了简历。然后顺利通过了面试，成功进入了阿里。之后，我就跟着褚霸（霸爷）干了 7 年多才离开了阿里。

在百度的时候，我基本上没有参加过社区活动。因为那时候百度可能更提倡内部分享，解决问题的经验基本上都是在内网分享。所以，去了阿里以后，我才建了博客、开了微博。我在阿里的花名叫丁奇，博客、微博、社区也因此都是用的这个名字。

# 为什么要了解数据库原理？

这里，我讲几个亲身经历的事情，和你聊聊为什么要了解数据库原理。

## 了解原理能帮你更好地定位问题

一次同学聚会，大家谈起了技术问题。一个在政府里的同学说，他们的系统很奇怪，每天早上都得重启一下应用程序，否则就提示连接数据库失败，他们都不知道该怎么办。

我分析说，按照这个错误提示，应该就是连接时间过长了，断开了连接。数据库默认的超时时间是 8 小时，而你们平时六点下班，下班之后系统就没有人用了，等到第二天早上九点甚至十点才上班，这中间的时间已经超过 10 个小时了，数据库的连接肯定就会断开了。

我当时说，估计这个系统程序写得比较差，连接失败也不会重连，仍然用原来断掉的连接，所以就报错了。然后，我让他回去把超时时间改得长一点。后来他跟我说，按照这个方法，问题已经解决了。

由此，我也更深刻地体会到，作为开发人员，即使我们只知道每个参数的意思，可能就可以给出一些问题的正确应对方法。

## 了解原理能让你更巧妙地解决问题

我在做贴吧系统的时候，每次访问页面都要请求一次权限。所以，这个请求权限的请求，访问概率会非常高，不可能每次都去数据库里查，怎么办呢？

我想了个简单的方案：在应用程序里面开了个很大的内存，启动的时候就把整张表全部 load 到内存里去。这样再有权限请求的时候，直接从内存里取就行了。

数据库重启时，我的进程也会跟着重启，接下来就会到数据表里面做全表扫描，把整个用户相关信息全部塞到内存里面去。

但是，后来我遇到了一个很郁闷的情况。有时候 MySQL 崩溃了，我的程序重新加载权限到内存里，结果这个 select 语句要执行 30 分钟左右。本来 MySQL 正常重启一下是很快的，进程重启也很快，正常加载权限的过程只需要两分钟就跑完了。但是，为什么异常重启的时候就要 30 分钟呢？

我没辙了，只好去看源码。然后，我发现 MySQL 有个机制，当它觉得系统空闲时会尽量去刷脏页。

具体到我们的例子里，MySQL 重启以后，会执行我的进程做全表扫描，但是因为这个时候权限数据还没有初始化完成，我的 Server 层不可能提供服务，于是 MySQL 里面就只有我那一个 select 全表扫描的请求，MySQL 就认为现在很闲，开始拼命地刷脏页，结果就吃掉了大量的磁盘资源，导致我的全表扫描也跑得很慢。

知道了这个机制以后，我就写了个脚本，每隔 0.5 秒发一个请求，执行一个简单的 SQL 查询，告诉数据库其实我现在很忙，脏页刷得慢一点。

脚本一发布使用，脏页果然刷得慢了，加载权限的扫描也跑得很快了。据说我离职两年多以后，这个脚本还在用。

你看，如果我们懂得一些参数，并可以理解这些参数，就可以做正确的设置了。而如果我们进一步地懂得一些原理，就可以更巧妙地解决问题了。

## 看得懂源码让你有更多的方法

2012 年的时候，阿里双十一业务的压力比较大。当时还没有这么多的 SSD，是机械硬盘的时代。

为了应对压力我们开始引入 SSD，但是不敢把 SSD 直接当存储用，而是作为二级缓存。当时，我们用了一个叫作 Flashcache 的开源系统（现在已经是老古董级别了，不知道你有没有听过这个系统）。

Flashcache 实现，把 SSD 当作物理盘的二级缓存，可以提升性能。但是，我们自己部署后发现性能提升的效果没有预想的那么好，甚至还不如纯机械盘。

于是，我跟霸爷就开始研究。霸爷负责分析 Flashcache 的源码，我负责分析 MySQL 源码。后来我们发现 Flashcache 是有脏页比例的，当脏页比例到了 80% 就会停下来强行刷盘。

一开始我们以为这个脏页比例是全部的 20%，看了源码才知道，原来它分了很多个桶，比如说一个桶 20M，这个桶如果用完 80%，它就认为脏页满了，就开始刷脏页。这也就意味着，如果你是顺序写的话，很容易就会把一个桶写满。

知道了这个原理以后，我就把日志之类顺序写的数据全都放到了机械硬盘，把随机写的数据放到了 Flashcache 上。这样修改以后，效果就好了。

你看，如果能看得懂源码，你的操作行为就会不一样。

# MySQL 学习路径

说到 MySQL 的学习路径，其实我上面分享的这些内容，都可以归结为学习路径。

首先你要会用，要去了解每个参数的意义，这样你的运维行为（使用行为）就会不一样。千万不要从网上拿了一些使用建议，别人怎么用，你就怎么用，而不去想为什么。再往后，就要去了解每个参数的实现原理。一旦你了解了这些原理，你的操作行为就会不一样。 再进一步，如果看得懂源码，那么你对数据库的理解也会不一样。

再来讲讲我是怎么带应届生的。实践是很好的学习方式，所以我会让新人来了以后先搭主备，然后你就会发现每个人的自学能力都不一样。比如遇到有延迟，或者我们故意构造一个主备数据不一致的场景，让新人了解怎么分析问题，解决问题。

如果一定要总结出一条学习路径的话，那首先要会**用**，然后可以**发现问题**。

在专栏里面，我在每篇文章末尾，都会提出一个常见问题，作为思考题。这些问题都不会很难，是跟专栏文章挂钩、又是会经常遇到的，但又无法直接从文章里拿到答案。

我的建议是，你可以尝试先不看答案自己去思考，或者去数据库里面翻一翻，这将会是一个不错的过程。

再下一步就是**实践**。之后当你觉得开始有一些“线”的概念了，再去**看 MySQL 的官方手册**。在我的专栏里，有人曾问我要不要直接去看手册？

我的建议是，一开始千万不要着急看手册，这里面有 100 多万个英文单词，你就算再厉害，也是看了后面忘了前面。所以，你一定要自己先有脉络，然后有一个知识网络，再看手册去查漏补缺。

我自己就是这么一路走过来的。

另外，在专栏的留言区，很多用户都希望我能推荐一本书搭配专栏学习。如果只推荐一本的话，我建议你读一下《高性能 MySQL》这本书，它是 MySQL 这个领域的经典图书，已经出到第三版了，你可以想象一下它的流行度。

这本书的其中两位译者（彭立勋、翟卫祥）是我原团队的小伙伴，有着非常丰富的 MySQL 源码开发经验，他们对 MySQL 的深刻理解，让这本书保持了跟原作英文版同样高的质量。
![img](assets/cebd662dab97995a7718c4a38009cfc8.png)

# DBA 的修炼

## DBA 和开发工程师有什么相同点？

我带过开发团队，也带过 DBA 团队，所以可以分享一下这两个岗位的交集。

其实，DBA 本身要有些开发底子，比如说做运维系统的开发。另外，自动化程度越高，DBA 的日常运维工作量就越少，DBA 得去了解开发业务逻辑，往业务架构师这个方向去做。

开发工程师也是一样，不能所有的问题都指望 DBA 来解决。因为，DBA 在每个公司都是很少的几个人。所以，开发也需要对数据库原理有一定的了解，这样向 DBA 请教问题时才能更专业，更高效地解决问题。

所以说，这两个岗位应该有一定程度的融合，即：开发要了解数据库原理，DBA 要了解业务和开发。

## DBA 有前途吗？

这里我要强调的是，每个岗位都有前途，只需要根据时代变迁稍微调整一下方向。

像原来开玩笑说 DBA 要体力好，因为得搬服务器。后来 DBA 的核心技能成了会搭库、会主备切换，但是现在这些也不够用了，因为已经有了自动化系统。

所以，DBA 接下来一方面是要了解业务，做业务的架构师；另一方面，是要有前瞻性，做主动诊断系统，把每个业务的问题挑出来做成月报，让业务开发去优化，有不清楚的地方，开发同学会来找你咨询。你帮助他们做好了优化之后，可以把优化的指标呈现出来。这将很好地体现出你对于公司的价值。

## 有哪些比较好的习惯和提高 SQL 效率的方法？

这个方法，总结起来就是：要多写 SQL，培养自己对 SQL 语句执行效率的感觉。以后再写或者建索引的时候，知道这个语句执行下去大概的时间复杂度，是全表扫描还是索引扫描、是不是需要回表，在心里都有一个大概的概念。

这样每次写出来的 SQL 都会快一点，而且不容易犯低级错误。这也正式我开设这个专栏的目标。

## 看源码需要什么技术？

看源码的话，一是要掌握 C 和 C++；另外还要熟悉一些调试工具。因为代码是静态的，运行起来是动态的，看代码是单线程的，运行起来是多线程的，所以要会调试。

另外，我不建议你用可视化的工具。虽然可视化工具很方便，但你不知道这个操作点下去以后，实际上做了什么，所以我建议你自己手写代码和 SQL 语句，这样对一些底层原理你会更明白。

## 怎么学习 C、C++？

我在读研究生的时候，在 C 和 C++ 语言的学习上进步最大。

那时，我去给专科上 C 和 C++ 的课。我觉得自己已经会了，完全可以教得了。但去了之后，我才知道，自己会跟能够教别人完全是两码事儿。备课的时候，你不能只讲会用的部分，还得把原理讲清楚。这样，就会倒逼自己进行更深入更全面的学习。

有的人看完技术博客和专栏，会把这篇文章的提纲列一下，写写自己的问题和对这篇文章的理解。这个过程，是非常利于学习的。因为你听进来是一回事儿，讲出去则是另一回事儿。

## 学数据库要保持什么心态？

不只是数据库，所有多线程的服务，调试和追查问题的过程都是很枯燥的，遇到问题都会很麻烦。但是，你找出问题时的那一下会很爽。

我觉得你得找到这种感觉，它可以支持你度过接下来要枯燥很久的那段时光，这样你才能继续坚持下去。