# MySQL · 引擎特性 · InnoDB 同步机制 

Source: https://learn.lianglianglee.com/文章/MySQL · 引擎特性 · InnoDB 同步机制.md

MySQL · 引擎特性 · InnoDB 同步机制 



[![](/static/favicon.png)
技术文章摘抄](/)

* [首页](/)
* [上一级](../)

* [AQS 万字图文全面解析.md](/%e6%96%87%e7%ab%a0/AQS%20%e4%b8%87%e5%ad%97%e5%9b%be%e6%96%87%e5%85%a8%e9%9d%a2%e8%a7%a3%e6%9e%90.md)
* [Docker 镜像构建原理及源码分析.md](/%e6%96%87%e7%ab%a0/Docker%20%e9%95%9c%e5%83%8f%e6%9e%84%e5%bb%ba%e5%8e%9f%e7%90%86%e5%8f%8a%e6%ba%90%e7%a0%81%e5%88%86%e6%9e%90.md)
* [ElasticSearch 小白从入门到精通.md](/%e6%96%87%e7%ab%a0/ElasticSearch%20%e5%b0%8f%e7%99%bd%e4%bb%8e%e5%85%a5%e9%97%a8%e5%88%b0%e7%b2%be%e9%80%9a.md)
* [JVM CPU Profiler技术原理及源码深度解析.md](/%e6%96%87%e7%ab%a0/JVM%20CPU%20Profiler%e6%8a%80%e6%9c%af%e5%8e%9f%e7%90%86%e5%8f%8a%e6%ba%90%e7%a0%81%e6%b7%b1%e5%ba%a6%e8%a7%a3%e6%9e%90.md)
* [JVM 垃圾收集器.md](/%e6%96%87%e7%ab%a0/JVM%20%e5%9e%83%e5%9c%be%e6%94%b6%e9%9b%86%e5%99%a8.md)
* [JVM 面试的 30 个知识点.md](/%e6%96%87%e7%ab%a0/JVM%20%e9%9d%a2%e8%af%95%e7%9a%84%2030%20%e4%b8%aa%e7%9f%a5%e8%af%86%e7%82%b9.md)
* [Java IO 体系、线程模型大总结.md](/%e6%96%87%e7%ab%a0/Java%20IO%20%e4%bd%93%e7%b3%bb%e3%80%81%e7%ba%bf%e7%a8%8b%e6%a8%a1%e5%9e%8b%e5%a4%a7%e6%80%bb%e7%bb%93.md)
* [Java NIO浅析.md](/%e6%96%87%e7%ab%a0/Java%20NIO%e6%b5%85%e6%9e%90.md)
* [Java 面试题集锦（网络篇）.md](/%e6%96%87%e7%ab%a0/Java%20%e9%9d%a2%e8%af%95%e9%a2%98%e9%9b%86%e9%94%a6%ef%bc%88%e7%bd%91%e7%bb%9c%e7%af%87%ef%bc%89.md)
* [Java-直接内存 DirectMemory 详解.md](/%e6%96%87%e7%ab%a0/Java-%e7%9b%b4%e6%8e%a5%e5%86%85%e5%ad%98%20DirectMemory%20%e8%af%a6%e8%a7%a3.md)
* [Java中9种常见的CMS GC问题分析与解决（上）.md](/%e6%96%87%e7%ab%a0/Java%e4%b8%ad9%e7%a7%8d%e5%b8%b8%e8%a7%81%e7%9a%84CMS%20GC%e9%97%ae%e9%a2%98%e5%88%86%e6%9e%90%e4%b8%8e%e8%a7%a3%e5%86%b3%ef%bc%88%e4%b8%8a%ef%bc%89.md)
* [Java中9种常见的CMS GC问题分析与解决（下）.md](/%e6%96%87%e7%ab%a0/Java%e4%b8%ad9%e7%a7%8d%e5%b8%b8%e8%a7%81%e7%9a%84CMS%20GC%e9%97%ae%e9%a2%98%e5%88%86%e6%9e%90%e4%b8%8e%e8%a7%a3%e5%86%b3%ef%bc%88%e4%b8%8b%ef%bc%89.md)
* [Java中的SPI.md](/%e6%96%87%e7%ab%a0/Java%e4%b8%ad%e7%9a%84SPI.md)
* [Java中的ThreadLocal.md](/%e6%96%87%e7%ab%a0/Java%e4%b8%ad%e7%9a%84ThreadLocal.md)
* [Java线程池实现原理及其在美团业务中的实践.md](/%e6%96%87%e7%ab%a0/Java%e7%ba%bf%e7%a8%8b%e6%b1%a0%e5%ae%9e%e7%8e%b0%e5%8e%9f%e7%90%86%e5%8f%8a%e5%85%b6%e5%9c%a8%e7%be%8e%e5%9b%a2%e4%b8%9a%e5%8a%a1%e4%b8%ad%e7%9a%84%e5%ae%9e%e8%b7%b5.md)
* [Java魔法类：Unsafe应用解析.md](/%e6%96%87%e7%ab%a0/Java%e9%ad%94%e6%b3%95%e7%b1%bb%ef%bc%9aUnsafe%e5%ba%94%e7%94%a8%e8%a7%a3%e6%9e%90.md)
* [Kafka 源码阅读笔记.md](/%e6%96%87%e7%ab%a0/Kafka%20%e6%ba%90%e7%a0%81%e9%98%85%e8%af%bb%e7%ac%94%e8%ae%b0.md)
* [Kafka、ActiveMQ、RabbitMQ、RocketMQ 区别以及高可用原理.md](/%e6%96%87%e7%ab%a0/Kafka%e3%80%81ActiveMQ%e3%80%81RabbitMQ%e3%80%81RocketMQ%20%e5%8c%ba%e5%88%ab%e4%bb%a5%e5%8f%8a%e9%ab%98%e5%8f%af%e7%94%a8%e5%8e%9f%e7%90%86.md)
* [MySQL · 引擎特性 · InnoDB Buffer Pool.md](/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20InnoDB%20Buffer%20Pool.md)
* [MySQL · 引擎特性 · InnoDB IO子系统.md](/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20InnoDB%20IO%e5%ad%90%e7%b3%bb%e7%bb%9f.md)
* [MySQL · 引擎特性 · InnoDB 事务系统.md](/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20InnoDB%20%e4%ba%8b%e5%8a%a1%e7%b3%bb%e7%bb%9f.md)
* [MySQL · 引擎特性 · InnoDB 同步机制.md](/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20InnoDB%20%e5%90%8c%e6%ad%a5%e6%9c%ba%e5%88%b6.md)
* [MySQL · 引擎特性 · InnoDB 数据页解析.md](/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20InnoDB%20%e6%95%b0%e6%8d%ae%e9%a1%b5%e8%a7%a3%e6%9e%90.md)
* [MySQL · 引擎特性 · InnoDB崩溃恢复.md](/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20InnoDB%e5%b4%a9%e6%ba%83%e6%81%a2%e5%a4%8d.md)
* [MySQL · 引擎特性 · 临时表那些事儿.md](/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20%e4%b8%b4%e6%97%b6%e8%a1%a8%e9%82%a3%e4%ba%9b%e4%ba%8b%e5%84%bf.md)
* [MySQL 主从复制 半同步复制.md](/%e6%96%87%e7%ab%a0/MySQL%20%e4%b8%bb%e4%bb%8e%e5%a4%8d%e5%88%b6%20%e5%8d%8a%e5%90%8c%e6%ad%a5%e5%a4%8d%e5%88%b6.md)
* [MySQL 主从复制 基于GTID复制.md](/%e6%96%87%e7%ab%a0/MySQL%20%e4%b8%bb%e4%bb%8e%e5%a4%8d%e5%88%b6%20%e5%9f%ba%e4%ba%8eGTID%e5%a4%8d%e5%88%b6.md)
* [MySQL 主从复制.md](/%e6%96%87%e7%ab%a0/MySQL%20%e4%b8%bb%e4%bb%8e%e5%a4%8d%e5%88%b6.md)
* [MySQL 事务日志(redo log和undo log).md](/%e6%96%87%e7%ab%a0/MySQL%20%e4%ba%8b%e5%8a%a1%e6%97%a5%e5%bf%97%28redo%20log%e5%92%8cundo%20log%29.md)
* [MySQL 亿级别数据迁移实战代码分享.md](/%e6%96%87%e7%ab%a0/MySQL%20%e4%ba%bf%e7%ba%a7%e5%88%ab%e6%95%b0%e6%8d%ae%e8%bf%81%e7%a7%bb%e5%ae%9e%e6%88%98%e4%bb%a3%e7%a0%81%e5%88%86%e4%ba%ab.md)
* [MySQL 从一条数据说起-InnoDB行存储数据结构.md](/%e6%96%87%e7%ab%a0/MySQL%20%e4%bb%8e%e4%b8%80%e6%9d%a1%e6%95%b0%e6%8d%ae%e8%af%b4%e8%b5%b7-InnoDB%e8%a1%8c%e5%ad%98%e5%82%a8%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84.md)
* [MySQL 地基基础：事务和锁的面纱.md](/%e6%96%87%e7%ab%a0/MySQL%20%e5%9c%b0%e5%9f%ba%e5%9f%ba%e7%a1%80%ef%bc%9a%e4%ba%8b%e5%8a%a1%e5%92%8c%e9%94%81%e7%9a%84%e9%9d%a2%e7%ba%b1.md)
* [MySQL 地基基础：数据字典.md](/%e6%96%87%e7%ab%a0/MySQL%20%e5%9c%b0%e5%9f%ba%e5%9f%ba%e7%a1%80%ef%bc%9a%e6%95%b0%e6%8d%ae%e5%ad%97%e5%85%b8.md)
* [MySQL 地基基础：数据库字符集.md](/%e6%96%87%e7%ab%a0/MySQL%20%e5%9c%b0%e5%9f%ba%e5%9f%ba%e7%a1%80%ef%bc%9a%e6%95%b0%e6%8d%ae%e5%ba%93%e5%ad%97%e7%ac%a6%e9%9b%86.md)
* [MySQL 性能优化：碎片整理.md](/%e6%96%87%e7%ab%a0/MySQL%20%e6%80%a7%e8%83%bd%e4%bc%98%e5%8c%96%ef%bc%9a%e7%a2%8e%e7%89%87%e6%95%b4%e7%90%86.md)
* [MySQL 故障诊断：一个 ALTER TALBE 执行了很久，你慌不慌？.md](/%e6%96%87%e7%ab%a0/MySQL%20%e6%95%85%e9%9a%9c%e8%af%8a%e6%96%ad%ef%bc%9a%e4%b8%80%e4%b8%aa%20ALTER%20TALBE%20%e6%89%a7%e8%a1%8c%e4%ba%86%e5%be%88%e4%b9%85%ef%bc%8c%e4%bd%a0%e6%85%8c%e4%b8%8d%e6%85%8c%ef%bc%9f.md)
* [MySQL 故障诊断：如何在日志中轻松定位大事务.md](/%e6%96%87%e7%ab%a0/MySQL%20%e6%95%85%e9%9a%9c%e8%af%8a%e6%96%ad%ef%bc%9a%e5%a6%82%e4%bd%95%e5%9c%a8%e6%97%a5%e5%bf%97%e4%b8%ad%e8%bd%bb%e6%9d%be%e5%ae%9a%e4%bd%8d%e5%a4%a7%e4%ba%8b%e5%8a%a1.md)
* [MySQL 故障诊断：教你快速定位加锁的 SQL.md](/%e6%96%87%e7%ab%a0/MySQL%20%e6%95%85%e9%9a%9c%e8%af%8a%e6%96%ad%ef%bc%9a%e6%95%99%e4%bd%a0%e5%bf%ab%e9%80%9f%e5%ae%9a%e4%bd%8d%e5%8a%a0%e9%94%81%e7%9a%84%20SQL.md)
* [MySQL 日志详解.md](/%e6%96%87%e7%ab%a0/MySQL%20%e6%97%a5%e5%bf%97%e8%af%a6%e8%a7%a3.md)
* [MySQL 的半同步是什么？.md](/%e6%96%87%e7%ab%a0/MySQL%20%e7%9a%84%e5%8d%8a%e5%90%8c%e6%ad%a5%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f.md)
* [MySQL中的事务和MVCC.md](/%e6%96%87%e7%ab%a0/MySQL%e4%b8%ad%e7%9a%84%e4%ba%8b%e5%8a%a1%e5%92%8cMVCC.md)
* [MySQL事务\_事务隔离级别详解.md](/%e6%96%87%e7%ab%a0/MySQL%e4%ba%8b%e5%8a%a1_%e4%ba%8b%e5%8a%a1%e9%9a%94%e7%a6%bb%e7%ba%a7%e5%88%ab%e8%af%a6%e8%a7%a3.md)
* [MySQL优化：优化 select count().md](/%e6%96%87%e7%ab%a0/MySQL%e4%bc%98%e5%8c%96%ef%bc%9a%e4%bc%98%e5%8c%96%20select%20count%28%29.md)
* [MySQL共享锁、排他锁、悲观锁、乐观锁.md](/%e6%96%87%e7%ab%a0/MySQL%e5%85%b1%e4%ba%ab%e9%94%81%e3%80%81%e6%8e%92%e4%bb%96%e9%94%81%e3%80%81%e6%82%b2%e8%a7%82%e9%94%81%e3%80%81%e4%b9%90%e8%a7%82%e9%94%81.md)
* [MySQL的MVCC（多版本并发控制）.md](/%e6%96%87%e7%ab%a0/MySQL%e7%9a%84MVCC%ef%bc%88%e5%a4%9a%e7%89%88%e6%9c%ac%e5%b9%b6%e5%8f%91%e6%8e%a7%e5%88%b6%ef%bc%89.md)
* [QingStor 对象存储架构设计及最佳实践.md](/%e6%96%87%e7%ab%a0/QingStor%20%e5%af%b9%e8%b1%a1%e5%ad%98%e5%82%a8%e6%9e%b6%e6%9e%84%e8%ae%be%e8%ae%a1%e5%8f%8a%e6%9c%80%e4%bd%b3%e5%ae%9e%e8%b7%b5.md)
* [RocketMQ 面试题集锦.md](/%e6%96%87%e7%ab%a0/RocketMQ%20%e9%9d%a2%e8%af%95%e9%a2%98%e9%9b%86%e9%94%a6.md)
* [SnowFlake 雪花算法生成分布式 ID.md](/%e6%96%87%e7%ab%a0/SnowFlake%20%e9%9b%aa%e8%8a%b1%e7%ae%97%e6%b3%95%e7%94%9f%e6%88%90%e5%88%86%e5%b8%83%e5%bc%8f%20ID.md)
* [Spring Boot 2.x 结合 k8s 实现分布式微服务架构.md](/%e6%96%87%e7%ab%a0/Spring%20Boot%202.x%20%e7%bb%93%e5%90%88%20k8s%20%e5%ae%9e%e7%8e%b0%e5%88%86%e5%b8%83%e5%bc%8f%e5%be%ae%e6%9c%8d%e5%8a%a1%e6%9e%b6%e6%9e%84.md)
* [Spring Boot 教程：如何开发一个 starter.md](/%e6%96%87%e7%ab%a0/Spring%20Boot%20%e6%95%99%e7%a8%8b%ef%bc%9a%e5%a6%82%e4%bd%95%e5%bc%80%e5%8f%91%e4%b8%80%e4%b8%aa%20starter.md)
* [Spring MVC 原理.md](/%e6%96%87%e7%ab%a0/Spring%20MVC%20%e5%8e%9f%e7%90%86.md)
* [Spring MyBatis和Spring整合的奥秘.md](/%e6%96%87%e7%ab%a0/Spring%20MyBatis%e5%92%8cSpring%e6%95%b4%e5%90%88%e7%9a%84%e5%a5%a5%e7%a7%98.md)
* [Spring 帮助你更好的理解Spring循环依赖.md](/%e6%96%87%e7%ab%a0/Spring%20%e5%b8%ae%e5%8a%a9%e4%bd%a0%e6%9b%b4%e5%a5%bd%e7%9a%84%e7%90%86%e8%a7%a3Spring%e5%be%aa%e7%8e%af%e4%be%9d%e8%b5%96.md)
* [Spring 循环依赖及解决方式.md](/%e6%96%87%e7%ab%a0/Spring%20%e5%be%aa%e7%8e%af%e4%be%9d%e8%b5%96%e5%8f%8a%e8%a7%a3%e5%86%b3%e6%96%b9%e5%bc%8f.md)
* [Spring中眼花缭乱的BeanDefinition.md](/%e6%96%87%e7%ab%a0/Spring%e4%b8%ad%e7%9c%bc%e8%8a%b1%e7%bc%ad%e4%b9%b1%e7%9a%84BeanDefinition.md)
* [Vert.x 基础入门.md](/%e6%96%87%e7%ab%a0/Vert.x%20%e5%9f%ba%e7%a1%80%e5%85%a5%e9%97%a8.md)
* [eBay 的 Elasticsearch 性能调优实践.md](/%e6%96%87%e7%ab%a0/eBay%20%e7%9a%84%20Elasticsearch%20%e6%80%a7%e8%83%bd%e8%b0%83%e4%bc%98%e5%ae%9e%e8%b7%b5.md)
* [不可不说的Java“锁”事.md](/%e6%96%87%e7%ab%a0/%e4%b8%8d%e5%8f%af%e4%b8%8d%e8%af%b4%e7%9a%84Java%e2%80%9c%e9%94%81%e2%80%9d%e4%ba%8b.md)
* [互联网并发限流实战.md](/%e6%96%87%e7%ab%a0/%e4%ba%92%e8%81%94%e7%bd%91%e5%b9%b6%e5%8f%91%e9%99%90%e6%b5%81%e5%ae%9e%e6%88%98.md)
* [从ReentrantLock的实现看AQS的原理及应用.md](/%e6%96%87%e7%ab%a0/%e4%bb%8eReentrantLock%e7%9a%84%e5%ae%9e%e7%8e%b0%e7%9c%8bAQS%e7%9a%84%e5%8e%9f%e7%90%86%e5%8f%8a%e5%ba%94%e7%94%a8.md)
* [从SpringCloud开始，聊微服务架构.md](/%e6%96%87%e7%ab%a0/%e4%bb%8eSpringCloud%e5%bc%80%e5%a7%8b%ef%bc%8c%e8%81%8a%e5%be%ae%e6%9c%8d%e5%8a%a1%e6%9e%b6%e6%9e%84.md)
* [全面了解 JDK 线程池实现原理.md](/%e6%96%87%e7%ab%a0/%e5%85%a8%e9%9d%a2%e4%ba%86%e8%a7%a3%20JDK%20%e7%ba%bf%e7%a8%8b%e6%b1%a0%e5%ae%9e%e7%8e%b0%e5%8e%9f%e7%90%86.md)
* [分布式一致性理论与算法.md](/%e6%96%87%e7%ab%a0/%e5%88%86%e5%b8%83%e5%bc%8f%e4%b8%80%e8%87%b4%e6%80%a7%e7%90%86%e8%ae%ba%e4%b8%8e%e7%ae%97%e6%b3%95.md)
* [分布式一致性算法 Raft.md](/%e6%96%87%e7%ab%a0/%e5%88%86%e5%b8%83%e5%bc%8f%e4%b8%80%e8%87%b4%e6%80%a7%e7%ae%97%e6%b3%95%20Raft.md)
* [分布式唯一 ID 解析.md](/%e6%96%87%e7%ab%a0/%e5%88%86%e5%b8%83%e5%bc%8f%e5%94%af%e4%b8%80%20ID%20%e8%a7%a3%e6%9e%90.md)
* [分布式链路追踪：集群管理设计.md](/%e6%96%87%e7%ab%a0/%e5%88%86%e5%b8%83%e5%bc%8f%e9%93%be%e8%b7%af%e8%bf%bd%e8%b8%aa%ef%bc%9a%e9%9b%86%e7%be%a4%e7%ae%a1%e7%90%86%e8%ae%be%e8%ae%a1.md)
* [动态代理种类及原理，你知道多少？.md](/%e6%96%87%e7%ab%a0/%e5%8a%a8%e6%80%81%e4%bb%a3%e7%90%86%e7%a7%8d%e7%b1%bb%e5%8f%8a%e5%8e%9f%e7%90%86%ef%bc%8c%e4%bd%a0%e7%9f%a5%e9%81%93%e5%a4%9a%e5%b0%91%ef%bc%9f.md)
* [响应式架构与 RxJava 在有赞零售的实践.md](/%e6%96%87%e7%ab%a0/%e5%93%8d%e5%ba%94%e5%bc%8f%e6%9e%b6%e6%9e%84%e4%b8%8e%20RxJava%20%e5%9c%a8%e6%9c%89%e8%b5%9e%e9%9b%b6%e5%94%ae%e7%9a%84%e5%ae%9e%e8%b7%b5.md)
* [大数据算法——布隆过滤器.md](/%e6%96%87%e7%ab%a0/%e5%a4%a7%e6%95%b0%e6%8d%ae%e7%ae%97%e6%b3%95%e2%80%94%e2%80%94%e5%b8%83%e9%9a%86%e8%bf%87%e6%bb%a4%e5%99%a8.md)
* [如何优雅地记录操作日志？.md](/%e6%96%87%e7%ab%a0/%e5%a6%82%e4%bd%95%e4%bc%98%e9%9b%85%e5%9c%b0%e8%ae%b0%e5%bd%95%e6%93%8d%e4%bd%9c%e6%97%a5%e5%bf%97%ef%bc%9f.md)
* [如何设计一个亿级消息量的 IM 系统.md](/%e6%96%87%e7%ab%a0/%e5%a6%82%e4%bd%95%e8%ae%be%e8%ae%a1%e4%b8%80%e4%b8%aa%e4%ba%bf%e7%ba%a7%e6%b6%88%e6%81%af%e9%87%8f%e7%9a%84%20IM%20%e7%b3%bb%e7%bb%9f.md)
* [异步网络模型.md](/%e6%96%87%e7%ab%a0/%e5%bc%82%e6%ad%a5%e7%bd%91%e7%bb%9c%e6%a8%a1%e5%9e%8b.md)
* [当我们在讨论CQRS时，我们在讨论些神马？.md](/%e6%96%87%e7%ab%a0/%e5%bd%93%e6%88%91%e4%bb%ac%e5%9c%a8%e8%ae%a8%e8%ae%baCQRS%e6%97%b6%ef%bc%8c%e6%88%91%e4%bb%ac%e5%9c%a8%e8%ae%a8%e8%ae%ba%e4%ba%9b%e7%a5%9e%e9%a9%ac%ef%bc%9f.md)
* [彻底理解 MySQL 的索引机制.md](/%e6%96%87%e7%ab%a0/%e5%bd%bb%e5%ba%95%e7%90%86%e8%a7%a3%20MySQL%20%e7%9a%84%e7%b4%a2%e5%bc%95%e6%9c%ba%e5%88%b6.md)
* [最全的 116 道 Redis 面试题解答.md](/%e6%96%87%e7%ab%a0/%e6%9c%80%e5%85%a8%e7%9a%84%20116%20%e9%81%93%20Redis%20%e9%9d%a2%e8%af%95%e9%a2%98%e8%a7%a3%e7%ad%94.md)
* [有赞权限系统(SAM).md](/%e6%96%87%e7%ab%a0/%e6%9c%89%e8%b5%9e%e6%9d%83%e9%99%90%e7%b3%bb%e7%bb%9f%28SAM%29.md)
* [有赞零售中台建设方法的探索与实践.md](/%e6%96%87%e7%ab%a0/%e6%9c%89%e8%b5%9e%e9%9b%b6%e5%94%ae%e4%b8%ad%e5%8f%b0%e5%bb%ba%e8%ae%be%e6%96%b9%e6%b3%95%e7%9a%84%e6%8e%a2%e7%b4%a2%e4%b8%8e%e5%ae%9e%e8%b7%b5.md)
* [服务注册与发现原理剖析（Eureka、Zookeeper、Nacos）.md](/%e6%96%87%e7%ab%a0/%e6%9c%8d%e5%8a%a1%e6%b3%a8%e5%86%8c%e4%b8%8e%e5%8f%91%e7%8e%b0%e5%8e%9f%e7%90%86%e5%89%96%e6%9e%90%ef%bc%88Eureka%e3%80%81Zookeeper%e3%80%81Nacos%ef%bc%89.md)
* [深入浅出Cache.md](/%e6%96%87%e7%ab%a0/%e6%b7%b1%e5%85%a5%e6%b5%85%e5%87%baCache.md)
* [深入理解 MySQL 底层实现.md](/%e6%96%87%e7%ab%a0/%e6%b7%b1%e5%85%a5%e7%90%86%e8%a7%a3%20MySQL%20%e5%ba%95%e5%b1%82%e5%ae%9e%e7%8e%b0.md)
* [漫画讲解 git rebase VS git merge.md](/%e6%96%87%e7%ab%a0/%e6%bc%ab%e7%94%bb%e8%ae%b2%e8%a7%a3%20git%20rebase%20VS%20git%20merge.md)
* [生成浏览器唯一稳定 ID 的探索.md](/%e6%96%87%e7%ab%a0/%e7%94%9f%e6%88%90%e6%b5%8f%e8%a7%88%e5%99%a8%e5%94%af%e4%b8%80%e7%a8%b3%e5%ae%9a%20ID%20%e7%9a%84%e6%8e%a2%e7%b4%a2.md)
* [缓存 如何保证缓存与数据库的双写一致性？.md](/%e6%96%87%e7%ab%a0/%e7%bc%93%e5%ad%98%20%e5%a6%82%e4%bd%95%e4%bf%9d%e8%af%81%e7%bc%93%e5%ad%98%e4%b8%8e%e6%95%b0%e6%8d%ae%e5%ba%93%e7%9a%84%e5%8f%8c%e5%86%99%e4%b8%80%e8%87%b4%e6%80%a7%ef%bc%9f.md)
* [网易严选怎么做全链路监控的？.md](/%e6%96%87%e7%ab%a0/%e7%bd%91%e6%98%93%e4%b8%a5%e9%80%89%e6%80%8e%e4%b9%88%e5%81%9a%e5%85%a8%e9%93%be%e8%b7%af%e7%9b%91%e6%8e%a7%e7%9a%84%ef%bc%9f.md)
* [美团万亿级 KV 存储架构与实践.md](/%e6%96%87%e7%ab%a0/%e7%be%8e%e5%9b%a2%e4%b8%87%e4%ba%bf%e7%ba%a7%20KV%20%e5%ad%98%e5%82%a8%e6%9e%b6%e6%9e%84%e4%b8%8e%e5%ae%9e%e8%b7%b5.md)
* [美团点评Kubernetes集群管理实践.md](/%e6%96%87%e7%ab%a0/%e7%be%8e%e5%9b%a2%e7%82%b9%e8%af%84Kubernetes%e9%9b%86%e7%be%a4%e7%ae%a1%e7%90%86%e5%ae%9e%e8%b7%b5.md)
* [美团百亿规模API网关服务Shepherd的设计与实现.md](/%e6%96%87%e7%ab%a0/%e7%be%8e%e5%9b%a2%e7%99%be%e4%ba%bf%e8%a7%84%e6%a8%a1API%e7%bd%91%e5%85%b3%e6%9c%8d%e5%8a%a1Shepherd%e7%9a%84%e8%ae%be%e8%ae%a1%e4%b8%8e%e5%ae%9e%e7%8e%b0.md)
* [解读《阿里巴巴 Java 开发手册》背后的思考.md](/%e6%96%87%e7%ab%a0/%e8%a7%a3%e8%af%bb%e3%80%8a%e9%98%bf%e9%87%8c%e5%b7%b4%e5%b7%b4%20Java%20%e5%bc%80%e5%8f%91%e6%89%8b%e5%86%8c%e3%80%8b%e8%83%8c%e5%90%8e%e7%9a%84%e6%80%9d%e8%80%83.md)
* [认识 MySQL 和 Redis 的数据一致性问题.md](/%e6%96%87%e7%ab%a0/%e8%ae%a4%e8%af%86%20MySQL%20%e5%92%8c%20Redis%20%e7%9a%84%e6%95%b0%e6%8d%ae%e4%b8%80%e8%87%b4%e6%80%a7%e9%97%ae%e9%a2%98.md)
* [进阶：Dockerfile 高阶使用指南及镜像优化.md](/%e6%96%87%e7%ab%a0/%e8%bf%9b%e9%98%b6%ef%bc%9aDockerfile%20%e9%ab%98%e9%98%b6%e4%bd%bf%e7%94%a8%e6%8c%87%e5%8d%97%e5%8f%8a%e9%95%9c%e5%83%8f%e4%bc%98%e5%8c%96.md)
* [铁总在用的高性能分布式缓存计算框架 Geode.md](/%e6%96%87%e7%ab%a0/%e9%93%81%e6%80%bb%e5%9c%a8%e7%94%a8%e7%9a%84%e9%ab%98%e6%80%a7%e8%83%bd%e5%88%86%e5%b8%83%e5%bc%8f%e7%bc%93%e5%ad%98%e8%ae%a1%e7%ae%97%e6%a1%86%e6%9e%b6%20Geode.md)
* [阿里云PolarDB及其共享存储PolarFS技术实现分析（上）.md](/%e6%96%87%e7%ab%a0/%e9%98%bf%e9%87%8c%e4%ba%91PolarDB%e5%8f%8a%e5%85%b6%e5%85%b1%e4%ba%ab%e5%ad%98%e5%82%a8PolarFS%e6%8a%80%e6%9c%af%e5%ae%9e%e7%8e%b0%e5%88%86%e6%9e%90%ef%bc%88%e4%b8%8a%ef%bc%89.md)
* [阿里云PolarDB及其共享存储PolarFS技术实现分析（下）.md](/%e6%96%87%e7%ab%a0/%e9%98%bf%e9%87%8c%e4%ba%91PolarDB%e5%8f%8a%e5%85%b6%e5%85%b1%e4%ba%ab%e5%ad%98%e5%82%a8PolarFS%e6%8a%80%e6%9c%af%e5%ae%9e%e7%8e%b0%e5%88%86%e6%9e%90%ef%bc%88%e4%b8%8b%ef%bc%89.md)
* [面试最常被问的 Java 后端题.md](/%e6%96%87%e7%ab%a0/%e9%9d%a2%e8%af%95%e6%9c%80%e5%b8%b8%e8%a2%ab%e9%97%ae%e7%9a%84%20Java%20%e5%90%8e%e7%ab%af%e9%a2%98.md)
* [领域驱动设计在互联网业务开发中的实践.md](/%e6%96%87%e7%ab%a0/%e9%a2%86%e5%9f%9f%e9%a9%b1%e5%8a%a8%e8%ae%be%e8%ae%a1%e5%9c%a8%e4%ba%92%e8%81%94%e7%bd%91%e4%b8%9a%e5%8a%a1%e5%bc%80%e5%8f%91%e4%b8%ad%e7%9a%84%e5%ae%9e%e8%b7%b5.md)
* [领域驱动设计的菱形对称架构.md](/%e6%96%87%e7%ab%a0/%e9%a2%86%e5%9f%9f%e9%a9%b1%e5%8a%a8%e8%ae%be%e8%ae%a1%e7%9a%84%e8%8f%b1%e5%bd%a2%e5%af%b9%e7%a7%b0%e6%9e%b6%e6%9e%84.md)
* [高效构建 Docker 镜像的最佳实践.md](/%e6%96%87%e7%ab%a0/%e9%ab%98%e6%95%88%e6%9e%84%e5%bb%ba%20Docker%20%e9%95%9c%e5%83%8f%e7%9a%84%e6%9c%80%e4%bd%b3%e5%ae%9e%e8%b7%b5.md)
* [捐赠](/assets/捐赠.md)

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# MySQL · 引擎特性 · InnoDB 同步机制

