# MySQL 主从复制 半同步复制 

Source: https://learn.lianglianglee.com/文章/MySQL 主从复制 半同步复制.md

MySQL 主从复制 半同步复制 



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

# MySQL 主从复制 半同步复制

# 1.半同步复制

半同步复制官方手册：<https://dev.mysql.com/doc/refman/5.7/en/replication-semisync.html>

默认情况下，MySQL的复制是异步的，master将新生成的binlog发送给各slave后，无需等待slave的ack回复(slave将接收到的binlog写进relay log后才会回复ack)，直接就认为这次DDL/DML成功了。

半同步复制(semi-synchronous replication)是指master在将新生成的binlog发送给各slave时，只需等待一个(默认)slave返回的ack信息就返回成功。

![img](assets/733013-20180524205148967-868029789-1623083552625.png)

MySQL 5.7对半同步复制作了大改进，新增了一个master线程。在MySQL 5.7以前，master上的binlog dump线程负责两件事：dump日志给slave的io\_thread；接收来自slave的ack消息。它们是串行方式工作的。在MySQL 5.7中，新增了一个专门负责接受ack消息的线程ack collector thread。这样master上有两个线程独立工作，可以同时发送binlog到slave和接收slave的ack。

还新增了几个变量，其中最重要的是 *rpl\_semi\_sync\_master\_wait\_point* ，它使得MySQL半同步复制有两种工作模型。解释如下。

# 2.半同步复制的两种类型

从MySQL 5.7.2开始，MySQL支持两种类型的半同步复制。这两种类型由变量 *rpl\_semi\_sync\_master\_wait\_point* (MySQL 5.7.2之前没有该变量)控制，它有两种值：AFTER\_SYNC和AFTER\_COMMIT。在MySQL 5.7.2之后，默认值为AFTER\_SYNC，在此版本之前，等价的类型为AFTER\_COMMIT。

这个变量控制的是master何时提交、何时接收ack以及何时回复成功信息给客户端的时间点。

1. `AFTER_SYNC`模式：master将新的事务写进binlog(buffer)，然后发送给slave，再sync到自己的binlog file(disk)。之后才允许接收slave的ack回复，接收到ack之后才会提交事务，并返回成功信息给客户端。
2. `AFTER_COMMIT`模式：master将新的事务写进binlog(buffer)，然后发送给slave，再sync到自己的binlog file(disk)，然后直接提交事务。之后才允许接收slave的ack回复，然后再返回成功信息给客户端。

画图理解就很清晰。(前提：已经设置了`sync_binlog=1`，否则binlog刷盘时间由操作系统决定)

![img](assets/733013-20180610220640867-571552886.png)

![img](assets/733013-20180610220716676-859240378.png)

再来分析下这两种模式的优缺点。

* AFTER\_SYNC
  + 对于所有客户端来说，它们看到的数据是一样的，因为它们看到的数据都是在接收到slave的ack后提交后的数据。
  + 这种模式下，如果master突然故障，不会丢失数据，因为所有成功的事务都已经写进slave的relay log中了，slave的数据是最新的。
* AFTER\_COMMIT
  + 不同客户端看到的数据可能是不一样的。对于发起事务请求的那个客户端，它只有在master提交事务且收到slave的ack后才能看到提交的数据。但对于那些非本次事务的请求客户端，它们在master提交后就能看到提交后的数据，这时候master可能还没收到slave的ack。
  + 如果master收到ack回复前，slave和master都故障了，那么将丢失这个事务中的数据。

在MySQL 5.7.2之前，等价的模式是 *AFTER\_COMMIT* ，在此版本之后，默认的模式为 *AFTER\_SYNC* ，该模式能最大程度地保证数据安全性，且性能上并不比 *AFTER\_COMMIT* 差。

# 3.半同步复制插件介绍

MySQL的半同步是通过加载google为MySQL提供的半同步插件 *semisync\_master.so* 和 *semisync\_slave.so* 来实现的。其中前者是master上需要安装的插件，后者是slave上需要安装的插件。

