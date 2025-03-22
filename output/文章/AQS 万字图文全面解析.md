# AQS 万字图文全面解析 

Source: https://learn.lianglianglee.com/%e6%96%87%e7%ab%a0/AQS%20%e4%b8%87%e5%ad%97%e5%9b%be%e6%96%87%e5%85%a8%e9%9d%a2%e8%a7%a3%e6%9e%90.md

AQS 万字图文全面解析 



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

# AQS 万字图文全面解析

### 前言

谈到并发，我们不得不说`AQS(AbstractQueuedSynchronizer)`，所谓的`AQS`即是抽象的队列式的同步器，内部定义了很多锁相关的方法，我们熟知的`ReentrantLock`、`ReentrantReadWriteLock`、`CountDownLatch`、`Semaphore`等都是基于`AQS`来实现的。

我们先看下`AQS`相关的`UML`图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDJjNDZiNGRlMQ.jfif)

思维导图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDJjNWQ2OTMzOA.jfif)

### AQS 实现原理

`AQS`中 维护了一个`volatile int state`（代表共享资源）和一个`FIFO`线程等待队列（多线程争用资源被阻塞时会进入此队列）。

这里`volatile`能够保证多线程下的可见性，当`state=1`则代表当前对象锁已经被占有，其他线程来加锁时则会失败，加锁失败的线程会被放入一个`FIFO`的等待队列中，比列会被`UNSAFE.park()`操作挂起，等待其他获取锁的线程释放锁才能够被唤醒。

另外`state`的操作都是通过`CAS`来保证其并发修改的安全性。

具体原理我们可以用一张图来简单概括：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDJjNzdiMjc2NQ.jfif)

`AQS` 中提供了很多关于锁的实现方法，

* getState()：获取锁的标志 state 值
* setState()：设置锁的标志 state 值
* tryAcquire(int)：独占方式获取锁。尝试获取资源，成功则返回 true，失败则返回 false。
* tryRelease(int)：独占方式释放锁。尝试释放资源，成功则返回 true，失败则返回 false。

这里还有一些方法并没有列出来，接下来我们以`ReentrantLock`作为突破点通过源码和画图的形式一步步了解`AQS`内部实现原理。

### 目录结构

文章准备模拟多线程竞争锁、释放锁的场景来进行分析`AQS`源码：

**三个线程(线程一、线程二、线程三)同时来加锁/释放锁**

**目录如下：**

* **线程一**加锁成功时`AQS`内部实现
* **线程二/三**加锁失败时`AQS`中等待队列的数据模型
* **线程一**释放锁及**线程二**获取锁实现原理
* 通过线程场景来讲解**公平锁**具体实现原理
* 通过线程场景来讲解 Condition 中 a`wait()`和`signal()`实现原理

这里会通过画图来分析每个线程加锁、释放锁后`AQS`内部的数据结构和实现原理

### 场景分析

#### 线程一加锁成功

如果同时有**三个线程**并发抢占锁，此时**线程一**抢占锁成功，**线程二**和**线程三**抢占锁失败，具体执行流程如下：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDJjNWQyZWIyYw.jfif)

此时`AQS`内部数据为：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDJjNzc5OTlkNQ.jfif)

**线程二**、**线程三**加锁失败：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDJjOGU1ZTI2OA.jfif)

有图可以看出，等待队列中的节点`Node`是一个双向链表，这里`SIGNAL`是`Node`中`waitStatus`属性，`Node`中还有一个`nextWaiter`属性，这个并未在图中画出来，这个到后面`Condition`会具体讲解的。

具体看下抢占锁代码实现：

```
java.util.concurrent.locks.ReentrantLock .NonfairSync:
static final class NonfairSync extends Sync {

    final void lock() {
        if (compareAndSetState(0, 1))
            setExclusiveOwnerThread(Thread.currentThread());
        else
            acquire(1);
    }

    protected final boolean tryAcquire(int acquires) {
        return nonfairTryAcquire(acquires);
    }
}

```

这里使用的**ReentrantLock 非公平锁**，线程进来直接利用`CAS`尝试抢占锁，如果抢占成功`state`值回被改为 1，且设置对象独占锁线程为当前线程。如下所示：

```
protected final boolean compareAndSetState(int expect, int update) {
    return unsafe.compareAndSwapInt(this, stateOffset, expect, update);
}

protected final void setExclusiveOwnerThread(Thread thread) {
    exclusiveOwnerThread = thread;
}

```

