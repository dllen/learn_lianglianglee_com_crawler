# 08 _ 远程服务调用（下）：如何选择适合自己的RPC框架？ 

Source: https://learn.lianglianglee.com/专栏/周志明的架构课/08 _ 远程服务调用（下）：如何选择适合自己的RPC框架？.md

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# 08 \_ 远程服务调用（下）：如何选择适合自己的RPC框架？

你好，我是周志明。

上一讲，我们主要是从学术的角度出发，一起学习了RPC概念的形成过程。今天这一讲，我会带你从技术的角度出发，去看看工业界在RPC这个领域曾经出现过的各种协议，以及时至今日还在层出不穷的各种框架。你会从中了解到RPC要解决什么问题，以及如何选择适合自己的RPC框架。

## RPC框架要解决的三个基本问题

在第1讲“[原始分布式时代](https://time.geekbang.org/column/article/309761)”中，我曾提到过，在80年代中后期，惠普和Apollo提出了[网络运算架构](https://en.wikipedia.org/wiki/Network_Computing_System)（Network Computing Architecture，NCA）的设想，并随后在[DCE项目](https://en.wikipedia.org/wiki/Distributed_Computing_Environment)中，发展成了在Unix系统下的远程服务调用框架[DCE/RPC](https://zh.wikipedia.org/wiki/DCE/RPC)。

这是历史上第一次对分布式有组织的探索尝试。因为DCE本身是基于Unix操作系统的，所以DCE/RPC也仅面向于Unix系统程序之间的通用。

> 补充：这句话其实不全对，微软COM/DCOM的前身[MS RPC](https://en.wikipedia.org/wiki/Microsoft_RPC)，就是DCE的一种变体版本，而它就可以在Windows系统中使用。

在1988年，Sun Microsystems起草并向[互联网工程任务组](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)（Internet Engineering Task Force，IETF）提交了[RFC 1050](https://tools.ietf.org/html/rfc1050)规范，此规范中设计了一套面向广域网或混合网络环境的、基于TCP/IP网络的、支持C语言的RPC协议，后来也被称为是[ONC RPC](https://en.wikipedia.org/wiki/Open_Network_Computing_Remote_Procedure_Call)（Open Network Computing RPC/Sun RPC）。

这两个RPC协议，就可以算是如今各种RPC协议的鼻祖了。从它们开始，一直到接下来的这几十年，所有流行过的RPC协议，都不外乎通过各种手段来解决三个基本问题：

1. 如何表示数据？
2. 如何传递数据？
3. 如何表示方法？

接下来，我们分别看看是如何解决的吧。

### 如何表示数据？

这里的数据包括了传递给方法的参数，以及方法的返回值。无论是将参数传递给另外一个进程，还是从另外一个进程中取回执行结果，都会涉及**应该如何表示**的问题。

针对进程内的方法调用，我们使用程序语言内置的和程序员自定义的数据类型，就很容易解决数据表示的问题了；而远程方法调用，则可能面临交互双方分属不同程序语言的情况。

所以，即使是只支持同一种语言的RPC协议，在不同硬件指令集、不同操作系统下，也完全可能有不一样的表现细节，比如数据宽度、字节序的差异等。

行之有效的做法，是**将交互双方涉及的数据，转换为某种事先约定好的中立数据流格式来传输，将数据流转换回不同语言中对应的数据类型来使用**。这个过程说起来比较拗口，但相信你一定很熟悉它，这其实就是序列化与反序列化。

每种RPC协议都应该有对应的序列化协议，比如：

* ONC RPC的[External Data Representation](https://en.wikipedia.org/wiki/External_Data_Representation) （XDR）
* CORBA的[Common Data Representation](https://en.wikipedia.org/wiki/Common_Data_Representation)（CDR）
* Java RMI的[Java Object Serialization Stream Protocol](https://docs.oracle.com/javase/8/docs/platform/serialization/spec/protocol.html#a10258)
* gRPC的[Protocol Buffers](https://developers.google.com/protocol-buffers)
* Web Service的[XML Serialization](https://docs.microsoft.com/en-us/dotnet/standard/serialization/xml-serialization-with-xml-web-services)
* 众多轻量级RPC支持的[JSON Serialization](https://tools.ietf.org/html/rfc7159)
* ……

### 如何传递数据？

准确地说，如何传递数据是指如何通过网络，在两个服务Endpoint之间相互操作、交换数据。这里“传递数据”通常指的是应用层协议，实际传输一般是基于标准的TCP、UDP等传输层协议来完成的。

两个服务交互不是只扔个序列化数据流来表示参数和结果就行了，诸如异常、超时、安全、认证、授权、事务等信息，都可能存在双方交换信息的需求。

在计算机科学中，专门有一个“[Wire Protocol](https://en.wikipedia.org/wiki/Wire_protocol)”，用来表示两个Endpoint之间交换这类数据的行为。常见的Wire Protocol有以下几种：

* Java RMI的[Java Remote Message Protocol](https://docs.oracle.com/javase/8/docs/platform/rmi/spec/rmi-protocol3.html)（JRMP，也支持[RMI-IIOP](https://zh.wikipedia.org/w/index.php?title=RMI-IIOP&action=edit&redlink=1)）
* CORBA的[Internet Inter ORB Protocol](https://en.wikipedia.org/wiki/General_Inter-ORB_Protocol)（IIOP，是GIOP协议在IP协议上的实现版本）
* DDS的[Real Time Publish Subscribe Protocol](https://en.wikipedia.org/wiki/Data_Distribution_Service)（RTPS）
* Web Service的[Simple Object Access Protocol](https://en.wikipedia.org/wiki/SOAP)（SOAP）
* 如果要求足够简单，双方都是HTTP Endpoint，直接使用HTTP也可以（如JSON-RPC）
* ……

### 如何表示方法？

“如何表示方法”，这在本地方法调用中其实也不成问题，因为编译器或者解释器会根据语言规范，把调用的方法转换为进程地址空间中方法入口位置的指针。

不过一旦考虑到不同语言，这件事儿又麻烦起来了，因为每门语言的方法签名都可能有所差别，所以，针对“如何表示一个方法”和“如何找到这些方法”这两个问题，我们还是得有个统一的标准。

这个标准做起来其实可以很简单：只要给程序中的每个方法，都规定一个通用的又绝对不会重复的编号；在调用的时候，直接传这个编号就可以找到对应的方法。这种听起来无比寒碜的办法，还真的就是DCE/RPC最初准备的解决方案。

虽然最后，DCE还是弄出了一套跟语言无关的[接口描述语言](https://en.wikipedia.org/wiki/Interface_description_language)（Interface Description Language，IDL），成为了此后许多RPC参考或依赖的基础（如CORBA的OMG IDL），但那个唯一的“绝不重复”的编码方案[UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)，却意外地流行了起来，已经被广泛应用到了程序开发的方方面面。

这类用于表示方法的协议还有：

* Android的[Android Interface Definition Language](https://developer.android.com/guide/components/aidl)（AIDL）
* CORBA的[OMG Interface Definition Language](https://www.omg.org/spec/IDL)（OMG IDL）
* Web Service的[Web Service Description Language](https://zh.wikipedia.org/wiki/WSDL)（WSDL）
* JSON-RPC的[JSON Web Service Protocol](https://en.wikipedia.org/wiki/JSON-WSP)（JSON-WSP）
* ……

你看，如何表示数据、如何传递数据、如何表示方法这三个RPC中的基本问题，都可以在本地方法调用中找到对应的操作。RPC的思想始于本地方法调用，尽管它早就不再追求要跟本地方法调用的实现完全一样了，但RPC的发展仍然带有本地方法调用的深刻烙印。因此，我们在理解PRC的本质时，比较轻松的方式是，以它和本地调用的联系来对比着理解。

好，理解了RPC要解决的三个基本问题以后，我们接着来看一下，现代的RPC框架都为我们提供了哪些可选的解决方案，以及为什么今天会有这么多的RPC框架在并行发展。

## 统一的RPC

DCE/RPC与ONC RPC都有很浓厚的Unix痕迹，所以它们其实并没有真正地在Unix系统以外大规模流行过，而且它们还有一个“大问题”：**只支持传递值而不支持传递对象**（ONC RPC的XDR的序列化器能用于序列化结构体，但结构体毕竟不是对象）。这两个RPC协议都是面向C语言设计的，根本就没有对象的概念。

而90年代，正好又是[面向对象编程](https://en.wikipedia.org/wiki/Object-oriented_programming)（Object-Oriented Programming，OOP）风头正盛的年代，所以在1991年，[对象管理组织](https://zh.wikipedia.org/wiki/对象管理组织)（Object Management Group，OMG）便发布了跨进程、面向异构语言的、支持面向对象的服务调用协议：**CORBA 1.0**（Common Object Request Broker Architecture）。

CORBA 1.0和1.1版本只提供了对C和C++的支持，而到了末代的CORBA 3.0版本，不仅支持了C、C++、Java、Object Pascal、Python、Ruby等多种主流编程语言，还支持了Smalltalk、Lisp、Ada、COBOL等已经“半截入土”的非主流语言，阵营不可谓不强大。

可以这么说，CORBA是一套由国际标准组织牵头、由多个软件提供商共同参与的分布式规范。在当时，只有微软私有的[DCOM](https://zh.wikipedia.org/wiki/Distributed_COM)的影响力可以稍微跟CORBA抗衡一下。但是，与DCE一样，DCOM也受限于操作系统（不过比DCE厉害的是，DCOM能跨语言哟）。所以，能够同时支持跨系统、跨语言的CORBA，其实原本是最有机会统一RPC这个细分领域的竞争者。

但很无奈的是，CORBA并没有抓住这个机会。一方面，CORBA本身的设计实在是太过于啰嗦和繁琐了，甚至有些规定简直到了荒谬的程度。比如说，我们要写一个**对象请求代理**（ORB，这是CORBA中的关键概念）大概要200行代码，其中大概有170行是纯粹无用的废话（这句带有鞭尸性质的得罪人的评价不是我说的，是CORBA的首席科学家Michi Henning在文章《[The Rise and Fall of CORBA](https://dl.acm.org/doi/pdf/10.1145/1142031.1142044)》中自己说的）。

另一方面，为CORBA制定规范的专家逐渐脱离实际了，所以做出的CORBA规范非常晦涩难懂，导致各家语言的厂商都有自己的解读，结果弄出来的CORBA实现互不兼容，实在是对CORBA号称支持众多异构语言的莫大讽刺。这也间接造就了后来**W3C Web Service**的出现。

所以，Web Service一出现，CORBA就在这场竞争中，犹如十八路诸侯讨董卓，互乱阵脚、一触即溃，局面可以说是惨败无比。**最终下场就是，CORBA和DCOM一起被扫进了计算机历史的博物馆中，而Web Service获得了一统RPC的大好机会。**

1998年，XML 1.0发布，并成为了[万维网联盟](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium)（World Wide Web Consortium，W3C）的推荐标准。1999年末，以XML为基础的SOAP 1.0（Simple Object Access Protocol）规范的发布，代表着一种被称为“Web Service”的全新RPC协议的诞生。

Web Service是由微软和DevelopMentor公司共同起草的远程服务协议，随后被提交给W3C，并通过投票成为了国际标准。所以，Web Service也被称为是W3C Web Service。

Web Service采用了XML作为远程过程调用的序列化、接口描述、服务发现等所有编码的载体，当时XML是计算机工业最新的银弹，只要是定义为XML的东西，几乎就都被认为是好的，风头一时无两，连微软自己都主动宣布放弃DCOM，迅速转投Web Service的怀抱。

交给W3C管理后，Web Service再没有天生属于哪家公司的烙印，商业运作非常成功，很受市场欢迎，大量的厂商都想分一杯羹。但从技术角度来看，它设计得也并不优秀，甚至同样可以说是有显著缺陷。

对于开发者而言，**Web Service的一大缺点，就是过于严格的数据和接口定义所带来的性能问题。**

虽然Web Service吸取了CORBA的教训，不再需要程序员手工去编写对象的描述和服务代理了，但是XML作为一门描述性语言，本身的信息密度就很低（都不用与二进制协议比，与今天的JSON或YAML比一下就知道了）。同时，Web Service是一个跨语言的RPC协议，这使得一个简单的字段，为了在不同语言中不会产生歧义，要以XML描述去清楚的话，往往比原本存储这个字段值的空间多出十几倍、几十倍乃至上百倍。

这个特点就导致了，要想使用Web Service，就必须要有专门的客户端去调用和解析SOAP内容，也需要专门的服务去部署（如Java中的Apache Axis/CXF）；更关键的是，这导致了每一次数据交互都包含大量的冗余信息，性能非常差。

如果只是需要客户端、传输性能差也就算了，[又不是不能用](https://www.zhihu.com/topic/20003839/hot)。既然选择了XML来获得自描述能力，也就代表着没打算把性能放到第一位。但是，Web Service还有另外一点原罪：**贪婪**。

“贪婪”是指，它希望在一套协议上，一揽子解决分布式计算中可能遇到的所有问题。这导致Web Service生出了一整个家族的协议出来。

Web Service协议家族中，除它本身包括了的SOAP、WSDL、UDDI协议之外，还有一堆以[WS-\*](https://en.wikipedia.org/wiki/List_of_web_service_specifications)命名的子功能协议，来解决事务、一致性、事件、通知、业务描述、安全、防重放等问题。这些几乎数不清个数的家族协议，对开发者来说学习负担极其沉重。结果就是，得罪惨了开发者，谁爱用谁用去。

当程序员们对Web Service的热情迅速燃起，又逐渐冷却之后，也不禁开始反思：那些**面向透明的、简单的RPC协议**，如DCE/RPC、DCOM、Java RMI，要么依赖于操作系统，要么依赖于特定语言，总有一些先天约束；那些**面向通用的、普适的RPC协议**，如CORBA，就无法逃过使用复杂性的困扰；而那些**意图通过技术手段来屏蔽复杂性的RPC协议**，如Web Service，又不免受到性能问题的束缚。

简单、普适和高性能，似乎真的难以同时满足。

## 分裂的RPC

由于一直没有一个能同时满足以上简单、普适和高性能的“完美RPC协议”，因此远程服务器调用这个小小的领域就逐渐进入了群雄混战、百家争鸣的“战国时代”，距离“统一”越来越远，并一直延续至今。

我们看看相继出现过的RPC协议/框架，就能明白了：RMI（Sun/Oracle）、Thrift（Facebook/Apache）、Dubbo（阿里巴巴/Apache）、gRPC（Google）、Motan2（新浪）、Finagle（Twitter）、brpc（百度）、.NET Remoting（微软）、Arvo（Hadoop）、JSON-RPC 2.0（公开规范，JSON-RPC工作组）……

这些RPC的功能、特点都不太一样，有的是某种语言私有，有的能支持跨越多门语言，有的运行在HTTP协议之上，有的能直接运行于TCP/UDP之上，但没有哪一款是“最完美的RPC”。据此，我们也可以发现一个规律，任何一款具有生命力的RPC框架，都不再去追求大而全的“完美”，而是会找到一个独特的点作为主要的发展方向。

我们看几个典型的发展方向：

* **朝着面向对象发展**。这条线的缘由在于，在分布式系统中，开发者们不再满足于RPC带来的面向过程的编码方式，而是希望能够进行跨进程的面向对象编程。因此，这条线还有一个别名叫作[分布式对象](https://en.wikipedia.org/wiki/Distributed_object)（Distributed Object），它的代表有**RMI、.NET Remoting**。当然了，之前的CORBA和DCOM也可以归入这一类。
* **朝着性能发展**，代表为**gRPC和Thrift**。决定RPC性能主要就两个因素：序列化效率和信息密度。序列化效率很好理解，序列化输出结果的容量越小，速度越快，效率自然越高；信息密度则取决于协议中，有效荷载（Payload）所占总传输数据的比例大小，使用传输协议的层次越高，信息密度就越低，SOAP使用XML拙劣的性能表现就是前车之鉴。gRPC和Thrift都有自己优秀的专有序列化器，而在传输协议方面，gRPC是基于HTTP/2的，支持多路复用和Header压缩，Thrift则直接基于传输层的TCP协议来实现，省去了额外的应用层协议的开销。
* **朝着简化发展**，代表为**JSON-RPC**。要是说选出功能最强、速度最快的RPC可能会有争议，但要选出哪个功能弱的、速度慢的，JSON-RPC肯定会是候选人之一。它牺牲了功能和效率，换来的是协议的简单。也就是说，JSON-RPC的接口与格式的通用性很好，尤其适合用在Web浏览器这类一般不会有额外协议、客户端支持的应用场合。
* ……

经历了RPC框架的“战国时代”，开发者们终于认可了，不同的RPC框架所提供的不同特性或多或少是互相矛盾的，很难有某一种框架说“我全部都要”。

要把面向对象那套全搬过来，就注定不会太简单（比如建Stub、Skeleton就很烦了，即使由IDL生成也很麻烦）；功能多起来，协议就要弄得复杂，效率一般就会受影响；要简单易用，那很多事情就必须遵循约定而不是配置才行；要重视效率，那就需要采用二进制的序列化器和较底层的传输协议，支持的语言范围容易受限。

也正是因为每一种RPC框架都有不完美的地方，才会有新的RPC轮子不断出现。

而到了最近几年，RPC框架有明显朝着更高层次（不仅仅负责调用远程服务，还管理远程服务）与插件化方向发展的趋势，**不再选择自己去解决表示数据、传递数据和表示方法这三个问题，而是将全部或者一部分问题设计为扩展点，实现核心能力的可配置**，再辅以外围功能，如负载均衡、服务注册、可观察性等方面的支持。这一类框架的代表，有Facebook的Thrift和阿里的Dubbo（现在两者都是Apache的）。

尤其是断更多年后重启的Dubbo表现得更为明显，它默认有自己的传输协议（Dubbo协议），同时也支持其他协议，它默认采用Hessian 2作为序列化器，如果你有JSON的需求，可以替换为Fastjson；如果你对性能有更高的需求，可以替换为[Kryo](https://github.com/EsotericSoftware/kryo)、[FST](https://github.com/RuedigerMoeller/fast-serialization)、Protocol Buffers等；如果你不想依赖其他包，直接使用JDK自带的序列化器也可以。这种设计，就在一定程度上缓解了RPC框架必须取舍，难以完美的缺憾。

## 小结

今天，我们一起学习了RPC协议在工业界的发展，包括它要解决的三个基本问题，以及层出不穷的RPC协议/框架。

表示数据、传递数据和表示方法，是RPC必须解决的三大基本问题。要解决这些问题，可以有很多方案，这也是RPC协议/框架出现群雄混战局面的一个原因。

出现这种分裂局面的另一个原因，是简单的框架很难能达到功能强大的要求。

功能强大的框架往往要在传输中加入额外的负载和控制措施，导致传输性能降低，而如果既想要高性能，又想要强功能，这就必然要依赖大量的技巧去实现，进而也就导致了框架会变得过于复杂，这就决定了不可能有一个“完美”的框架同时满足简单、普适和高性能这三个要求。

认识到这一点后，一个RPC框架要想取得成功，就要选择一个发展方向，能够非常好地满足某一方面的需求。因此，我们也就有了朝着面向对象发展、朝着性能发展和朝着简化发展这三条线。

以上就是这一讲我要和你分享的RPC在工业界的发展成果了。这也是，你在日后工作中选择RPC实现方案的一个参考。

最后，我再和你分享一点我的心得。我在讲到DCOM、CORBA、Web Service的失败的时候，虽然说我的口吻多少有一些戏谑，但我们得明确一点：这些框架即使没有成功，但作为早期的探索先驱，并没有什么应该被讽刺的地方。而且其后续的发展，都称得上是知耻后勇，反而值得我们的掌声赞赏。

比如，说到CORBA的消亡，OMG痛定思痛之后，提出了基于RTPS协议栈的“[数据分发服务](https://en.wikipedia.org/wiki/Data_Distribution_Service)”商业标准（Data Distribution Service，DDS，“商业”就是要付费使用的意思）。这个标准现在主要用在物联网领域，能够做到微秒级延时，还能支持大规模并发通讯。

再比如，说到DCOM的失败和Web Service的衰落，微软在它们的基础上，推出了[.NET WCF](https://en.wikipedia.org/wiki/Windows_Communication_Foundation)（Windows Communication Foundation，Windows通信基础）。

.NET WCF的优势主要有两点：一是，把REST、TCP、SOAP等不同形式的调用，自动封装为了完全一致的、如同本地方法调用一般的程序接口；二是，依靠自家的“地表最强IDE”Visual Studio，把工作量减少到只需要指定一个远程服务地址，就可以获取服务描述、绑定各种特性（如安全传输）、自动生成客户端调用代码，甚至还能选择同步还是异步之类细节的程度。

虽然.NET WCF只支持.NET平台，而且也是采用XML语言描述，但使用体验真的是非常畅快，足够挽回Web Service得罪开发者丢掉的全部印象分。

## 一课一思

我们通过两讲学习了RPC在学术界和工业界的发展后，再回过头来思考一个问题：**开发一个分布式系统，是不是就一定要用RPC呢？**

我提供给你一个分析思路吧。RPC的三大问题源自对本地方法调用的类比模拟，如果我们把思维从“方法调用”的约束中挣脱，那参数与结果如何表示、方法如何表示、数据如何传递这些问题，都会海阔天空，拥有焕然一新的视角。但是我们写程序，真的可能不面向方法来编程吗？

这就是我在下一讲准备跟你探讨的话题了。现在你可以先自己思考一下，欢迎在留言区分享你的看法。另外，如果觉得有收获，也非常欢迎你把今天的内容分享给更多的朋友。

好，感谢你的阅读，我们下一讲再见。