MySQL的插件位置默认存放在`$basedir/lib/plugin`目录下。例如，yum安装的mysql-server，插件目录为/usr/lib64/mysql/plugin。

```
[root@xuexi ~]# find / -type f -name "semisync*" 
/usr/lib64/mysql/plugin/debug/semisync_master.so
/usr/lib64/mysql/plugin/debug/semisync_slave.so
/usr/lib64/mysql/plugin/semisync_master.so
/usr/lib64/mysql/plugin/semisync_slave.so

```

因为要加载插件，所以应该保证需要加载插件的MySQL的全局变量 *have\_dynamic\_loading* 已经设置为YES(默认值就是YES)，否则无法动态加载插件。

```
mysql> select @@global.have_dynamic_loading;
+-------------------------------+
| @@global.have_dynamic_loading |
+-------------------------------+
| YES                           |
+-------------------------------+

```

## 3.1 MySQL中安装插件的方式

安装插件有两种方式：1.在mysql环境中使用`INSTALL PLUGIN`语句临时安装；2.在配置文件中配置永久生效。

INSTALL安装插件的语法为：

```
Syntax:
INSTALL PLUGIN plugin_name SONAME 'shared_library_name'
UNINSTALL PLUGIN plugin_name

```

例如，使用INSTALL语句在master上安装 *semisync\_master.so* 插件。

```
mysql> install plugin rpl_semi_sync_master soname 'semisync_master.so';

```

配置文件中加载插件的方式为：

```
[mysqld]
plugin-load='plugin_name=shared_library_name'

```

例如，配置文件中加载`semisync_master.so`插件。

```
[mysqld]
plugin-load="rpl_semi_sync_master=sermisync_master.so"

```

如果需要加载多个插件，则插件之间使用分号分隔。例如，在本节的slave1既是slave，又是master，需要同时安装两个半同步插件。

```
[mysqld]
plugin-load="rpl_semi_sync_master=semisync_master.so;rpl_sync_slave=semisync_slave.so"

```

安装插件后，应该使用`show plugins`来查看插件是否真的激活。

```
mysql> show plugins;
+----------------------+--------+-------------+--------------------+---------+
| Name                 | Status | Type        | Library            | License |
+----------------------+--------+-------------+--------------------+---------+
......
| rpl_semi_sync_master | ACTIVE | REPLICATION | semisync_master.so | GPL     |
+----------------------+--------+-------------+--------------------+---------+

```

或者查看`information_schema.plugins`表获取更详细的信息。

```
mysql> select * from information_schema.plugins where plugin_name like "%semi%"\G
*************************** 1. row ***************************
           PLUGIN_NAME: rpl_semi_sync_master
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: REPLICATION
   PLUGIN_TYPE_VERSION: 4.0
        PLUGIN_LIBRARY: semisync_master.so
PLUGIN_LIBRARY_VERSION: 1.7
         PLUGIN_AUTHOR: He Zhenxing
    PLUGIN_DESCRIPTION: Semi-synchronous replication master
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: ON
1 row in set (0.00 sec)

```

插件装载完成后，半同步功能还未开启，需要手动设置它们启动，或者写入配置文件永久生效。

```
# 开启master的半同步
mysql> set @@global.rpl_semi_sync_master_enabled=1;

# 开启slave半同步
mysql> set @@globale.rpl_semi_sync_slave_enabled=1;

```

或者配合插件加载选项一起写进配置文件永久开启半同步功能。

```
[mysqld]
rpl_semi_sync_master_enabled=1

[mysqld]
rpl_semi_sync_slave_enabled=1

```

## 3.2 半同步插件相关的变量

安装了 *semisync\_master.so* 和 *semisync\_slave.so* 后，这两个插件分别提供了几个变量。

```
mysql> show global variables like "%semi%";
+-------------------------------------------+------------+
| Variable_name                             | Value      |
+-------------------------------------------+------------+
| rpl_semi_sync_master_enabled              | OFF        |
| rpl_semi_sync_master_timeout              | 10000      |
| rpl_semi_sync_master_trace_level          | 32         |
| rpl_semi_sync_master_wait_for_slave_count | 1          |
| rpl_semi_sync_master_wait_no_slave        | ON         |
| rpl_semi_sync_master_wait_point           | AFTER_SYNC |
| rpl_semi_sync_slave_enabled               | OFF        |
| rpl_semi_sync_slave_trace_level           | 32         |
+-------------------------------------------+------------+

```