## 前言

现代操作系统以及硬件基本都支持并发程序，而在并发程序设计中，各个进程或者线程需要对公共变量的访问加以制约，此外，不同的进程或者线程需要协同工作以完成特征的任务，这就需要一套完善的同步机制，在Linux内核中有相应的技术实现，包括原子操作，信号量，互斥锁，自旋锁，读写锁等。InnoDB考虑到效率和监控两方面的原因，实现了一套独有的同步机制，提供给其他模块调用。本文的分析默认基于MySQL 5.6，CentOS 6，gcc 4.8，其他版本的信息会另行指出。

## 基础知识

同步机制对于其他数据库模块来说相对独立，但是需要比较多的操作系统以及硬件知识，这里简单介绍一下几个有用的概念，便于读者理解后续概念。
***内存模型 :***主要分为语言级别的内存模型和硬件级别的内存模型。语言级别的内存模型，C/C++属于weak memory model，简单的说就是编译器在进行编译优化的时候，可以对指令进行重排，只需要保证在单线程的环境下，优化前和优化后执行结果一致即可，执行中间过程不保证跟代码的语义顺序一致。所以在多线程的环境下，如果依赖代码中间过程的执行顺序，程序就会出现问题。硬件级别的内存模型，我们常用的cpu，也属于弱内存模型，即cpu在执行指令的时候，为了提升执行效率，也会对某些执行进行乱序执行（按照wiki提供的资料，在x86 64环境下，只会发生读写乱序，即读操作可能会被乱序到写操作之前），如果在编程的时候不做一些措施，同样容易造成错误。
***内存屏障 :***为了解决弱内存模型造成的问题，需要一种能控制指令重排或者乱序执行程序的手段，这种技术就叫做内存屏障，程序员只需要在代码中插入特定的函数，就能控制弱内存模型带来的负面影响，当然，由于影响了乱序和重排这类的优化，对代码的执行效率有一定的影响。具体实现上，内存屏障技术分三种，一种是full memory barrier，即barrier之前的操作不能乱序或重排到barrier之后，同时barrier之后的操作不能乱序或重排到barrier之前，当然这种full barrier对性能影响最大，为了提高效率才有了另外两种：acquire barrier和release barrier，前者只保证barrier后面的操作不能移到之前，后者只保证barrier前面的操作不移到之后。
***互斥锁 :***互斥锁有两层语义，除了大家都知道的排他性（即只允许一个线程同时访问）外，还有一层内存屏障（full memory barrier）的语义，即保证临界区的操作不会被乱序到临界区外。Pthread库里面常用的mutex，conditional variable等操作都自带内存屏障这层语义。此外，使用pthread库，每次调用都需要应用程序从用户态陷入到内核态中查看当前环境，在锁冲突不是很严重的情况下，效率相对比较低。
***自旋锁 :***传统的互斥锁，只要一检测到锁被其他线程所占用了，就立刻放弃cpu时间片，把cpu留给其他线程，这就会产生一次上下文切换。当系统压力大的时候，频繁的上下文切换会导致sys值过高。自旋锁，在检测到锁不可用的时候，首先cpu忙等一小会儿，如果还是发现不可用，再放弃cpu，进行切换。互斥锁消耗cpu sys值，自旋锁消耗cpu usr值。
***递归锁 :***如果在同一个线程中，对同一个互斥锁连续加锁两次，即第一次加锁后，没有释放，继续进行对这个锁进行加锁，那么如果这个互斥锁不是递归锁，将导致死锁。可以把递归锁理解为一种特殊的互斥锁。
***死锁 :***构成死锁有四大条件，其中有一个就是加锁顺序不一致，如果能保证不同类型的锁按照某个特定的顺序加锁，就能大大降低死锁发生的概率，之所以不能完全消除，是因为同一种类型的锁依然可能发生死锁。另外，对同一个锁连续加锁两次，如果是非递归锁，也将导致死锁。