#### 线程二抢占锁失败

我们按照真实场景来分析，**线程一**抢占锁成功后，`state`变为 1，**线程二**通过`CAS`修改`state`变量必然会失败。此时`AQS`中`FIFO`(First In First Out 先进先出)队列中数据如图所示：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDMwYjUyNTZkZQ.jfif)

我们将**线程二**执行的逻辑一步步拆解来看：

`java.util.concurrent.locks.AbstractQueuedSynchronizer.acquire()`:

```
public final void acquire(int arg) {
    if (!tryAcquire(arg) &&
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg))
        selfInterrupt();
}

```

先看看`tryAcquire()`的具体实现： `java.util.concurrent.locks.ReentrantLock .nonfairTryAcquire()`:

```
final boolean nonfairTryAcquire(int acquires) {
    final Thread current = Thread.currentThread();
    int c = getState();
    if (c == 0) {
        if (compareAndSetState(0, acquires)) {
            setExclusiveOwnerThread(current);
            return true;
        }
    }
    else if (current == getExclusiveOwnerThread()) {
        int nextc = c + acquires;
        if (nextc < 0)
            throw new Error("Maximum lock count exceeded");
        setState(nextc);
        return true;
    }
    return false;
}

```

`nonfairTryAcquire()`方法中首先会获取`state`的值，如果不为 0 则说明当前对象的锁已经被其他线程所占有，接着判断占有锁的线程是否为当前线程，如果是则累加`state`值，这就是可重入锁的具体实现，累加`state`值，释放锁的时候也要依次递减`state`值。

如果`state`为 0，则执行`CAS`操作，尝试更新`state`值为 1，如果更新成功则代表当前线程加锁成功。

以**线程二**为例，因为**线程一**已经将`state`修改为 1，所以**线程二**通过`CAS`修改`state`的值不会成功。加锁失败。

**线程二**执行`tryAcquire()`后会返回 false，接着执行`addWaiter(Node.EXCLUSIVE)`逻辑，将自己加入到一个`FIFO`等待队列中，代码实现如下：

`java.util.concurrent.locks.AbstractQueuedSynchronizer.addWaiter()`:

```
private Node addWaiter(Node mode) {    
    Node node = new Node(Thread.currentThread(), mode);
    Node pred = tail;
    if (pred != null) {
        node.prev = pred;
        if (compareAndSetTail(pred, node)) {
            pred.next = node;
            return node;
        }
    }
    enq(node);
    return node;
}

```

这段代码首先会创建一个和当前线程绑定的`Node`节点，`Node`为双向链表。此时等待对内中的`tail`指针为空，直接调用`enq(node)`方法将当前线程加入等待队列尾部：

```
private Node enq(final Node node) {
    for (;;) {
        Node t = tail;
        if (t == null) {
            if (compareAndSetHead(new Node()))
                tail = head;
        } else {
            node.prev = t;
            if (compareAndSetTail(t, node)) {
                t.next = node;
                return t;
            }
        }
    }
}

```

第一遍循环时`tail`指针为空，进入 if 逻辑，使用`CAS`操作设置`head`指针，将`head`指向一个新创建的`Node`节点。此时`AQS`中数据：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDMxZGZmMGI2Zg.jfif)

执行完成之后，`head`、`tail`、`t`都指向第一个`Node`元素。

接着执行第二遍循环，进入`else`逻辑，此时已经有了`head`节点，这里要操作的就是将**线程二**对应的`Node`节点挂到`head`节点后面。此时队列中就有了两个`Node`节点：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDMyMTk0MTdmNQ.jfif)

`addWaiter()`方法执行完后，会返回当前线程创建的节点信息。继续往后执行`acquireQueued(addWaiter(Node.EXCLUSIVE), arg)` 逻辑，此时传入的参数为**线程二**对应的`Node`节点信息：

`java.util.concurrent.locks.AbstractQueuedSynchronizer.acquireQueued()`:

```
final boolean acquireQueued(final Node node, int arg) {
    boolean failed = true;
    try {
        boolean interrupted = false;
        for (;;) {
            final Node p = node.predecessor();
            if (p == head && tryAcquire(arg)) {
                setHead(node);
                p.next = null; // help GC
                failed = false;
                return interrupted;
            }
            if (shouldParkAfterFailedAcquire(p, node) &&
                parkAndChecknIterrupt())
                interrupted = true;
        }
    } finally {
        if (failed)
            cancelAcquire(node);
    }
}

private static boolean shouldParkAfterFailedAcquire(Node pred, Node node) {
    int ws = pred.waitStatus;
    if (ws == Node.SIGNAL)
        return true;
    if (ws > 0) {
        do {
            node.prev = pred = pred.prev;
        } while (pred.waitStatus > 0);
        pred.next = node;
    } else {
        compareAndSetWaitStatus(pred, ws, Node.SIGNAL);
    }
    return false;
}

private final boolean parkAndCheckInterrupt() {
    LockSupport.park(this);
    return Thread.interrupted();
}

```

`acquireQueued()`这个方法会先判断当前传入的`Node`对应的前置节点是否为`head`，如果是则尝试加锁。加锁成功过则将当前节点设置为`head`节点，然后空置之前的`head`节点，方便后续被垃圾回收掉。

如果加锁失败或者`Node`的前置节点不是`head`节点，就会通过`shouldParkAfterFailedAcquire`方法 将`head`节点的`waitStatus`变为了`SIGNAL=-1`，最后执行`parkAndChecknIterrupt`方法，调用`LockSupport.park()`挂起当前线程。

此时`AQS`中的数据如下图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDMyNzYxZDk2MQ.jfif)

此时**线程二**就静静的待在`AQS`的等待队列里面了，等着其他线程释放锁来唤醒它。

#### 线程三抢占锁失败

看完了**线程二**抢占锁失败的分析，那么再来分析**线程三**抢占锁失败就很简单了，先看看`addWaiter(Node mode)`方法：

```
private Node addWaiter(Node mode) {
    Node node = new Node(Thread.currentThread(), mode);
    Node pred = tail;
    if (pred != null) {
        node.prev = pred;
        if (compareAndSetTail(pred, node)) {
            pred.next = node;
            return node;
        }
    }
    enq(node);
    return node;
}

```

此时等待队列的`tail`节点指向**线程二**，进入`if`逻辑后，通过`CAS`指令将`tail`节点重新指向**线程三**。接着**线程三**调用`enq()`方法执行入队操作，和上面**线程二**执行方式是一致的，入队后会修改**线程二**对应的`Node`中的`waitStatus=SIGNAL`。最后**线程三**也会被挂起。此时等待队列的数据如图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDJjOGU1ZTI2OA-1590419214352.jfif)

#### 线程一释放锁

现在来分析下释放锁的过程，首先是**线程一**释放锁，释放锁后会唤醒`head`节点的后置节点，也就是我们现在的**线程二**，具体操作流程如下：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDMzMmRmNmZkNQ.jfif)

执行完后等待队列数据如下：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDM0MzkzYzU4Zg.jfif)

此时**线程二**已经被唤醒，继续尝试获取锁，如果获取锁失败，则会继续被挂起。如果获取锁成功，则`AQS`中数据如图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDM1ZDI0OThhYg.jfif)

接着还是一步步拆解来看，先看看**线程一**释放锁的代码：

```
java.util.concurrent.locks.AbstractQueuedSynchronizer.release()
public final boolean release(int arg) {
    if (tryRelease(arg)) {
        Node h = head;
        if (h != null && h.waitStatus != 0)
            unparkSuccessor(h);
        return true;
    }
    return false;
}

```

这里首先会执行`tryRelease()`方法，这个方法具体实现在`ReentrantLock`中，如果`tryRelease`执行成功，则继续判断`head`节点的`waitStatus`是否为 0，前面我们已经看到过，`head`的`waitStatue`为`SIGNAL(-1)`，这里就会执行`unparkSuccessor()`方法来唤醒`head`的后置节点，也就是我们上面图中**线程二**对应的`Node`节点。

此时看`ReentrantLock.tryRelease()`中的具体实现：

```
protected final boolean tryRelease(int releases) {
    int c = getState() - releases;
    if (Thread.currentThread() != getExclusiveOwnerThread())
        throw new IllegalMonitorStateException();
    boolean free = false;
    if (c == 0) {
        free = true;
        setExclusiveOwnerThread(null);
    }
    setState(c);
    return free;
}

```

执行完`ReentrantLock.tryRelease()`后，`state`被设置成 0，Lock 对象的独占锁被设置为 null。此时看下`AQS`中的数据：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDM2M2U4NzkwMg.jfif)