下面还多给了两个和半同步相关的状态变量的解释，可以通过`show status like %semi%;`查看它们。

1. master相关的变量：

   * ①.`Rpl_semi_sync_master_clients`：(状态变量)master所拥有的半同步复制slave的主机数量。
   * ②.`Rpl_semi_sync_master_status` ：(状态变量)master当前是否以半同步复制状态工作(ON)，OFF表示降级为了异步复制。
   * ③.`rpl_semi_sync_master_enabled`：master上是否启用了半同步复制。
   * ④.`rpl_semi_sync_master_timeout`：等待slave的ack回复的超时时间，默认为10秒。
   * ⑤.`rpl_semi_sync_master_trace_level`：半同步复制时master的调试级别。
   * ⑥.`rpl_semi_sync_master_wait_for_slave_count`：master在超时时间内需要收到多少个ack回复才认为此次DML成功，否则就降级为异步复制。该变量在MySQL5.7.3才提供，在此之前的版本都默认为收到1个ack则确认成功，且不可更改。MySQL 5.7.3之后该变量的默认值也是1。
   * ⑦.`rpl_semi_sync_master_wait_no_slave`：值为ON(默认)或者OFF。ON表示master在超时时间内如果未收到指定数量的ack消息，则会一直等待下去直到收满ack，即一直采用半同步复制方式，不会降级；OFF表示如果在超时时间内未收到指定数量的ack，则超时时间一过立即降级为异步复制。

   更官方的解释是：当设置为ON时，即使状态变量Rpl\_semi\_sync\_master\_clients中的值小于rpl\_semi\_sync\_master\_wait\_for\_slave\_count，Rpl\_semi\_sync\_master\_status依旧为ON；当设置为OFF时，如果clients的值小于count的值，则Rpl\_semi\_sync\_master\_status立即变为OFF。通俗地讲，就是在超时时间内，如果slave宕机的数量超过了应该要收到的ack数量，master是否降级为异步复制。

   该变量在MySQL 5.7.3之前似乎没有效果，因为默认设置为ON时，超时时间内收不到任何ack时仍然会降级为异步复制。

   * ⑧.`rpl_semi_sync_master_wait_point`：控制master上commit、接收ack、返回消息给客户端的时间点。值为 *AFTER\_SYNC* 和 *AFTER\_COMMIT* ，该选项是MySQL5.7.2后引入的，默认值为 *AFTER\_SYNC* ，在此版本之前，等价于使用了 *AFTER\_COMMIT* 模式。关于这两种模式，见前文对两种半同步类型的分析。
2. slave相关的变量：

   * ①.`rpl_semi_sync_slave_enabled`：slave是否开启半同步复制。
   * ②.`rpl_semi_sync_slave_trace_level`：slave的调试级别。

# 4.配置半同步复制

需要注意的是，”半同步”是同步/异步类型的一种情况，**既可以实现半同步的传统复制，也可以实现半同步的GTID复制**。其实半同步复制是基于异步复制的，它是在异步复制的基础上通过加载半同步插件的形式来实现半同步性的。

此处以全新的环境进行配置，方便各位道友”依葫芦画瓢”。

本文实现如下拓扑图所示的半同步传统复制。如果要实现半同步GTID复制，也只是在gtid复制的基础上改改配置文件而已。

![img](assets/733013-20180611095458324-817021379.png)

具体环境：