## 原子操作

现代的cpu提供了对单一变量简单操作的原子指令，即这个变量的这些简单操作只需要一条cpu指令即可完成，这样就不用对这个操作加互斥锁了，在锁冲突不激烈的情况下，减少了用户态和内核态的切换，化悲观锁为乐观锁，从而提高了效率。此外，现在外面很火的所谓无锁编程（类似CAS操作），底层就是用了这些原子操作。gcc为了方便程序员使用这些cpu原子操作，提供了一系列\_\_sync开头的函数，这些函数如果包含内存屏障语义，则同时禁止编译器指令重排和cpu乱序执行。
InnoDB针对不同的操作系统以及编译器环境，自己封装了一套原子操作，在头文件os0sync.h中。下面的操作基于Linux x86 64位环境， gcc 4.1以上的版本进行分析。
`os_compare_and_swap_xxx(ptr, old_val, new_val)`类型的操作底层都使用了gcc包装的`__sync_bool_compare_and_swap(ptr, old_val, new_val)`函数，语义为，交换成功则返回true，ptr是交换后的值，old\_val是之前的值，new\_val是交换后的预期值。这个原子操作是个内存屏障（full memory barrier）。
`os_atomic_increment_xxx`类型的操作底层使用了函数`__sync_add_and_fetch`，`os_atomic_decrement_xxx`类型的操作使用了函数`__sync_sub_and_fetch`，分别表示原子递增和原子递减。这个两个原子操作也都是内存屏障（full memory barrier）。
另外一个比较重要的原子操作是`os_atomic_test_and_set_byte(ptr, new_val)`，这个操作使用了`__sync_lock_test_and_set(ptr, new_val)`这个函数，语义为，把ptr设置为new\_val，同时返回旧的值。这个操作提供了原子改变某个变量值的操作，InnoDB锁实现的同步机制中，大量的用了这个操作，因此比较重要。需要注意的是，参看gcc文档，这个操作不是full memory barrier，只是一个acquire barrier，简单的说就是，代码中`__sync_lock_test_and_set`之后操作不能被乱序或者重排到`__sync_lock_test_and_set`之前，但是`__sync_lock_test_and_set`之前的操作可能被重排到其之后。
关于内存屏障的专门指令，MySQL 5.7提供的比较完善。`os_rmb`表示acquire barrier，`os_wmb`表示release barrier。如果在编程时，需要在某个位置准确的读取一个变量的值时，记得在读取之前加上os\_rmb，同理，如果需要在某个位置保证一个变量已经被写了，记得在写之后调用os\_wmb。

