# Redis 源码剖析与实战 

Source: https://learn.lianglianglee.com/专栏/Redis 源码剖析与实战

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# Redis 源码剖析与实战

* [00 开篇词 阅读Redis源码能给你带来什么？.md](/专栏/Redis 源码剖析与实战/00  开篇词  阅读Redis源码能给你带来什么？.md)
* [01 带你快速攻略Redis源码的整体架构.md](/专栏/Redis 源码剖析与实战/01  带你快速攻略Redis源码的整体架构.md)
* [02 键值对中字符串的实现，用char还是结构体？.md](/专栏/Redis 源码剖析与实战/02  键值对中字符串的实现，用char还是结构体？.md)
* [03 如何实现一个性能优异的Hash表？.md](/专栏/Redis 源码剖析与实战/03  如何实现一个性能优异的Hash表？.md)
* [04 内存友好的数据结构该如何细化设计？.md](/专栏/Redis 源码剖析与实战/04  内存友好的数据结构该如何细化设计？.md)
* [05 有序集合为何能同时支持点查询和范围查询？.md](/专栏/Redis 源码剖析与实战/05  有序集合为何能同时支持点查询和范围查询？.md)
* [06 从ziplist到quicklist，再到listpack的启发.md](/专栏/Redis 源码剖析与实战/06  从ziplist到quicklist，再到listpack的启发.md)
* [07 为什么Stream使用了Radix Tree？.md](/专栏/Redis 源码剖析与实战/07  为什么Stream使用了Radix Tree？.md)
* [08 Redis server启动后会做哪些操作？.md](/专栏/Redis 源码剖析与实战/08  Redis server启动后会做哪些操作？.md)
* [09 Redis事件驱动框架（上）：何时使用select、poll、epoll？.md](/专栏/Redis 源码剖析与实战/09  Redis事件驱动框架（上）：何时使用select、poll、epoll？.md)
* [10 Redis事件驱动框架（中）：Redis实现了Reactor模型吗？.md](/专栏/Redis 源码剖析与实战/10  Redis事件驱动框架（中）：Redis实现了Reactor模型吗？.md)
* [11 Redis事件驱动框架（下）：Redis有哪些事件？.md](/专栏/Redis 源码剖析与实战/11  Redis事件驱动框架（下）：Redis有哪些事件？.md)
* [12 Redis真的是单线程吗？.md](/专栏/Redis 源码剖析与实战/12  Redis真的是单线程吗？.md)
* [13 Redis 6.0多IO线程的效率提高了吗？.md](/专栏/Redis 源码剖析与实战/13  Redis 6.0多IO线程的效率提高了吗？.md)
* [14 从代码实现看分布式锁的原子性保证.md](/专栏/Redis 源码剖析与实战/14  从代码实现看分布式锁的原子性保证.md)
* [15 为什么LRU算法原理和代码实现不一样？.md](/专栏/Redis 源码剖析与实战/15  为什么LRU算法原理和代码实现不一样？.md)
* [16 LFU算法和其他算法相比有优势吗？.md](/专栏/Redis 源码剖析与实战/16  LFU算法和其他算法相比有优势吗？.md)
* [17 Lazy Free会影响缓存替换吗？.md](/专栏/Redis 源码剖析与实战/17  Lazy Free会影响缓存替换吗？.md)
* [18 如何生成和解读RDB文件？.md](/专栏/Redis 源码剖析与实战/18  如何生成和解读RDB文件？.md)
* [19 AOF重写（上）：触发时机与重写的影响.md](/专栏/Redis 源码剖析与实战/19  AOF重写（上）：触发时机与重写的影响.md)
* [20 AOF重写（下）：重写时的新写操作记录在哪里？.md](/专栏/Redis 源码剖析与实战/20  AOF重写（下）：重写时的新写操作记录在哪里？.md)
* [21 主从复制：基于状态机的设计与实现.md](/专栏/Redis 源码剖析与实战/21  主从复制：基于状态机的设计与实现.md)
* [22 哨兵也和Redis实例一样初始化吗？.md](/专栏/Redis 源码剖析与实战/22  哨兵也和Redis实例一样初始化吗？.md)
* [23 从哨兵Leader选举学习Raft协议实现（上）.md](/专栏/Redis 源码剖析与实战/23  从哨兵Leader选举学习Raft协议实现（上）.md)
* [24 从哨兵Leader选举学习Raft协议实现（下）.md](/专栏/Redis 源码剖析与实战/24  从哨兵Leader选举学习Raft协议实现（下）.md)
* [25 PubSub在主从故障切换时是如何发挥作用的？.md](/专栏/Redis 源码剖析与实战/25  PubSub在主从故障切换时是如何发挥作用的？.md)
* [26 从Ping-Pong消息学习Gossip协议的实现.md](/专栏/Redis 源码剖析与实战/26  从Ping-Pong消息学习Gossip协议的实现.md)
* [27 从MOVED、ASK看集群节点如何处理命令？.md](/专栏/Redis 源码剖析与实战/27  从MOVED、ASK看集群节点如何处理命令？.md)
* [28 Redis Cluster数据迁移会阻塞吗？.md](/专栏/Redis 源码剖析与实战/28  Redis Cluster数据迁移会阻塞吗？.md)
* [29 如何正确实现循环缓冲区？.md](/专栏/Redis 源码剖析与实战/29  如何正确实现循环缓冲区？.md)
* [30 如何在系统中实现延迟监控？.md](/专栏/Redis 源码剖析与实战/30  如何在系统中实现延迟监控？.md)
* [31 从Module的实现学习动态扩展功能.md](/专栏/Redis 源码剖析与实战/31  从Module的实现学习动态扩展功能.md)
* [32 如何在一个系统中实现单元测试？.md](/专栏/Redis 源码剖析与实战/32  如何在一个系统中实现单元测试？.md)
* [结束语 Redis源码阅读，让我们从新开始.md](/专栏/Redis 源码剖析与实战/结束语  Redis源码阅读，让我们从新开始.md)