| 称呼 | 主机IP | MySQL版本 | OS | 角色(master/slave) | 数据库状态 |
| --- | --- | --- | --- | --- | --- |
| master | 192.168.100.21 | MySQL 5.7.22 | CentOS 7.2 | master | 全新实例 |
| salve1 | 192.168.100.22 | MySQL 5.7.22 | CentOS 7.2 | semi\_slave for master semi\_master for other slaves | 全新实例 |
| slave2 | 192.168.100.23 | MySQL 5.7.22 | CentOS 7.2 | semi\_slave for slave1 | 全新实例 |
| slave3 | 192.168.100.24 | MySQL 5.7.22 | CentOS 7.2 | semi\_slave for slave1 | 全新实例 |

因为都是全新的实例环境，所以无需考虑基准数据和binlog坐标的问题。如果开始测试前，已经在master上做了一些操作，或者创建了一些新数据，那么请将master上的数据恢复到各slave上，并获取master binlog的坐标，具体操作方法可参见前文：将slave恢复到master指定的坐标。

## 4.1 半同步复制的配置文件

首先提供各MySQL Server的配置文件。

以下是master的配置文件。

```
[mysqld]
datadir=/data
socket=/data/mysql.sock
log-error=/data/error.log
pid-file=/data/mysqld.pid
log-bin=/data/master-bin
sync-binlog=1
server-id=100
plugin-load="rpl_semi_sync_master=semisync_master.so"
rpl_semi_sync_master_enabled=1

```

以下是slave1的配置文件，注意slave1同时还充当着slave2和slave3的master的角色。

```
[mysqld]
datadir=/data
socket=/data/mysql.sock
log-error=/data/error.log
pid-file=/data/mysqld.pid
log-bin=/data/master-bin
sync-binlog=1
server-id=110
relay-log=/data/slave-bin
log-slave-updates
plugin-load="rpl_semi_sync_master=semisync_master.so;rpl_semi_sync_slave=semisync_slave.so"
rpl_semi_sync_slave_enabled=1
rpl_semi_sync_master_enabled=1

```

以下是slave2和slave3的配置文件，它们配置文件除了\*server-id\*外都一致。

```
[mysqld]
datadir=/data
socket=/data/mysql.sock
log-error=/data/error.log
pid-file=/data/mysqld.pid
server-id=120      # slave3的server-id=130
relay-log=/data/slave-bin
plugin-load="rpl_semi_sync_slave=semisync_slave.so"
rpl_semi_sync_slave_enabled=1
read-only=on

```

## 4.2 启动复制线程

现在master上创建一个专门用于复制的用户。

```
mysql> create user repl@'192.168.100.%' identified by 'P@ssword1!';
mysql> grant replication slave on *.* to repl@'192.168.100.%';

```

因为master和所有的slave都是全新的实例，所以slave上指定的binlog坐标可以从任意位置开始。不过刚才master上创建了一个用户，也会写binlog，所以建议还是从master的第一个binlog的position=4开始。

以下是slave1上的`change master to`参数：

```
mysql> change master to 
            master_host='192.168.100.21',
            master_port=3306,
            master_user='repl',
            master_password='P@ssword1!',
            master_log_file='master-bin.000001',
            master_log_pos=4;

```

以下是slave2和slave3的`change master to`参数：

```
mysql> change master to 
            master_host='192.168.100.22',
            master_port=3306,
            master_user='repl',
            master_password='P@ssword1!',
            master_log_file='master-bin.000001',
            master_log_pos=4;

```

启动各slave上的两个SQL线程。

```
mysql> start slave;

```

一切就绪后，剩下的事情就是测试。在master上对数据做一番修改，然后查看是否会同步到slave1、slave2、slave3上。

# 5.半同步复制的状态信息