## 条件通知机制

条件通知机制在多线程协作中非常有用，一个线程往往需要等待其他线程完成指定工作后，再进行工作，这个时候就需要有线程等待和线程通知机制。`Pthread_cond_XXX`类似的变量和函数来完成等待和通知的工作。InnoDB中，对Pthread库进行了简单的封装，并在此基础上，进一步抽象，提供了一套方便易用的接口函数给调用者使用。

### 系统条件变量

在文件os0sync.cc中，`os_cond_XXX`类似的函数就是InnoDB对Pthread库的封装。常用的几个函数如：
`os_cond_t`是核心的操作对象，其实就是pthread\_cond\_t的一层typedef而已，`os_cond_init`初始化函数，`os_cond_destroy`销毁函数，`os_cond_wait`条件等待，不会超时，`os_cond_wait_timed`条件等待，如果超时则返回，`os_cond_broadcast`唤醒所有等待线程，`os_cond_signal`只唤醒其中一个等待线程，但是在阅读源码的时候发现，似乎没有什么地方调用了`os_cond_signal`。。。
此外，还有一个`os_cond_module_init`函数，用来window下的初始化操作。
在InnoDB下，`os_cond_XXX`模块的函数主要是给InnoDB自己设计的条件变量使用。

### InnoDB条件变量