接着执行`java.util.concurrent.locks.AbstractQueuedSynchronizer.unparkSuccessor()`方法，唤醒`head`的后置节点：

```
private void unparkSuccessor(Node node) {
    int ws = node.waitStatus;
    if (ws < 0)
        compareAndSetWaitStatus(node, ws, 0);
    Node s = node.next;
    if (s == null || s.waitStatus > 0) {
        s = null;
        for (Node t = tail; t != null && t != node; t = t.prev)
            if (t.waitStatus <= 0)
                s = t;
    }
    if (s != null)
        LockSupport.unpark(s.thread);
}

```

这里主要是将`head`节点的`waitStatus`设置为 0。

此时重新将`head`指针指向**线程二**对应的`Node`节点，且使用`LockSupport.unpark`方法来唤醒**线程二**。

被唤醒的**线程二**会接着尝试获取锁，用`CAS`指令修改`state`数据。 执行完成后可以查看`AQS`中数据：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDM0MzkzYzU4Zg-1590419228808.jfif)

此时**线程二**被唤醒，**线程二**接着之前被`park`的地方继续执行，继续执行`acquireQueued()`方法。

#### 线程二唤醒继续加锁

```
final boolean acquireQueued(final Node node, int arg) {
    boolean failed = true;
    try {
        boolean interrupted = false;
        for (;;) {
            final Node p = node.predecessor();
            if (p == head && tryAcquire(arg)) {
                setHead(node);
                p.next = null; // help GC
                failed = false;
                return interrupted;
            }
            if (shouldParkAfterFailedAcquire(p, node) &&
                parkAndCheckInterrupt())
                interrupted = true;
        }
    } finally {
        if (failed)
            cancelAcquire(node);
    }
}

```

此时**线程二**被唤醒，继续执行`for`循环，判断**线程二**的前置节点是否为`head`，如果是则继续使用`tryAcquire()`方法来尝试获取锁，其实就是使用`CAS`操作来修改`state`值，如果修改成功则代表获取锁成功。接着将**线程二**设置为`head`节点，然后空置之前的`head`节点数据，被空置的节点数据等着被**垃圾回收**。

此时线程二获取锁成功，`AQS`中队列数据如下：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDM3ZWI5MzQ5MA.jfif)

等待队列中的数据都等待着被垃圾回收。

#### 线程二释放锁/线程三加锁

当**线程二**释放锁时，会唤醒被挂起的**线程三**，流程和上面大致相同，被唤醒的**线程三**会再次尝试加锁，具体代码可以参考上面内容。具体流程图如下：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDNhMWEyNmU5NA.jfif)

此时`AQS`中队列数据如图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDNhYjVmZDRjNw.jfif)

### 公平锁实现原理

上面所有的加锁场景都是基于**非公平锁**来实现的，**非公平锁**是`ReentrantLock`的默认实现，那我们接着来看一下**公平锁**的实现原理，这里先用一张图来解释**公平锁**和**非公平锁**的区别：

**非公平锁**执行流程：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDNjMjExMjgzOQ.jfif)

这里我们还是用之前的线程模型来举例子，当**线程二**释放锁的时候，唤醒被挂起的**线程三**，**线程三**执行`tryAcquire()`方法使用`CAS`操作来尝试修改`state`值，如果此时又来了一个**线程四**也来执行加锁操作，同样会执行`tryAcquire()`方法。

这种情况就会出现竞争，**线程四**如果获取锁成功，**线程三**仍然需要待在等待队列中被挂起。这就是所谓的**非公平锁**，**线程三**辛辛苦苦排队等到自己获取锁，却眼巴巴的看到**线程四**插队获取到了锁。

**公平锁**执行流程：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDNjMzQ2MmQ2YQ.jfif)

公平锁在加锁的时候，会先判断`AQS`等待队列中是存在节点，如果存在节点则会直接入队等待，具体代码如下.

公平锁在获取锁是也是首先会执行`acquire()`方法，只不过公平锁单独实现了`tryAcquire()`方法：

`#java.util.concurrent.locks.AbstractQueuedSynchronizer.acquire()`:

```
public final void acquire(int arg) {
    if (!tryAcquire(arg) &&
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg))
        selfInterrupt();
}

```

这里会执行`ReentrantLock`中公平锁的`tryAcquire()`方法

`#java.util.concurrent.locks.ReentrantLock.FairSync.tryAcquire()`:

```
static final class FairSync extends Sync {
    protected final boolean tryAcquire(int acquires) {
        final Thread current = Thread.currentThread();
        int c = getState();
        if (c == 0) {
            if (!hasQueuedPredecessors() &&
                compareAndSetState(0, acquires)) {
                setExclusiveOwnerThread(current);
                return true;
            }
        }
        else if (current == getExclusiveOwnerThread()) {
            int nextc = c + acquires;
            if (nextc < 0)
                throw new Error("Maximum lock count exceeded");
            setState(nextc);
            return true;
        }
        return false;
    }
}

```

这里会先判断`state`值，如果不为 0 且获取锁的线程不是当前线程，直接返回 false 代表获取锁失败，被加入等待队列。如果是当前线程则可重入获取锁。

如果`state=0`则代表此时没有线程持有锁，执行`hasQueuedPredecessors()`判断`AQS`等待队列中是否有元素存在，如果存在其他等待线程，那么自己也会加入到等待队列尾部，做到真正的先来后到，有序加锁。具体代码如下：

`#java.util.concurrent.locks.AbstractQueuedSynchronizer.hasQueuedPredecessors()`:

```
public final boolean hasQueuedPredecessors() {
    Node t = tail;
    Node h = head;
    Node s;
    return h != t &&
        ((s = h.next) == null || s.thread != Thread.currentThread());
}

```

这段代码很有意思，返回`false`代表队列中没有节点或者仅有一个节点是当前线程创建的节点。返回`true`则代表队列中存在等待节点，当前线程需要入队等待。

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDNlMDM2NzlhZA.jfif)

先判断`head`是否等于`tail`，如果队列中只有一个`Node`节点，那么`head`会等于`tail`。

接着判断`(s = h.next) == null`，这种属于一种极端情况，在`enq()`入队操作中，此时不是原子性操作，可能存在这种情况：

![YcAPpD.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzE2LzE3MjFjZDI1MTUzNmU3Y2M.jfif)

在第一个红框处，例如 **线程一** 执行完成，此时 head 已经有值，而还未执行`tail=head`的时候，此时 **线程二** 判断 `head != tail`成立。而接着 **线程一** 执行完第二个红框处，此时`tail = node`，但是并未将`head.next`指向`node`。而这时 **线程二** 就会得到`head.next == null`成立，直接返回 true。这种情况代表有节点正在做入队操作。

如果`head.next`不为空，那么接着判断`head.next`节点是否为当前线程，如果不是则返回 false。大家要记清楚，返回 false 代表 FIFO 队列中没有等待获取锁的节点，此时线程可以直接尝试获取锁，如果返回 true 代表有等待线程，当前线程如要入队排列，这就是体现**公平锁**的地方。

**非公平锁**和**公平锁**的区别： **非公平锁**性能高于**公平锁**性能。**非公平锁**可以减少`CPU`唤醒线程的开销，整体的吞吐效率会高点，`CPU`也不必取唤醒所有线程，会减少唤起线程的数量

**非公平锁**性能虽然优于**公平锁**，但是会存在导致**线程饥饿**的情况。在最坏的情况下，可能存在某个线程**一直获取不到锁**。不过相比性能而言，饥饿问题可以暂时忽略，这可能就是`ReentrantLock`默认创建非公平锁的原因之一了。

### Condition 实现原理

#### Condition 简介

上面已经介绍了`AQS`所提供的核心功能，当然它还有很多其他的特性，这里我们来继续说下`Condition`这个组件。

```
Condition`是在`java 1.5`中才出现的，它用来替代传统的`Object`的`wait()`、`notify()`实现线程间的协作，相比使用`Object`的`wait()`、`notify()`，使用`Condition`中的`await()`、`signal()`这种方式实现线程间协作更加安全和高效。因此通常来说比较推荐使用`Condition

```

其中`AbstractQueueSynchronizer`中实现了`Condition`中的方法，主要对外提供`awaite(Object.wait())`和`signal(Object.notify())`调用。

#### Condition Demo 示例

使用示例代码：