首先是semisync相关的可修改变量，这几个变量在[前文](https://www.cnblogs.com/f-ck-need-u/p/9166452.html#blog3.2)已经解释过了。

例如以下是开启了半同步复制后的master上的semisync相关变量。

```
mysql> show global variables like "%semi%";
+-------------------------------------------+------------+
| Variable_name                             | Value      |
+-------------------------------------------+------------+
| rpl_semi_sync_master_enabled              | ON         |
| rpl_semi_sync_master_timeout              | 10000      |
| rpl_semi_sync_master_trace_level          | 32         |
| rpl_semi_sync_master_wait_for_slave_count | 1          |
| rpl_semi_sync_master_wait_no_slave        | ON         |
| rpl_semi_sync_master_wait_point           | AFTER_SYNC |
+-------------------------------------------+------------+

```

关于半同步复制，还有几个状态变量很重要。

例如，以下是master上关于semi\_sync的状态变量信息。

```
mysql> show status like "%semi%";
+--------------------------------------------+-------+
| Variable_name                              | Value |
+--------------------------------------------+-------+
| Rpl_semi_sync_master_clients               | 1     |  # 注意行1
| Rpl_semi_sync_master_net_avg_wait_time     | 0     |
| Rpl_semi_sync_master_net_wait_time         | 0     |
| Rpl_semi_sync_master_net_waits             | 5     |
| Rpl_semi_sync_master_no_times              | 1     |
| Rpl_semi_sync_master_no_tx                 | 1     |
| Rpl_semi_sync_master_status                | ON    |  # 注意行2
| Rpl_semi_sync_master_timefunc_failures     | 0     |
| Rpl_semi_sync_master_tx_avg_wait_time      | 384   |
| Rpl_semi_sync_master_tx_wait_time          | 1537  |
| Rpl_semi_sync_master_tx_waits              | 4     |
| Rpl_semi_sync_master_wait_pos_backtraverse | 0     |
| Rpl_semi_sync_master_wait_sessions         | 0     |
| Rpl_semi_sync_master_yes_tx                | 4     |
+--------------------------------------------+-------+

```

除了上面标注”注意行”的变量，其他都无需关注，而且其中有一些是废弃了的状态变量。

`Rpl_semi_sync_master_clients`是该master所连接到的slave数量。

`Rpl_semi_sync_master_status`是该master的半同步复制功能是否开启。在有些时候半同步复制会降级为异步复制，这时它的值为OFF。

以下是slave1上关于semi\_sync的状态变量信息。

```
mysql>  show status like "%semi%";
+--------------------------------------------+-------+
| Variable_name                              | Value |
+--------------------------------------------+-------+
| Rpl_semi_sync_master_clients               | 2     |  # 注意行1
| Rpl_semi_sync_master_net_avg_wait_time     | 0     |
| Rpl_semi_sync_master_net_wait_time         | 0     |
| Rpl_semi_sync_master_net_waits             | 8     |
| Rpl_semi_sync_master_no_times              | 2     |
| Rpl_semi_sync_master_no_tx                 | 4     |
| Rpl_semi_sync_master_status                | ON    |  # 注意行2
| Rpl_semi_sync_master_timefunc_failures     | 0     |
| Rpl_semi_sync_master_tx_avg_wait_time      | 399   |
| Rpl_semi_sync_master_tx_wait_time          | 1199  |
| Rpl_semi_sync_master_tx_waits              | 3     |
| Rpl_semi_sync_master_wait_pos_backtraverse | 0     |
| Rpl_semi_sync_master_wait_sessions         | 0     |
| Rpl_semi_sync_master_yes_tx                | 3     |
| Rpl_semi_sync_slave_status                 | ON    |  # 注意行3
+--------------------------------------------+-------+

```

此外，从MySQL的错误日志、`show slave status`也能获取到一些半同步复制的状态信息。下一节测试半同步复制再说明。

# 6.测试半同步复制(等待、降级问题)

前面已经搭建好了下面的半同步复制结构。

```
                                     |------> slave2
                master ---> slave1 ---
                                     |------> slave3

```

下面来测试半同步复制降级为异步复制的问题，借此来观察一些semisync的状态变化。

首先，只停掉slave2或slave3中其中一个io线程的话，slave1是不会出现降级的，因为默认的半同步复制只需等待一个ack回复即可返回成功信息。

如果同时停掉slave2和slave3的io线程，当master更新数据后，slave1在10秒(默认)之后将降级为异步复制。如下：

在slave2和slave3上执行：

```
mysql> stop slave io_thread;

```

在master上执行：

```
create database test1;
create table test1.t(id int);
insert into test1.t values(33);

```

在slave1上查看(在上面的步骤之后的10秒内查看)：

```
mysql> show status like "%semi%";
+--------------------------------------------+-------+
| Variable_name                              | Value |
+--------------------------------------------+-------+
| Rpl_semi_sync_master_clients               | 0     |  # clients=0
| Rpl_semi_sync_master_net_avg_wait_time     | 0     |
| Rpl_semi_sync_master_net_wait_time         | 0     |
| Rpl_semi_sync_master_net_waits             | 8     |
| Rpl_semi_sync_master_no_times              | 2     |
| Rpl_semi_sync_master_no_tx                 | 4     |
| Rpl_semi_sync_master_status                | ON    |  # status=ON
| Rpl_semi_sync_master_timefunc_failures     | 0     |
| Rpl_semi_sync_master_tx_avg_wait_time      | 399   |
| Rpl_semi_sync_master_tx_wait_time          | 1199  |
| Rpl_semi_sync_master_tx_waits              | 3     |
| Rpl_semi_sync_master_wait_pos_backtraverse | 0     |
| Rpl_semi_sync_master_wait_sessions         | 1     |
| Rpl_semi_sync_master_yes_tx                | 3     |
| Rpl_semi_sync_slave_status                 | ON    |
+--------------------------------------------+-------+

```

可以看到在这一小段时间内，slave1还是半同步复制。此时用`show slave status`查看slave1。

```
# slave1上执行
mysql> show slave status \G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.100.21
                  Master_User: repl
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: master-bin.000004
          Read_Master_Log_Pos: 1762
               Relay_Log_File: slave-bin.000005
                Relay_Log_Pos: 1729
        Relay_Master_Log_File: master-bin.000004
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
................................................
      Slave_SQL_Running_State: Waiting for semi-sync ACK from slave
................................................

```

此时slave的**SQL线程**状态是`Waiting for semi-sync ACK from slave`。

但10秒之后再查看。

```
mysql> show status like "%semi%";
+--------------------------------------------+-------+
| Variable_name                              | Value |
+--------------------------------------------+-------+
| Rpl_semi_sync_master_clients               | 0     |
| Rpl_semi_sync_master_net_avg_wait_time     | 0     |
| Rpl_semi_sync_master_net_wait_time         | 0     |
| Rpl_semi_sync_master_net_waits             | 8     |
| Rpl_semi_sync_master_no_times              | 3     |
| Rpl_semi_sync_master_no_tx                 | 5     |
| Rpl_semi_sync_master_status                | OFF   |
| Rpl_semi_sync_master_timefunc_failures     | 0     |
| Rpl_semi_sync_master_tx_avg_wait_time      | 399   |
| Rpl_semi_sync_master_tx_wait_time          | 1199  |
| Rpl_semi_sync_master_tx_waits              | 3     |
| Rpl_semi_sync_master_wait_pos_backtraverse | 0     |
| Rpl_semi_sync_master_wait_sessions         | 0     |
| Rpl_semi_sync_master_yes_tx                | 3     |
| Rpl_semi_sync_slave_status                 | ON    |
+--------------------------------------------+-------+

```

发现slave1已经关闭半同步功能了，也就是说降级为异步复制了。

此时查看slave1的错误日志。

```
2018-06-11T03:43:21.765384Z 4 [Warning] Timeout waiting for reply of binlog (file: master-bin.000001, pos: 2535), semi-sync up to file master-bin.000001, position 2292.
2018-06-11T03:43:21.765453Z 4 [Note] Semi-sync replication switched OFF.

```

它先记录了当前slave2/slave3中已经同步到slave1的哪个位置。然后将Semi-sync复制切换为OFF状态，即降级为异步复制。

在下次slave2或slave3启动IO线程时，**slave1将自动切换回半同步复制**，并发送那些未被复制的binlog。

---

© 2019 - 2023 [Liangliang Lee](/cdn-cgi/l/email-protection#0f636363363b3e3e3f384f68626e6663216c6062).
Powered by [gin](https://github.com/gin-gonic/gin) and [hexo-theme-book](https://github.com/kaiiiz/hexo-theme-book).