如果在InnoDB层直接使用系统条件变量的话，主要有四个弊端，首先，弊端1，系统条件变量的使用需要与一个系统互斥锁（详见下一节）相配合使用，使用完还要记得及时释放，使用者会比较麻烦。接着，弊端2，在条件等待的时候，需要在一个循环中等待，使用者还是比较麻烦。最后，弊端3，也是比较重要的，不方便系统监控。
基于以上几点，InnoDB基于系统的条件变量和系统互斥锁自己实现了一套条件通知机制。主要在文件os0sync.cc中实现，相关数据结构以及接口进一层的包装在头文件os0sync.h中。使用方法如下：
InnoDB条件变量核心数据结构为`os_event_t`，类似`pthread_cont_t`。如果需要创建和销毁则分别使用`os_event_create`和`os_event_free`函数。需要等待某个条件变量，先调用`os_event_reset`（原因见下一段），然后使用`os_event_wait`，如果需要超时等待，使用`os_event_wait_time`替换`os_event_wait`即可，`os_event_wait_XXX`这两个函数，解决了弊端1和弊端2，此外，建议把`os_event_reset`返回值传给他们，这样能防止多线程情况下的无限等待（详见下下段）。如果需要发出一个条件通知，使用`os_event_set`。这个几个函数，里面都插入了一些监控信息，方便InnoDB上层管理。怎么样，方便多了吧~

#### 多线程环境下可能发生的问题

首先来说说两个线程下会发生的问题。创建后，正常的使用顺序是这样的，线程A首先`os_event_reset`（步骤1），然后`os_event_wait`（步骤2），接着线程B做完该做的事情后，执行`os_event_set`（步骤3）发送信号，通知线程A停止等待，但是在多线程的环境中，会出现以下两种步骤顺序错乱的情况：乱序A： `步骤1--步骤3--步骤2`，乱序B: `步骤3--步骤1--步骤2`。对于乱序B，属于条件通知在条件等待之前发生，目前InnoDB条件变量的机制下，会发生无限等待，所以上层调用的时候一定要注意，例如在InnoDB在实现互斥锁和读写锁的时候为了防止发生条件通知在条件等待之前发生，在等待之前对lock\_word再次进行了判断，详见InnoDB自旋互斥锁这一节。为了解决乱序A，InnoDB在核心数据结构os\_event中引入布尔型变量is\_set，is\_set这个变量就表示是否已经发生过条件通知，在每次调用条件通知之前，会把这个变量设置为true（在`os_event_reset`时改为false，便于多次通知），在条件等待之前会检查一下这变量，如果这个变量为true，就不再等待了。所以，乱序A也能保证不会发生无限等待。
接着我们来说说大于两个线程下可能会发生的问题。线程A和C是等待线程，等待同一个条件变量，B是通知线程，通知A和C结束等待。考虑一个乱序C：线程A执行`os_event_reset`（步骤1），线程B马上就执行`os_event_set`（步骤2）了，接着线程C执行了`os_event_reset`（步骤3），最后线程A执行`os_event_wait`（步骤4），线程C执行`os_event_wait`（步骤5）。乍一眼看，好像看不出啥问题，但是实际上你会发现A和C线程在无限等待了。原因是，步骤2，把is\_set这个变量设置为false，但是在步骤3，线程C通过reset又把它给重新设回false了。。然后线程A和C在`os_event_wait`中误以为还没有发生过条件通知，就开始无限等待了。为了解决这个问题，InnoDB在核心数据结构os\_event中引入64位整形变量signal\_count，用来记录已经发出条件信号的次数。每次发出一个条件通知，这个变量就递增1。`os_event_reset`的返回值就把当前的signal\_count值取出来。`os_event_wait`如果发现有这个参数的传入，就会判断传入的参数与当前的signal\_count值是否相同，如果不相同，表示这个已经通知过了，就不会进入等待了。举个例子，假设乱序C，一开始的signal\_count为100，步骤1把这个参数传给了步骤4，在步骤4中，`os_event_wait`会发现传入值100与当前的值101（步骤2中递增了1）不同，所以线程A认为信号已经发生过了，就不会再等待了。。。然而。。线程C呢？步骤3返回的值应该是101，传给步骤5后，发生于当前值一样。。继续等待。。。仔细分析可以发现，线程C是属于条件变量通知发生在等待之前（步骤2，步骤3，步骤5），上一段已经说过了，针对这种通知提前发出的，目前InnoDB没有非常好的解法，只能调用者自己控制。
总结一下， InnoDB条件变量能方便InnoDB上层做监控，也简化了条件变量使用的方法，但是调用者上层逻辑必须保证条件通知不能过早的发出，否则就会有无限等待的可能。

## 互斥锁

互斥锁保证一段程序同时只能一个线程访问，保证临界区得到正确的序列化访问。同条件变量一样，InnoDB对Pthread的mutex简单包装了一下，提供给其他模块用（主要是辅助其他自己实现的数据结构，不用InnoDB自己的互斥锁是为了防止递归引用，详见辅助结构这一节）。但与条件变量不同的是，InnoDB自己实现的一套互斥锁并没有依赖Pthread库，而是依赖上述的原子操作（如果平台不支持原子操作则使用Pthread库，但是这种情况不太会发生，因为gcc在4.1就支持原子操作了）和上述的InnoDB条件变量。

### 系统互斥锁