```
/**
 * ReentrantLock 实现源码学习
 * @author 一枝花算不算浪漫
 * @date 2020/4/28 7:20
 */
public class ReentrantLockDemo {
    static ReentrantLock lock = new ReentrantLock();

    public static void main(String[] args) {
        Condition condition = lock.newCondition();

        new Thread(() -> {
            lock.lock();
            try {
                System.out.println("线程一加锁成功");
                System.out.println("线程一执行 await 被挂起");
                condition.await();
                System.out.println("线程一被唤醒成功");
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                lock.unlock();
                System.out.println("线程一释放锁成功");
            }
        }).start();

        new Thread(() -> {
            lock.lock();
            try {
                System.out.println("线程二加锁成功");
                condition.signal();
                System.out.println("线程二唤醒线程一");
            } finally {
                lock.unlock();
                System.out.println("线程二释放锁成功");
            }
        }).start();
    }
}

```

执行结果如下图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDNlNjc4NTFiMw.jfif)

这里**线程一**先获取锁，然后使用`await()`方法挂起当前线程并**释放锁**，**线程二**获取锁后使用`signal`唤醒**线程一**。

#### Condition 实现原理图解

我们还是用上面的`demo`作为实例，执行的流程如下：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDNmOTE5NmRlYw.jfif)

**线程一**执行`await()`方法：

先看下具体的代码实现，`#java.util.concurrent.locks.AbstractQueuedSynchronizer.ConditionObject.await()`：

```
 public final void await() throws InterruptedException {
    if (Thread.interrupted())
        throw new InterruptedException();
    Node node = addConditionWaiter();
    int savedState = fullyRelease(node);
    int interruptMode = 0;
    while (!isOnSyncQueue(node)) {
        LockSupport.park(this);
        if ((interruptMode = checkInterruptWhileWaiting(node)) != 0)
            break;
    }
    if (acquireQueued(node, savedState) && interruptMode != THROW_IE)
        interruptMode = REINTERRUPT;
    if (node.nextWaiter != null) // clean up if cancelled
        unlinkCancelledWaiters();
    if (interruptMode != 0)
        reportInterruptAfterWait(interruptMode);
}

```

`await()`方法中首先调用`addConditionWaiter()`将当前线程加入到`Condition`队列中。

执行完后我们可以看下`Condition`队列中的数据：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDQwM2Y0NTRiYw.jfif)

具体实现代码为：

```
private Node addConditionWaiter() {
    Node t = lastWaiter;
    if (t != null && t.waitStatus != Node.CONDITION) {
        unlinkCancelledWaiters();
        t = lastWaiter;
    }
    Node node = new Node(Thread.currentThread(), Node.CONDITION);
    if (t == null)
        firstWaiter = node;
    else
        t.nextWaiter = node;
    lastWaiter = node;
    return node;
}

```

这里会用当前线程创建一个`Node`节点，`waitStatus`为`CONDITION`。接着会释放该节点的锁，调用之前解析过的`release()`方法，释放锁后此时会唤醒被挂起的**线程二**，**线程二**会继续尝试获取锁。

接着调用`isOnSyncQueue()`方法是判断当前的线程节点是不是在同步队列中，因为上一步已经释放了锁，也就是说此时可能有线程已经获取锁同时可能已经调用了`singal()`方法，如果已经唤醒，那么就不应该`park`了，而是退出`while`方法，从而继续争抢锁。

此时**线程一**被挂起，**线程二**获取锁成功。

具体流程如下图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDQyNTBmMzA4OQ.jfif)

**线程二**执行`signal()`方法：

首先我们考虑下**线程二**已经获取到锁，此时`AQS`等待队列中已经没有了数据。

接着就来看看**线程二**唤醒**线程一**的具体执行流程：

```
public final void signal() {
    if (!isHeldExclusively())
        throw new IllegalMonitorStateException();
    Node first = firstWaiter;
    if (first != null)
        doSignal(first);
}

```

先判断当前线程是否为获取锁的线程，如果不是则直接抛出异常。 接着调用`doSignal()`方法来唤醒线程。

```
private void doSignal(Node first) {
    do {
        if ( (firstWaiter = first.nextWaiter) == null)
            lastWaiter = null;
        first.nextWaiter = null;
    } while (!transferForSignal(first) &&
             (first = firstWaiter) != null);
}

final boolean transferForSignal(Node node) {
    if (!compareAndSetWaitStatus(node, Node.CONDITION, 0))
        return false;

    Node p = enq(node);
    int ws = p.waitStatus;
    if (ws > 0 || !compareAndSetWaitStatus(p, ws, Node.SIGNAL))
        LockSupport.unpark(node.thread);
    return true;
}

/**
 * Inserts node into queue, initializing if necessary. See picture above.
 * @param node the node to insert
 * @return node's predecessor
 */
private Node enq(final Node node) {
    for (;;) {
        Node t = tail;
        if (t == null) { // Must initialize
            if (compareAndSetHead(new Node()))
                tail = head;
        } else {
            node.prev = t;
            if (compareAndSetTail(t, node)) {
                t.next = node;
                return t;
            }
        }
    }
}

```

