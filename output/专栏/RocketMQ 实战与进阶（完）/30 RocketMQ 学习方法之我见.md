# 30 RocketMQ 学习方法之我见 

Source: https://learn.lianglianglee.com/专栏/RocketMQ 实战与进阶（完）/30 RocketMQ 学习方法之我见.md

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# 30 RocketMQ 学习方法之我见

亲爱的读者朋友，RocketMQ 实战专辑的全部内容即将更新完毕，前面的篇幅主要是介绍 RocketMQ 技术本身，本篇想和大家谈谈我是如何学习 RocketMQ 的，尽量做到授之以渔。

我想大家都会有这样一个共识：**光学理论没用，要实战**。这个有一定的道理，但不应该成为阻碍我们学习的理由。对知识的学习我们当然需要优先学习研究工作中常用的技术，例如以微服务为例，现在市面上 Spring Clould 很火，但公司主要用的是 Dubbo，如果此时你想深入研究微服务，我建议优先选择学习 Dubbo，因为你有实践经验，深入研究 Dubbo 能更好的指导实践，从而实现理论与实际相结合，并且 Dubbo 在市面上也使用的很广泛。

但有时候受到所在平台的限制，日常工作中无法接触到主流的技术，例如缺乏高并发、压根就没有接触过消息中间件，此时该怎么办？

**笔者个人的建议**：在无法实际使用时，应该去研究主流技术的原理，为使用做好准备，不要因为没有接触到而放弃学习，机会是留给有准备的人，如果你对某一项技术研究有一定深度时，当项目中需要使用时，你可以立马施展你的才华，很容易脱颖而出。

我在学习 RocketMQ 之前在实际工作中没有接触过任意一款消息中间件，更别谈使用了，促成我学习 RocketMQ 的原因是我得知 RocketMQ 被捐献给 Apache 基金会，而且还听说 RocketMQ 支撑了阿里双十一的具大流量，让我比较好奇，想一睹一款高性能的分布式消息中间件的风采，从此踏上了学习 RocketMQ 的历程。

**确定好目标后，该怎么学习 RocketMQ 呢？**

**1. 通读 RocketMQ 官方设计手册**

通常开始学习一个开源框架(产品)，建议大家首先去官网查看其用户手册、设计手册，从而对该框架能解决什么问题，基本的工作原理、涵盖了哪些知识点（后续可以对这些知识点一一突破），从全局上掌握这块中间件。我还清晰的记得我在看 RokcetMQ 设计手册时，我不仅将一些属于理解透彻，并且一些与性能方面的“高级”名词深深的吸引了我，例如：

* 亿级消息堆积能力
* 内存映射、pagecache
* 零拷贝
* 同步刷盘、异步刷盘
* 同步复制、异步复制
* Hash 索引

看过设计手册后，让我产生了极大的兴趣，下决心从源码角度对其进行深入研究，立下了不仅深入研究 RocketMQ 的工作原理与实现细节，更是想掌握基于文件编程的设计理念，如何在实践中使用内存映射。

**2. 下载源码，跑通 Demo**

每一个开源框架，都会提供完备的测试案例，RokcetMQ 也不例外，RokcetMQ 的源码中有一个单独的模块 example，里面放了很多使用 Demo，按需运行一些测试用例，能让你掌握 RokcetMQ 的基本使用，算是入了一个门。

**3. 源码研究 RocketMQ**

通过前面两个步骤，对设计原理有了一个全局的理解，同时掌握了 RocketMQ 的基本使用，接下来需要深入探究 RocketMQ，特别是如果大家认真阅读了本专栏的所有实战类文章，那是时候研究其源码了。

阅读 RocketMQ 原理个人觉得有如下几个好处：

* 深入研究其实现原理，成体系化的研读 RocketMQ，对 RocketMQ 更具掌控性。通常对应消息中间件，如果出现故障，通常会给公司业务造成较大损失，当出现问题时快速止血固然重要，更难能可贵的时预判风险，避免生产故障发生，要做到预判风险，成体系化研究 RocketMQ 显得非常必要。
* 学习优秀的 RocketMQ 框架，提升编程技能，例如高并发、基于文件编程相关的技巧，我们都可以从中得到一些启发。

**那如何阅读 RocketMQ 源码呢？**

阅读源码之前还是需要具备一定的基础，建议在阅读 RokcetMQ 源码之前，先尝试阅读一下 Java 数据结构相关的源码，例如 HashMap、ArrayList，主要是培养自己阅读源码的方法，**通常我阅读源码的方法：先主流程、后分支流程**。

我举一个简单的例子来说明先主流程、后分支流程。

例如我在学习消息发送流程时，我只关注消息发送在客户端的流程，至于服务端接收到消息发送请求时，存储、复制、刷盘这些我都暂时不关注，我暂时先关注消息发送在客户端的设计，等弄明白了，后面再去服务端接收消息发送请求时会做哪些操作，然后逐一理解消息存储、消息刷盘、消息同步等机制，这样就能有条理的，逐个破解 RocketMQ 核心设计理念。