相比与系统条件变量，系统互斥锁除了包装Pthread库外，还做了一层简单的监控统计，结构名为`os_mutex_t`。在文件os0sync.cc中，`os_mutex_create`创建mutex，并调用`os_fast_mutex_init_func`创建pthread的mutex，值得一提的是，创建pthread mutex的参数是`my_fast_mutexattr`的东西，其在MySQL server层函数`my_thread_global_init`初始化 ，只要pthread库支持，则默认成初始化为PTHREAD\_MUTEX\_ADAPTIVE\_NP和PTHREAD\_MUTEX\_ERRORCHECK。前者表示，当锁释放，之前在等待的锁进行公平的竞争，而不是按照默认的优先级模式。后者表示，如果发生了递归的加锁，即同一个线程对同一个锁连续加锁两次，第二次加锁会报错。另外三个有用的函数为，销毁锁`os_mutex_free`，加锁`os_mutex_enter`，解锁`os_mutex_exit`。
一般来说，InnoDB上层模块不需要直接与系统互斥锁打交道，需要用锁的时候一般用InnoDB自己实现的一套互斥锁。系统互斥锁主要是用来辅助实现一些数据结构，例如最后一节提到的一些辅助结构，由于这些辅助结构可能本身就要提供给InnoDB自旋互斥锁用，为了防止递归引用，就暂时用系统互斥锁来代替。

### InnoDB自旋互斥锁

为什么InnoDB需要实现自己的一套互斥锁，不直接用上述的系统互斥锁呢？这个主要有以下几个原因，首先，系统互斥锁是基于pthread mutex的，Heikki Tuuri（同步模块的作者，也是Innobase的创始人）认为在当时的年代pthread mutex上下文切换造成的cpu开销太大，使用spin lock的方式在多处理器的机器上更加有效，尤其是在锁竞争不是很严重的时候，Heikki Tuuri还总结出，在spin lock大概自旋20微秒的时候在多处理的机器下效率最高。其次，不使用pthread spin lock的原因是，当时在1995年左右的时候，spin lock的类似实现，效率很低，而且当时的spin lock不支持自定义自旋时间，要知道自旋锁在单处理器的机器上没什么卵用。最后，也是为了更加完善的监控需求。总的来说，有历史原因，有监控需求也有自定义自旋时间的需求，然后就有了这一套InnoDB自旋互斥锁。
InnoDB自旋互斥锁的实现主要在文件sync0sync.cc和sync0sync.ic中，头文件sync0sync.h定义了核心数据结构ib\_mutex\_t。使用方法很简单，`mutex_create`创建锁，`mutex_free`释放锁，`mutex_enter`尝试获得锁，如果已经被占用了，则等待。`mutex_exit`释放锁，同时唤醒所有等待的线程，拿到锁的线程开始执行，其余线程继续等待。`mutex_enter_nowait`这个函数类似pthread的trylock，只要已检测到锁不用，就直接返回错误，不进行自旋等待。总体来说，InnoDB自旋互斥锁的用法和语义跟系统互斥锁一模一样，但是底层实现却大相径庭。
在ib\_mutex\_t这个核心数据结构中，最重要的是前面两个变量：event和lock\_word。lock\_word为0表示锁空闲，1表示锁被占用，InnoDB自旋互斥锁使用`__sync_lock_test_and_set`这个函数对lock\_word进行原子操作，加锁的时候，尝试把其设置为1，函数返回值不指示是否成功，指示的是尝试设置之前的值，因此如果返回值是0，表示加锁成功，返回是1表示失败。如果加锁失败，则会自旋一段时间，然后等待在条件变量event（`os_event_wait`）上，当锁占用者释放锁的时候，会使用`os_event_set`来唤醒所有的等待者。简单的来说，byte类型的lock\_word基于平台提供的原子操作来实现互斥访问，而event是InnoDB条件变量类型，用来实现锁释放后唤醒等待线程的操作。
接下来，详细介绍一下，`mutex_enter`和`mutex_exit`的逻辑，InnoDB自旋互斥锁的精华都在这两个函数中。
mutex\_enter的伪代码如下：

```
if (__sync_lock_test_and_set(mutex->lock_word, 1) == 0) {
    get mutex successfully;
    return;
}
loop1:
    i = 0;
loop2:
    /*指示点1*/
    while (mutex->lock_word ! = 0 && i < SPIN_ROUNDS) {
             random spin using ut_delay, spin max time depend on SPIN_WAIT_DELAY;
             i++;
}
if (i == SPIN_ROUNDS) {
    yield_cpu;
}
/*指示点2*/
if (__sync_lock_test_and_set(mutex->lock_word, 1) == 0) {
    get mutex successfully;
    return;
}
if (i < SPIN_ROUNDS) {
     goto loop2
}
/*指示点4*/
get cell from sync array and call os_event_reset(mutex->event);
mutex->waiter =1;
/*指示点3*/
for (i = 0; i < 4; i++) {
    if (__sync_lock_test_and_set(mutex->lock_word, 1) == 0) {
        get mutex successfully;
        free cell;
        return;
    }
}
sync array wait and os_event_wait(mutex->event);
goto loop1;

```

代码还是有点小复杂的。这里分析几点如下：

1. SPIN\_ROUNDS控制了在放弃cpu时间片（yield\_cpu）之前，一共进行多少次忙等，这个参数就是对外可配置的innodb\_sync\_spin\_loops，而SPIN\_WAIT\_DELAY控制了每次忙等的时间，这个参数也就是对外可配置的innodb\_spin\_wait\_delay。这两个参数一起决定了自旋的时间。Heikki Tuuri建议在单处理器的机器上调小spin的时间，在对称多处理器的机器上，可以适当调大。比较有意思的是innodb\_spin\_wait\_delay的单位，这个是100MHZ的奔腾处理器处理1毫秒的时间，默认innodb\_spin\_wait\_delay配置成6，表示最多在100MHZ的奔腾处理器上自旋6毫秒。由于现在cpu都是按照GHZ来计算的，所以按照默认配置自旋时间往往很短。此外，自旋不真是cpu傻傻的在那边100%的跑，在现代的cpu上，给自旋专门提供了一条指令，在笔者的测试环境下，这条指令是pause，查看Intel的文档，其对pause的解释是：不会发生用户态和内核态的切换，cpu在用户态自旋，因此不会发生上下文切换，同时这条指令不会消耗太多的能耗。。。所以那些说spin lock太浪费电的不攻自破了。。。另外，编译器也不会把ut\_delay给优化掉，因为其里面估计修改了一个全局变量。
2. yield\_cpu 操作在笔者的环境中，就是调用了pthread\_yield函数，这个函数把放弃当前cpu的时间片，然后把当前线程放到cpu可执行队列的末尾。
3. 在指示点1后面的循环，没有采用原子操作读取数据，是因为，Heikki Tuuri认为由于原子操作在内存和cpu cache之间会产生过的数据交换，如果只是读本地的cache，可以减少总线的争用。即使本地读到脏的数据，也没关系，因为在跳出循环的指示点2，依然会再一次使用原子操作进行校验。
4. get cell这个操作是从sync array执行的，sync array详见辅助数据结构这一节，简单的说就是提供给监控线程使用的。
5. 注意一下，os\_event\_reset和os\_event\_wait这两个函数的调用位置，另外，有一点必须清楚，就是os\_event\_set（锁持有者释放所后会调用这个函数通知所有等待者）可能在这整段代码执行到任意位置出现，有可能出现在指示点4的位置，这样就构成了条件变量通知在条件变量等待之前，会造成无限等待。为了解决这个问题，才有了指示点3下面的代码，需要重新再次检测一下lock\_word，另外，即使os\_event\_set发生在os\_event\_reset之后，有了这些代码，也能让当前线程提前拿到锁，不用执行后续os\_event\_wait的代码，一定程度上提高了效率。

mutex\_exit的伪代码就简单多了，如下：

```
__sync_lock_test_and_set(mutex->lock_word, 0);

/* A problem: we assume that mutex_reset_lock word                                                                     
        is a memory barrier, that is when we read the waiters                                                                  
        field next, the read must be serialized in memory                                                                      
        after the reset. A speculative processor might                                                                         
        perform the read first, which could leave a waiting                                                                    
        thread hanging indefinitely.                                                                                                                                                                                                                        
Our current solution call every second                                                                                 
        sync_arr_wake_threads_if_sema_free()                                                                                   
        to wake up possible hanging threads if                                                                                 
        they are missed in mutex_signal_object. */ 

if (mutex->waiter != 0) {
     mutex->waiter = 0;
     os_event_set(mutex->event);
}

```

1. waiter是ib\_mutex\_t中的一个变量，用来表示当前是否有线程在等待这个锁。整个代码逻辑很简单，就是先把lock\_word设置为0，然后如果发现有等待者，就把所有等待者给唤醒。facebook的mark callaghan在2014年测试过，相比现在已经比较完善的pthread库，InnoDB自旋互斥锁只在并发量相对较低（小于256线程）和锁等待时间比较短的情况下有优势，在高并发且较长的锁等待时间情况下，退化比较严重，其中一个很重要的原因就是InnoDB自旋互斥锁在锁释放的时候需要唤醒所有等待者。由于os\_event\_ret底层通过pthread\_cond\_boardcast来通知所有的等待者，一种改进是把pthread\_cond\_boardcast改成pthread\_cond\_signal，即只唤醒一个线程，但Inaam Rana Mark测试后发现，如果只唤醒一个线程的话，在高并发的情况下，这个线程可能不会立刻被cpu调度到。。由此看来，似乎唤醒一个特定数量的等待者是一个比较好的选择。
2. 伪代码中的这段注释笔者估计加上去的，大意是由于编译器或者cpu的指令重排乱序执行，mutex->waiter这个变量的读取可能在发生在原子操作之前，从而导致一些无线等待的问题。然后还专门开了一个叫做sync\_arr\_wake\_threads\_if\_sema\_free的函数来做清理。这个函数是在后台线程srv\_error\_monitor\_thread中做的，每隔1秒钟执行一次。在现代的cpu和编译器上，完全可以用内存屏障的技术来防止指令重排和乱序执行，这个函数可以被去掉，官方的意见貌似是，不要这么激进，万一其他地方还需要这个函数呢。。详见BUG #79477。