这里先从`transferForSignal()`方法来看，通过上面的分析我们知道`Condition`队列中只有线程一创建的一个`Node`节点，且`waitStatue`为`CONDITION`，先通过`CAS`修改当前节点`waitStatus`为 0，然后执行`enq()`方法将当前线程加入到等待队列中，并返回当前线程的前置节点。

加入等待队列的代码在上面也已经分析过，此时等待队列中数据如下图：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDQyNWZhMmU5ZQ.jfif)

接着开始通过`CAS`修改当前节点的前置节点`waitStatus`为`SIGNAL`，并且唤醒当前线程。此时`AQS`中等待队列数据为：

![image.png](assets/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAyMC81LzIvMTcxZDJkNDQ0ODQ0ZDI3ZQ.jfif)

**线程一**被唤醒后，继续执行`await()`方法中的 while 循环。

```
public final void await() throws InterruptedException {
    if (Thread.interrupted())
        throw new InterruptedException();
    Node node = addConditionWaiter();
    int savedState = fullyRelease(node);
    int interruptMode = 0;
    while (!isOnSyncQueue(node)) {
        LockSupport.park(this);
        if ((interruptMode = checkInterruptWhileWaiting(node)) != 0)
            break;
    }
    if (acquireQueued(node, savedState) && interruptMode != THROW_IE)
        interruptMode = REINTERRUPT;
    if (node.nextWaiter != null) // clean up if cancelled
        unlinkCancelledWaiters();
    if (interruptMode != 0)
        reportInterruptAfterWait(interruptMode);
}

```

因为此时线程一的`waitStatus`已经被修改为 0，所以执行`isOnSyncQueue()`方法会返回`false`。跳出`while`循环。

接着执行`acquireQueued()`方法，这里之前也有讲过，尝试重新获取锁，如果获取锁失败继续会被挂起。直到另外线程释放锁才被唤醒。

```
final boolean acquireQueued(final Node node, int arg) {
    boolean failed = true;
    try {
        boolean interrupted = false;
        for (;;) {
            final Node p = node.predecessor();
            if (p == head && tryAcquire(arg)) {
                setHead(node);
                p.next = null; // help GC
                failed = false;
                return interrupted;
            }
            if (shouldParkAfterFailedAcquire(p, node) &&
                parkAndCheckInterrupt())
                interrupted = true;
        }
    } finally {
        if (failed)
            cancelAcquire(node);
    }
}

```

此时**线程一**的流程都已经分析完了，等**线程二**释放锁后，**线程一**会继续重试获取锁，流程到此终结。

#### Condition 总结

我们总结下 Condition 和 wait/notify 的比较：

* Condition 可以精准的对多个不同条件进行控制，wait/notify 只能和 synchronized 关键字一起使用，并且只能唤醒一个或者全部的等待队列；
* Condition 需要使用 Lock 进行控制，使用的时候要注意 lock()后及时的 unlock()，Condition 有类似于 await 的机制，因此不会产生加锁方式而产生的死锁出现，同时底层实现的是 park/unpark 的机制，因此也不会产生先唤醒再挂起的死锁，一句话就是不会产生死锁，但是 wait/notify 会产生先唤醒再挂起的死锁。

### 总结

这里用了一步一图的方式结合三个线程依次加锁/释放锁来展示了`ReentrantLock`的实现方式和实现原理，而`ReentrantLock`底层就是基于`AQS`实现的，所以我们也对`AQS`有了深刻的理解。

另外还介绍了**公平锁**与**非公平锁**的实现原理，`Condition`的实现原理，基本上都是使用**源码+绘图**的讲解方式，尽量让大家更容易去理解。

---

© 2019 - 2023 [Liangliang Lee](/cdn-cgi/l/email-protection#b0dcdcdc898481818087f0d7ddd1d9dc9ed3dfdd).
Powered by [gin](https://github.com/gin-gonic/gin) and [hexo-theme-book](https://github.com/kaiiiz/hexo-theme-book).