总体来说，InnoDB自旋互斥锁的底层实现还是比较有意思的，非常适合学习研究。这套锁机制在现在完善的Pthread库和高达4GMHZ的cpu下，已经有点力不从心了，mark callaghan研究发现，在高负载的压力下，使用这套锁机制的InnoDB，大部分cpu时间都给了sys和usr，基本没有空闲，而pthread mutex在相同情况下，却有平均80%的空闲。同时，由于ib\_mutex\_t这个结构体体积比较庞大，当buffer pool比较大的时候，会发现锁占用了很多的内存。最后，从代码风格上来说，有不少代码没有解耦，如果需要把锁模块单独打成一个函数库，比较困难。
基于上述几个缺陷，MySQL 5.7及后续的版本中，对互斥锁进行了大量的重新，包括以下几点(WL#6044)：

1. 使用了C++中的类继承关系，系统互斥锁和InnoDB自己实现的自旋互斥锁都是一个父类的子类。
2. 由于bool pool的锁对性能要求比较高，因此使用静态继承（也就是模板）的方式来减少继承中虚指针造成的开销。
3. 保留旧的InnoDB自旋互斥锁，并实现了一种基于futex的锁。简单的说，futex锁与上述的原子操作类似，能减少用户态和内核态切换的开销，但同时保留类似mutex的使用方法，大大降低了程序编写的难度。

## InnoDB读写锁

与条件变量、互斥锁不同，InnoDB里面没有Pthread库的读写锁的包装，其完全依赖依赖于原子操作和InnoDB的条件变量，甚至都不需要依赖InnoDB的自旋互斥锁。此外，读写锁还实现了写操作的递归锁，即同一个线程可以多次获得写锁，但是同一个线程依然不能同时获得读锁和写锁。InnoDB读写锁的核心数据结构rw\_lock\_t中，并没有等待队列的信息，因此不能保证先到的请求一定会先进入临界区。这与系统互斥量用PTHREAD\_MUTEX\_ADAPTIVE\_NP来初始化有异曲同工之妙。
InnoDB读写锁的核心实现在源文件sync0rw.cc和sync0rw.ic中，核心数据结构rw\_lock\_t定义在sync0rw.h中。使用方法与InnoDB自旋互斥锁很类似，只不过读请求和写请求要调用不同的函数。加读锁调用`rw_lock_s_lock`, 加写锁调用`rw_lock_x_lock`，释放读锁调用`rw_lock_s_unlock`, 释放写锁调用`rw_lock_x_unlock`，创建读写锁调用`rw_lock_create`，释放读写锁调用`rw_lock_free`。函数`rw_lock_x_lock_nowait`和`rw_lock_s_lock_nowait`表示，当加读写锁失败的时候，直接返回，而不是自旋等待。

### 核心机制

rw\_lock\_t中，核心的成员有以下几个：lock\_word, event, waiters, wait\_ex\_event，writer\_thread, recursive。
与InnoDB自旋互斥锁的lock\_word不同，rw\_lock\_t中的lock\_word是int 型，注意不是unsigned的，其取值范围是(-2X\_LOCK\_DECR, X\_LOCK\_DECR]，其中X\_LOCK\_DECR为0x00100000，差不多100多W的一个数。在InnoDB自旋互斥锁互斥锁中，lock\_word的取值范围只有0，1，因为这两个状态就能把互斥锁的所有状态都表示出来了，也就是说，只需要查看一下这个lock\_word就能确定当前的线程是否能获得锁。rw\_lock\_t中的lock\_word也扮演了相同的角色，只需要查看一下当前的lock\_word落在哪个取值范围中，就确定当前线程能否获得锁。至于rw\_lock\_t中的lock\_word是如何做到这一点的，这其实是InnoDB读写锁乃至InnoDB同步机制中最神奇的地方，下文我们会详细分析。
event是一个InnoDB条件变量，当当前的锁已经被一个线程以写锁方式独占时，后续的读锁和写锁都等待在这个event上，当这个线程释放写锁时，等待在这个event上的所有读锁和写锁同时竞争。waiters这变量，与event一起用，当有等待者在等待时，这个变量被设置为1，否则为0，锁被释放的时候，需要通过这个变量来判断有没有等待者从而执行os\_event\_set。
与InnoDB自旋互斥锁不同，InnoDB读写锁还有wait\_ex\_event和recursive两个变量。wait\_ex\_event也是一个InnoDB条件变量，但是它用来等待第一个写锁（因为写请求可能会被先前的读请求堵住），当先前到达的读请求都读完了，就会通过这个event来唤醒这个写锁的请求。
由于InnoDB读写锁实现了写锁的递归，因此需要保存当前写锁被哪个线程占用了，后续可以通过这个值来判断是否是这个线程的写锁请求，如果是则加锁成功，否则失败，需要等待。线程的id就保存在writer\_thread这个变量中。
recursive是个bool变量，用来表示当前的读写锁是否支持递归写模式，在某些情况下，例如需要另外一个线程来释放这个读写锁（insert buffer需要这个功能）的时候，就不要开启递归模式了。

接下来，我们来详细介绍一下lock\_word的变化规则：

1. 当有一个读请求加锁成功时，lock\_word原子递减1。
2. 当有一个写请求加锁成功时，lock\_word原子递减X\_LOCK\_DECR。
3. 如果读写锁支持递归写，那么第一个递归写锁加锁成功时，lock\_word依然原子递减X\_LOCK\_DECR，而后续的递归写锁加锁成功是，lock\_word只是原子递减1。
   在上述的变化规则约束下，lock\_word会形成以下几个区间：
   lock\_word == X\_LOCK\_DECR: 表示锁空闲，即当前没有线程获得了这个锁。
   0 < lock\_word < X\_LOCK\_DECR: 表示当前有X\_LOCK\_DECR - lock\_word个读锁
   lock\_word == 0: 表示当前有一个写锁
   -X\_LOCK\_DECR < lock\_word < 0: 表示当前有-lock\_word个读锁，他们还没完成，同时后面还有一个写锁在等待
   lock\_word <= -X\_LOCK\_DECR: 表示当前处于递归锁模式，同一个线程加了2 - (lock\_word + X\_LOCK\_DECR)次写锁。
   另外，还可以得出以下结论
4. 由于lock\_word的范围被限制（rw\_lock\_validate）在(-2X\_LOCK\_DECR, X\_LOCK\_DECR]中，结合上述规则，可以推断出，一个读写锁最多能加X\_LOCK\_DECR个读锁。在开启递归写锁的模式下，一个线程最多同时加X\_LOCK\_DECR+1个写锁。
5. 在读锁释放之前，lock\_word一定处于(-X\_LOCK\_DECR, 0)U(0, X\_LOCK\_DECR)这个范围内。
6. 在写锁释放之前，lock\_word一定处于(-2\*X\_LOCK\_DECR, -X\_LOCK\_DECR]或者等于0这个范围内。
7. 只有在lock\_word大于0的情况下才可以对它递减。有一个例外，就是同一个线程需要加递归写锁的时候，lock\_word可以在小于0的情况下递减。

接下来，举个读写锁加锁的例子，方便读者理解读写锁底层加锁的原理。假设有读写加锁请求按照以下顺序依次到达：R1->R2->W1->R3->W2->W3->R4，其中W2和W3是属于同一个线程的写加锁请求，其他所有读写请求均来自不同线程。初始化后，lock\_word的值为X\_LOCK\_DECR（十进制值为1048576）。R1读加锁请求首先到，其发现lock\_word大于0，表示可以加读锁，同时lock\_word递减1，结果为1048575，R2读加锁请求接着来到，发现lock\_word依然大于0，继续加读锁并递减lock\_word，最终结果为1048574。注意，如果R1和R2几乎是同时到达，即使时序上是R1先请求，但是并不保证R1首先递减，有可能是R2首先拿到原子操作的执行权限。如果在R1或者R2释放锁之前，写加锁请求W1到来，他发现lock\_word依旧大于0，于是递减X\_LOCK\_DECR，并把自己的线程id记录在writer\_thread这个变量里，再检查lock\_word的值（此时为-2），由于结果小于0，表示前面有未完成的读加锁请求，于是其等待在wait\_ex\_event这个条件变量上。后续的R3, W2, W3, R4请求发现lock\_word小于0，则都等待在条件变量event上，并且设置waiter为1，表示有等待者。假设R1先释放读锁(lock\_word递增1)，R2后释放(lock\_word再次递增1)。R2释放后，由于lock\_word变为0了，其会在wait\_ex\_event上调用os\_event\_set，这样W3就被唤醒了，他可以执行临界区内的代码了。W3执行完后，lock\_word被恢复为X\_LOCK\_DECR，然后其发现waiter为1，表示在其后面有新的读写加锁请求在等待，然后在event上调用os\_event\_set，这样R3, W2, W3, R4同时被唤醒，进行原子操作执行权限争抢(可以简单的理解为谁先得到cpu调度)。假设W2首先抢到了执行权限，其会把lock\_word再次递减为0并自己的线程id记录在writer\_thread这个变量里，当检查lock\_word的时候，发现值为0，表示前面没有读请求了，于是其就进入临界区执行代码了。假设此时，W3得到了cpu的调度，由于lock\_word只有在大于0的情况下才能递减，所以其递减lock\_word失败，但是其通过对比writer\_thread和自己的线程id，发现前面的写锁是自己加的，如果这个时候开启了递归写锁，即recursive值为true，他把lock\_word再次递减X\_LOCK\_DECR（现在lock\_word变为-X\_LOCK\_DECR了），然后进入临界区执行代码。这样就保证了同一个线程多次加写锁也不发生死锁，也就是递归锁的概念。后续的R3和R4发现lock\_word小于等于0，就直接等待在event条件变量上，并设置waiter为1。直到W2和W3都释放写锁，lock\_word又变为X\_LOCK\_DECR，最后一个释放的，检查waiter变量发现非0，就会唤醒event上的所有等待者，于是R3和R4就可以执行了。
读写锁的核心函数函数结构跟InnoDB自旋互斥锁的基本相同，主要的区别就是用rw\_lock\_x\_lock\_low和rw\_lock\_s\_lock\_low替换了**sync\_lock\_test\_and\_set原子操作。rw\_lock\_x\_lock\_low和rw\_lock\_s\_lock\_low就按照上述的lock\_word的变化规则来原子的改变（依然使用了**sync\_lock\_test\_and\_set）lock\_word这个变量。

在MySQL 5.7中，读写锁除了可以加读锁(Share lock)请求和加写锁(exclusive lock)请求外，还可以加share exclusive锁请求，锁兼容性如下：

```
 LOCK COMPATIBILITY MATRIX
    S SX  X
 S  +  +  -
 SX +  -  -
 X  -  -  -

```

按照WL#6363的说法，是为了修复index->lock这个锁的冲突。

## 辅助结构

InnoDB同步机制中，还有很多使用的辅助结构，他们的作用主要是为了监控方便和死锁的预防和检测。这里主要介绍sync array, sync thread level array和srv\_error\_monitor\_thread。
sync array主要的数据结构是sync\_array\_t，可以把他理解为一个数据，数组中的元素为sync\_cell\_t。当一个锁（InnoDB自旋互斥锁或者InnoDB读写锁，下同）需要发生`os_event_wait`等待时，就需要在sync array中申请一个sync\_cell\_t来保存当前的信息，这些信息包括等待锁的指针（便于死锁检测），在哪一个文件以及哪一行发生了等待（也就是mutex\_enter, rw\_lock\_s\_lock或者rw\_lock\_x\_lock被调用的地方，只在debug模式下有效），发生等待的线程（便于死锁检测）以及等待开始的时间（便于统计等待的时间）。当锁释放的时候，就把相关联的sync\_cell\_t重置为空，方便复用。sync\_cell\_t在sync\_array\_t中的个数，是在初始化同步模块时候就指定的，其个数一般为OS\_THREAD\_MAX\_N，而OS\_THREAD\_MAX\_N是在InnoDB初始化的时候被计算，其包括了系统后台开启的所有线程，以及max\_connection指定的个数，还预留了一些。由于一个线程在某一个时刻最多只能发生一个锁等待，所以不用担心sync\_cell\_t不够用。从上面也可以看出，在每个锁进行等待和释放的时候，都需要对sync array操作，因此在高并发的情况下，单一的sync array可能成为瓶颈，在MySQL 5.6中，引入了多sync array, 个数可以通过innodb\_sync\_array\_size进行控制，这个值默认为1，在高并发的情况下，建议调高。
InnoDB作为一个成熟的存储引擎，包含了完善的死锁预防机制和死锁检测机制。在每次需要锁等待时，即调用`os_event_wait`之前，需要启动死锁检测机制来保证不会出现死锁，从而造成无限等待。在每次加锁成功（lock\_word递减后，函数返回之前）时，都会启动死锁预防机制，降低死锁出现的概率。当然，由于死锁预防机制和死锁检测机制需要扫描比较多的数据，算法上也有递归操作，所以只在debug模式下开启。
死锁检测机制主要依赖sync array中保存的信息以及死锁检测算法来实现。死锁检测机制通过sync\_cell\_t保存的等待锁指针和发生等待的线程以及教科书上的有向图环路检测算法来实现，具体实现在`sync_array_deadlock_step`和`sync_array_detect_deadlock`中实现，仔细研究后发现个小问题，由于`sync_array_find_thread`函数仅仅在当前的sync array中遍历，当有多个sync array时（innodb\_sync\_array\_size > 1）,如果死锁发生在不同的sync array上，现有的死锁检测算法将无法发现这个死锁。
死锁预防机制是由sync thread level array和全局锁优先级共同保证的。InnoDB为了降低死锁发生的概率，上层的每种类型的锁都有一个优先级。例如回滚段锁的优先级就比文件系统page页的优先级高，虽然两者底层都是InnoDB互斥锁或者InnoDB读写锁。有了这个优先级，InnoDB规定，每个锁创建是必须制定一个优先级，同一个线程的加锁顺序必须从优先级高到低，即如果一个线程目前已经加了一个低优先级的锁A，在释放锁A之前，不能再请求优先级比锁A高(或者相同)的锁。形成死锁需要四个必要条件，其中一个就是不同的加锁顺序，InnoDB通过锁优先级来降低死锁发生的概率，但是不能完全消除。原因是可以把锁设置为SYNC\_NO\_ORDER\_CHECK这个优先级，这是最高的优先级，表示不进行死锁预防检查，如果上层的程序员把自己创建的锁都设置为这个优先级，那么InnoDB提供的这套机制将完全失效，所以要养成给锁设定优先级的好习惯。sync thread level array是一个数组，每个线程单独一个，在同步模块初始化时分配了OS\_THREAD\_MAX\_N个，所以不用担心不够用。这个数组中记录了某个线程当前锁拥有的所有锁，当新加了一个锁B时，需要扫描一遍这个数组，从而确定目前线程所持有的锁的优先级都比锁B高。
最后，我们来讲讲srv\_error\_monitor\_thread这个线程。这是一个后台线程，在InnoDB启动的时候启动，每隔1秒钟执行一下指定的操作。跟同步模块相关的操作有两点，去除无限等待的锁和报告长时间等待的异常锁。
去除无线等待的锁，如上文所属，就是sync\_arr\_wake\_threads\_if\_sema\_free这个函数。这个函数通过遍历sync array，如果发现锁已经可用(`sync_arr_cell_can_wake_up`)，但是依然有等待者，则直接调用`os_event_set`把他们唤醒。这个函数是为了解决由于cpu乱序执行或者编译器指令重排导致锁无限等待的问题，但是可以通过内存屏障技术来避免，所以可以去掉。
报告长时间等待的异常锁，通过sync\_cell\_t里面记录的锁开始等待时间，我们可以很方便的统计锁等待发生的时间。在目前的实现中，当锁等待超过240秒的时候，就会在错误日志中看到信息。如果同一个锁被检测到等到超过600秒且连续10次被检测到，则InnoDB会通过assert来自杀。。。相信当做运维DBA的同学一定看到过如下的报错：

```
InnoDB: Warning: a long semaphore wait:
--Thread 139774244570880 has waited at log0read.h line 765 for 241.00 seconds the semaphore:
Mutex at 0x30c75ca0 created file log0read.h line 522, lock var 1 
Last time reserved in file /home/yuhui.wyh/mysql/storage/innobase/include/log0read.h line 765, waiters flag 1
InnoDB: ###### Starts InnoDB Monitor for 30 secs to print diagnostic info:
InnoDB: Pending preads 0, pwrites 0

```

一般出现这种错误都是pread或者pwrite长时间不返回，导致锁超时。至于pread或者pwrite长时间不返回的root cause常常是有很多的读写请求在极短的时间内到达导致磁盘扛不住或者磁盘已经坏了。。。

## 总结

本文详细介绍了原子操作，条件变量，互斥锁以及读写锁在InnoDB引擎中的实现。原子操作由于其能减少不必要的用户态和内核态的切换以及更精简的cpu指令被广泛的应用到InnoDB自旋互斥锁和InnoDB读写锁中。InnoDB条件变量使用更加方便，但是一定要注意条件通知必须在条件等待之后，否则会有无限等待发生。InnoDB自旋互斥锁加锁和解锁过程虽然复杂但是都是必须的操作。InnoDB读写锁神奇的lock\_word控制方法给我们留下了深刻影响。正因为InnoDB底层同步机制的稳定、高效，MySQL在我们的服务器上才能运行的如此稳定。

---

© 2019 - 2023 [Liangliang Lee](/cdn-cgi/l/email-protection#81edededb8b5b0b0b1b6c1e6ece0e8edafe2eeec).
Powered by [gin](https://github.com/gin-gonic/gin) and [hexo-theme-book](https://github.com/kaiiiz/hexo-theme-book).