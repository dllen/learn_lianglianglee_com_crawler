# MySQL 地基基础：事务和锁的面纱 

Source: https://learn.lianglianglee.com/%e6%96%87%e7%ab%a0/MySQL%20%e5%9c%b0%e5%9f%ba%e5%9f%ba%e7%a1%80%ef%bc%9a%e4%ba%8b%e5%8a%a1%e5%92%8c%e9%94%81%e7%9a%84%e9%9d%a2%e7%ba%b1.md

MySQL 地基基础：事务和锁的面纱 



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

# MySQL 地基基础：事务和锁的面纱

### 什么是事务，为什么需要事务

在 MySQL 中，事务是由一条或多条 SQL 组成的单位，在这个单位中所有的 SQL 共存亡，有点有福同享，有难同当的意思。要么全部成功，事务顺利完成；要么只要有一个 SQL 失败就会导致整个事务失败，所有已经做过的操作回退到原始数据状态。

### 用日常细说事务的特性

首先我们先说一下事务的四个特性：ACID。

* A：原子性（atomicity），一个事务要么全都成功，要么全都失败
* C：一致性（consistency），在事务的整个生命周期里，查询的数据是一致的，保证数据库不会返回未提交的事务的数据
* I：隔离性（isolation），一个事务所做的操作，在最终提交前，对其他事务是不可见的，保证事务与事务之间不会冲突
* D：持久性（durability），只要事务提交，数据就不会丢失，即使系统崩溃，事务也已经完成

在日常生活中有很多的事情就能体现为数据库中的事务。比如“转账”，下面我们就具体展开，你就可以很清晰的认识事务的四个特性。

* 时间：2020 年 1 月 1 日
* 地点：某银行 ATM
* 人物：A 和 B
* 起因：B 向 A 借 1000 元人民币
* 经过：A 转账给 B
* 结果：转账成功或失败

这么一个转账我们想一下底层基本的技术支撑与实现，B 向 A 借钱，A 要转账给 B，首先 A 必须有大于 1000 元的余额，然后从 A 的账户减 1000 元，在 B 的账户里加 1000 元。

我们定义一个事务：

```
获取 A 账户余额
select balance from account where username='A';
在 A 账户里减 1000 元
update account set balance=balance-1000 where username='A';
获取 B 账户余额
select balance from account where username='B';
在 B 账户里加 1000 元
update account set balance=balance+1000 where username='B';

```

好了，一个简单事务基本就这样，我们开始分析分析这个事务是如何保证事务的 ACID 的。

* **原子性**：这个事务要么全成功，要么全失败。事务成功则 1000 元转账到了 B 账户，事务失败回滚则 1000 元还在 A 账户里，就是说 1000 元不能凭空消失。
* **一致性**：在这个事务中，所有的查询都是一致的，我们先查询 A 账户余额是否大于 1000，如果小于 1000，事务失败回滚；如果获取不到 B 账户余额，事务失败回滚。
* **隔离性**：在这个事务发生的同时，发生了另一个事务（A 通过手机银行将钱全部转移到另外的账户，比如一共有 1500 元），第一个事务转 1000 元，第二个事务转 1500 元，我们仔细想想，如果都成功，那岂不是凭空获取了 1000 元，这是不合理的，每个事务在执行前都应查一下余额是否够本次转账的。这两个事务应该是隔离的，不能有冲突。
* **持久性**：转账成功了（即事务完成），这代表钱已经发生了转移，这个时候发生 ATM 吞卡、ATM 断电、手机银行无法登陆等等一切故障，反正钱已经转走了，钱没有丢（即数据没有丢）

### MySQL 并发控制技术

并发控制技术可以说是数据库的底层基础技术，并发控制技术可以拆分来看，一是并发，一是控制。并发也就是说大量请求连接到数据库，控制就是数据库要控制好这些连接，保证资源的可用性、安全性，解决资源的挣用的问题。

那么如何实现并控制呢？主要通过两个方面：

* Lock
* MVCC

先分别简单说一下 Lock 和 MVCC，具体的后面再聊。

* Lock，并发连接到数据库，操作有读和读、读和写、写和写，锁来保证并发连接使得数据可以保持一致性。
* MVCC（Multiversion Concurrency Control），多版本并发控制，是数据库的多版本，可以提高并发过程中的读和写操作，有效的避免写请求阻塞读请求。

### 面试再也不怕被问到的 MVCC

前面我们已经大致了解了 MVCC 是什么，以及他做什么事情，现在我们具体看看 MVCC 是如何工作的？

我们知道数据的一致性，可以通过锁来保证，在并发连接中，锁机制在读和读的并发请求中不会锁数据，但是在读和写的并发请求中，写请求会加锁，读请求会被写请求阻塞，基于此，MVCC 发挥其作用。

MVCC 控制两类操作：

* 快照读：读取的是历史可见版本的数据，无锁
* 当前读：读取的是当前最新版本的数据，加锁

我们举个例子说一下吧，比如:

```
mysql> create table tab1(id decimal,name varchar(10),address varchar(10),status decimal,primary key(id));
mysql> insert into tab1 values(1,'a','beijing',1); 

```

表中数据为：

| id | name | address | status |
| --- | --- | --- | --- |
| 1 | a | beijing | 1 |

现在有一个请求，将数据 a 的地址改为 shanghai，这个数据更新的过程，我们细化一下，将历史数据置为失效，将新的数据插入：

```
mysql> update tab1 set status=0 where name='a';
mysql> insert into tab1 value(2,'a','shanghai',1);

```

表中数据为：

| id | name | address | status |
| --- | --- | --- | --- |
| 1 | a | beijing | 0 |
| 2 | a | shanghai | 1 |

MVCC 的原理就类似是这样的，`address='beijing'` 就是历史数据，更新前保存了下来，`address='shanghai'` 就是当前数据，新插入数据，这样并发连接来了，既可以读取历史数据，也可以修改当前数据。比如，现在有三个事务：

* T1 -> 要执行 update address
* T2 -> 要执行 update address
* T3 -> 要执行 update address

T1 先获取了表中这一行数据，执行了 update，未提交；T2 获取表中这一行数据，由于 T1 未提交，address=‘beijing’,这个 beijing 就来源历史数据；T3 也获取表中这一行数据，由于 T1 未提交，`address='beijing'`，这个 beijing 也来源历史数据。这样是不是好理解了。

以此类推，如果只对 `name='a'` 这一行数据有 N 个并发连接要做 M 个操作，这些历史数据都保存在表中，这个表的数据量无法预估，势必会造成压力与瓶颈。多版本数据到底如何保存，这就不是本节考虑的问题了，是数据库 undo 帮你做的工作。这里就不展开了。（后期可能会做 undo 相关的 chat，大家可以关注我）

### 简单易懂的实例帮你理解 MySQL 事务隔离级别

事务隔离级别，拆分来看，事务、隔离、级别，故是三个概念的集合，是保证事务之间相互隔离互不影响的，有多个级别。事务在执行过程中可能会出现脏读、不可重复读、幻读，那么 MySQL 的事务隔离级别到底有怎样的表现呢？

| 事务隔离级别 | 脏读 | 不可重复读 | 幻读 |
| --- | --- | --- | --- |
| 读未提交(Read-Uncommited) | 可能 | 可能 | 可能 |
| 读提交(Read-Commited) | 不可能 | 可能 | 可能 |
| 可重复读交(Repeatable-Read) | 不可能 | 不可能 | 可能 |
| 序列化(Serializable) | 不可能 | 不可能 | 不可能 |

那么到底什么是脏读、不可重复读、幻读呢？

* **脏读**：一个事务读取了另一个未提交事务操作的数据。
* **不可重复读**：一个事务重新读取前面读取过的数据时，发现该数据已经被修改了或者不见了，其实已被另一个已提交的事务操作了。解决了脏读的问题。
* **幻读**：一个事务，需要更新数据，于是重新提交了一个查询，返回符合查询条件行，发现这些行因为其他提交的事务发生了改变，这些数据像“幻影”一样出现了。解决了不可重复读。

接下来我们用具体实例分析各个事务隔离级别。

创建测试表 t\_account：

```
mysql> create table t_account(name varchar(10),balance decimal);
mysql> insert into t_account values('A',100);
mysql> insert into t_account values('B',0);

```

#### 读未提交

设置事务隔离级别：

```
mysql> set global tx_isolation='read-uncommitted';          

```

查询事务隔离级别：

```
mysql>  SELECT @@tx_isolation;
+------------------+
| @@tx_isolation   |
+------------------+
| READ-UNCOMMITTED |
+------------------+
1 row in set (0.00 sec)

```

**当前事务可以读取另一个未提交事务操作的数据。**

环境：用户 A 有 100 元钱，给用户 A 增加 100 元，然后用户 A 转账给用户 B。

| 事务 1 | 事务 2 |
| --- | --- |
| begin; | begin; |
| update t\_account set balance=balance+100 where name=‘A’; #给用户 A 增加 100 元 |  |
|  | select balance from t\_account where name=‘A’; #转账前查询用户 A 余额为 200 元 |
| rollback; #决定不给用户 A 增加 100 元了，事务回滚 |  |
|  | update t\_account set balance=balance-200 where name=‘A’; #用户 A 继续给用户 B 转账，用户 A 减 200 元 |
|  | update t\_account set balance=balance+200 where name=‘B’; #用户 A 继续给用户 B 转账，用户加加 200 元 |
|  | commit; #提交事务 |

现在我们查询一下用户 A 和用户 B 的余额：

```
mysql> select * from t_account;
+------+---------+
| name | balance |
+------+---------+
| A    |    -100 |
| B    |     200 |
+------+---------+
2 rows in set (0.00 sec)

```

问题来了，这个结果不符合预期，用户 A 竟然是 -100 元，用户 B 增加了 200 元，这是因为事务 2 读取了事务 1 未提交的数据。

#### 读提交

设置事务隔离级别：

```
mysql> set global tx_isolation='read-committed';          

```

查询事务隔离级别：

```
mysql>  SELECT @@tx_isolation;
+------------------+
| @@tx_isolation   |
+------------------+
| READ-COMMITTED    |
+------------------+
1 row in set (0.00 sec)

```

**当前事务只能读取另一个提交事务操作的数据。**

环境：用户 A 有 100 元钱，给用户 A 增加 100 元。

| 事务 1 | 事务 2 |
| --- | --- |
| begin; | begin; |
| update t\_account set balance=balance+100 where name=‘A’; #给用 A 增加 100 元 |  |
|  | select \* from t\_account where name=‘A’; #事务 2 查用户的余额，因事务 1 未提交，仍为 100 元 |
| commit; |  |
|  | select \* from t\_account where name=‘A’; #事务 2 查用户的余额，事务 1 已提交，变为 200 元 |

一个事务重新读取前面读取过的数据时，发现该数据已经被修改了，其实已被另一个已提交的事务操作了。

#### 可重复读

设置事务隔离级别：

```
mysql> set global tx_isolation='repeatable-read';          

```

查询事务隔离级别：

```
mysql>  SELECT @@tx_isolation;
+------------------+
| @@tx_isolation   |
+------------------+
| REPEATABLE-READ  |
+------------------+
1 row in set (0.00 sec)

```

**当前事务读取通过第一次读取建立的快照是一致的，即使另外一个事务提交了该数据。除非自己这个事务可以读取在自身事务中修改的数据。**

可重复读隔离级别是 MySQL 的默认隔离级别。

环境：用户 A 有 100 元钱，给用户 A 增加 100 元。

| 事务 1 | 事务 2 |
| --- | --- |
| begin; | begin; |
|  | select \* from t\_account where name=‘A’; #事务 2 查用户的余额，为 100 元 |
| update t\_account set balance=balance+100 where name=‘A’; #给用 A 增加 100 元 |  |
|  | select \* from t\_account where name=‘A’; #事务 2 查用户的余额，因事务 1 未提交，仍为 100 元 |
| commit; |  |
|  | select \* from t\_account where name=‘A’; #事务 2 查用户的余额，事务 1 已提交，仍为 100 元 |

这就能看出来，事务 2 开启后读取了用户 A 的余额，即使事务 1 修改了数据，不管提交与否，事务 2 读取的数据一直是之前第一次读取的数据。继续操作。

| 事务 1 | 事务 2 |
| --- | --- |
|  | commit; |
|  | select \* from t\_account where name=‘A’; ###事务 2 查用户的余额，为 200 元 |

为什么现在变成了 200 元了，因为事务 2 已经 commit，再次 select 是一个新的事务，读取数据当然又变为第一次获取数据（此时的数据是最新的数据）。

思考一下：上述这个举例是可重复读的 select 相关验证，如果是 DML 操作，会不会是同样的结果呢？

思考三分钟……

答案是：其他事物即使查询不到的数据，DML 操作也可能会影响那些提交的数据。好，让我验证一下。

update 操作：

| 事务 1 | 事务 2 |
| --- | --- |
| begin; | begin; |
| select \* from t\_account; #有一行数据，用户 A，余额 100 元 |  |
|  | insert into t\_account values(‘B’,100); #增加用户 B，余额 100 元 |
|  | commit; |
| select \* from t\_account where name=‘B’; #无返回行，查询不到用户 B |  |
| update t\_account set balance=balance+100 where name=‘B’; #神奇，更新成功了 |  |
| select \* from t\_account; #用户 A 余额 100，用户 B 余额 200 |  |
|  | select \* from t\_account; #用户 A 余额 100，用户 B 余额 100 |
| commit; |  |
|  | select \* from t\_account; #用户 A 余额 100，用户 B 余额 200 |

delete 操作：

| 事务 1 | 事务 2 |
| --- | --- |
| begin; | begin; |
| select \* from t\_account; #有 2 行数据，用户 A 余额 100 元，用户 B 余额 200 |  |
|  | insert into t\_account values(‘C’,100); #增加用户 C，余额 100 元 |
|  | commit; |
| select \* from t\_account where name=‘C’; #无返回行，查询不到用户 C |  |
| delete from t\_account where name=‘C’; #神奇，删除成功了 |  |
| select \* from t\_account; #用户 A 余额 100，用户 B 余额 200 |  |
|  | select \* from t\_account; #用户 A 余额 100，用户 B 余额 200，用户 C 余额 100 |
| commit; |  |
|  | select \* from t\_account; #户 A 余额 100，用户 B 余额 200 |

通过这两个例子你是不是了解了一个事务的 update 和 delete 操作了另外一个事务提交的数据，会使得这些数据在当前事务变得可见。就像幻影一下出现了！

#### 序列化

设置事务隔离级别：

```
mysql> set global tx_isolation='serializable';          

```

查询事务隔离级别：

```
mysql>  SELECT @@tx_isolation;
+------------------+
| @@tx_isolation   |
+------------------+
| SERIALIZABLE     |
+------------------+
1 row in set (0.00 sec)

```

**当前事务 select 和 DML 操作的数据都会加行锁，其他事务访问同样的数据需要等锁释放。**

环境：用户 A 有 100 元钱，给用户 A 增加 100 元。

| 事务 1 | 事务 2 |
| --- | --- |
| begin; | begin; |
| select \* from t\_account where name=‘A’; #查询用户余额 |  |
|  | update t\_account set balance=balance+100 where name=‘A’; #给用户 A 增加 100 元，执行一直处于等待 |
| commit; |  |
|  | update 成功返回 |
| select \* from t\_account where name=‘A’; #用户 A 余额为 100，因为事务 2 还未提交，获取的是 undo 中的历史版本数据 |  |
| begin; |  |
| select \* from t\_account where name=‘A’; #新开一个事务，由于事务 2 还未提交，此查询锁等 |  |
|  | commit; |
| select \* from t\_account where name=‘A’; #用户 A 余额 200 |  |

好了，实例讲解到此结束，是否已经帮你理解了 MySQL 事务隔离级别。

另外，结合前面说的 MVCC，Read-Committed 和 Repeatable-Read，支持 MVCC；Read-Uncommitted 由于可以读取未提交的数据，不支持 MVCC；Serializable 会对所有读取的数据加行锁，不支持 MVCC。

### MySQL 锁机制（机智）

锁是可以协调并发连接访问 MySQL 数据库资源的一种技术，可以保证数据的一致性。锁有两个阶段：加锁和解锁，InnoDB 引擎的锁主要有两类。

**共享锁（S）**

允许一个事务读取数据，阻塞其他事务想要获取相同数据。共享锁之间不互斥，读和读操作可以并行。代码展示：

```
select * from table where ... lock in share mode

```

**排它锁（X）**

持有排他锁的事务可以更新数据，阻塞其他事务获取数据的排他锁和共享锁。排它锁之间互斥，读和写、写和写操作不可以并行。代码展示：

```
select * from table where ... for update;

```

从 MySQL 数据库的内外区分锁，有两种锁。

**内部锁**

MySQL 在数据库内部自动管理，协调并发连接的资源争用。内部锁再具体来看分为：

* 行锁：会话事务将访问的行数据加锁
* 表锁：会话事务将访问的表整体加锁

**外部锁**

会话层使用特殊的手段显示获取锁，阻塞其他会话对数据的操作。我们通过外部操作命令实现外部锁，比如使用 lock table 和 unlock tables。

我们举个例子来描述一下这个过程吧，比如有事务 1 和事务 2，事务 1 锁定了一行数据，加了一个 S 锁；事务 2 想要对整个表加锁，需要判断这个表是否被加了表锁，表中的每一行是否有行锁。仔细想想这个过程是很快呢？还是非常的慢？如果表很小无所谓了，如果表是海量级数据，那糟了，事务 2 势必耗费很多资源。

如何解决事务 2 这种检索资源消耗的问题呢？事务意向锁帮你先获取意向，先一步问问情况，然后再获取我们想要的 S 和 X 锁，具体分为：

**意向共享锁（IS）**

事务 1 说：我要加一个行锁，我有这个意向，你们其他人有没有意见，如果没有我就先拿这个 IS 锁了。

**意向排它锁（IX）**

事务 2 说：我要加一个表锁，这个可是排他锁，我拿了你们就等我用完再说吧，我有这个意向，你们其他人有没有意见，如果没有我就先拿这个 IX 锁了。

前面这个举例，其过程升级优化为：

* 事务 1 先申请获取 IS 锁，成功后，获取 S 锁
* 事务 2 发现表中有 IS 锁了，事务 2 获取表锁会被阻塞

那么这四个锁之间兼容性如何呢？

|  | X | S | IX | IS |
| --- | --- | --- | --- | --- |
| X | 冲突 | 冲突 | 冲突 | 冲突 |
| S | 冲突 | 兼容 | 冲突 | 兼容 |
| IX | 冲突 | 冲突 | 兼容 | 兼容 |
| IS | 冲突 | 兼容 | 兼容 | 兼容 |

### 聊几个经典死锁案例

在实际应用中经常发生数据库死锁的情况，那么什么是死锁呢？说白了就是事务 1 锁事务 2，事务 2 锁事务 1，这两个事务都在等着对方释放锁资源，陷入了死循环。

接下来我们介绍几个经典死锁案例，MySQL 默认级别使用的是 REPEATABLE-READ。

#### 场景 1：insert 死锁

创建一个测试表：

```
mysql> create table t_insert(id decimal,no decimal,primary key(id),unique key(no));

```

session1：

```
mysql> begin;
mysql> insert into t_insert values(1,101);

```

session2：

```
mysql> begin;
mysql> insert into t_insert values(2,101);

```

此时会话一直等待无响应。

session1：

```
mysql> insert into t_insert values(3,100);

```

结果如下。

此时 session2 立马报出来死锁：

```
ERROR 1213 (40001): ==Deadlock== found when trying to get lock; try restarting transaction

```

数据库中 insert 作为最简单的 SQL，为什么会导致死锁呢？

session1 在插入(1,101) 的时候会加一个 X 锁；session2 插入(2,101)，no 字段有着唯一性，故 session2 在插入时数据库会做 duplicate 冲突检测，由于事务冲突先加 S 锁；然后 session1 又插入了 (3,100)，此时 session1 会加 insert intention X 锁（插入意向锁），之前 session1 已经有了 X 锁，故进入等待队列，结局就是 session1 和 session2 都在等待，陷入了僵局，MySQL 很机智，牺牲一方事务解决这个尴尬的局面，所以 session2 被干掉了，报错死锁。

#### 场景 2：自增列死锁

自增列死锁问题和场景 1 的类似，比如将场景 1 的主键属性改为自增长属性，主键自增仍唯一，场景模拟类似，加锁的过程也类似，产生死锁的过程也类似，这里就不详细模拟了。

#### 场景 3：rollback 死锁

创建一个测试表：

```
mysql> create table t_rollback(id decimal,no decimal,primary key(id),unique key(no));

```

session1：

```
mysql> begin;
mysql> insert into t_rollback values(1,100);

```

session2：

```
mysql> begin;
mysql> insert into t_rollback values(2,100);

```

此时会话一直等待无响应。

session3

```
mysql> begin;
mysql> insert into t_rollback values(3,100);

```

此时会话一直等待无响应。

session1

```
mysql> rollback;

```

结果如下： 此时 session1 执行了 rollback 成功返回，session2 的 insert 返回成功，session3 立马报出来死锁。

```
ERROR 1213 (40001): ==Deadlock== found when trying to get lock; try restarting transaction

```

为什么我回滚了事务，还要报死锁，难道我需要全部回滚吗？

session1 在插入 (1,100) 的时候会加一个 X 锁；session2 插入 (2,100)，no 字段有着唯一性，故 session2 在插入时数据库会做 duplicate 冲突检测，由于事务冲突先加 S 锁；session3 插入 (3,100)，no 字段有着唯一性，故 session3 在插入时数据库会做 duplicate 冲突检测，由于事务冲突先加 S 锁；session1 回滚，session2 申请 insert intention X 锁，等 session3;session3 申请 insert intention X 锁，等 session2，结局就是 session2 和 session3 都在等待，陷入了僵局，MySQL 很机智，牺牲一方事务解决这个尴尬的局面，所以 session3 被干掉了，报错死锁。

#### 场景 4：commit 死锁

创建一个测试表：

```
mysql> create table t_commit(id decimal,no decimal,primary key(id),unique key(no));
mysql> insert into t_commit values(1,100);

```

session1：

```
mysql> begin;
mysql> delete from t_commit where id=1;

```

session2：

```
mysql> begin;
mysql> insert into t_commit values(1,100);

```

此时会话一直等待无响应。

session3：

```
mysql> begin;
mysql> insert into t_commit values(1,100);

```

此时会话一直等待无响应。

session1：

```
mysql> commit;

```

结果如下：此时 session1 执行了 commit 成功返回，session3 的 insert 返回成功，session2 立马报出来死锁。

```
ERROR 1213 (40001): ==Deadlock== found when trying to get lock; try restarting transaction

```

为什么我提交了事务，还要报死锁，难道我需要全部提交吗？

这个产生死锁的过程和场景 3rollback 死锁类似，大家可以和之前的 rollback 死锁产生过程对应来看。

### 小技巧——事务保存点帮你读档重闯关

玩游戏你是不是有过存档、读档的经历，过某一个比较难的关卡，先存档，过不了，就读档重新过。数据库中我们也可以如此，MySQL 事务保存点可以回滚到事务的某时间点，并且不用中止事务。下面举例说明一下。

用户 B 和用户 C 向用户 A 借钱，用户 A 转账给用户 B 和用户 C，转账的过程中发生了用户 C 账户不存在，那么我们也要把转给用户 B 的钱也取消吗？我们可以不取消，使用一个保存点即可。

查询用户 A 有 1000 元：

```
mysql> select balance from t_account where name='A';

```

转账 100 元给用户 B：

```
mysql> update t_account set balance=balance-100 where name='A';
mysql> update t_account set balance=balance+100 where name='B';

```

**设置事务保存点**

```
mysql> savepoint T_A_TO_B;

```

转账 200 元给用户 C：

```
mysql> update t_account set balance=balance-200 where name='A';
mysql> update t_account set balance=balance+200 where name='C';
Query OK, 0 rows affected (0.00 sec)
Rows matched: 0  Changed: 0  Warnings: 0

```

发现转账给 C 返回有 0 条受影响的行，转账给 C 未成功，此时用户 A 已经少了 200 元了，先退 200 元再排查吧，转账给用户 B 的不需要重新操作了。

```
mysql> rollback to T_A_TO_B;
mysql> commit；

```

根据提示 0 条受影响的行，也就是说用户 C 不存在呀，我们查询一下个用户信息：

```
mysql> select * from t_account where name='A';
+------+---------+
| name | balance |
+------+---------+
| A    |     900 |
+------+---------+
1 row in set (0.00 sec)

mysql> select * from t_account where name='B';
+------+---------+
| name | balance |
+------+---------+
| B    |     200 |
+------+---------+
1 row in set (0.00 sec)

mysql> select * from t_account where name='C';
Empty set (0.00 sec)

```

结果：用户 A 成功转 100 元给用户 B，用户 C 果然不存才，设置了保存点，帮我们省了很多工作，中途不用取消全部操作。

### 小技巧——一个死锁的具体分析方法

前面我们学习了事务、锁，以及介绍了几个经典死锁案例，当遇到死锁，我们怎样具体分析呢？

分析死锁，我们就需要看死锁的日志信息，通过日志具体找到死锁的原因及执行的语句。

首先，我们用前面的场景 1 模拟一个死锁。

然后，执行如下命令获取死锁信息：

```
mysql> show engine innodb status;

```

在打印的日志中，先看事务 1 的日志：

```
*** (1) TRANSACTION:
TRANSACTION 2179, ACTIVE 8 sec inserting
mysql tables in use 1, locked 1
LOCK WAIT 2 lock struct(s), heap size 1136, 1 row lock(s), undo log entries 1
MySQL thread id 32, OS thread handle 140317789804288, query id 823 localhost root update
insert into t_insert values(2,101)
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 37 page no 4 n bits 72 index no of table `test`.`t_insert` trx id 2179 lock mode S waiting
Record lock, heap no 2 PHYSICAL RECORD: n_fields 2; compact format; info bits 0
 0: len 5; hex 8000000065; asc     e;;
 1: len 5; hex 8000000001; asc      ;;
TRANSACTION 2179, ACTIVE ==8 sec== inserting

```

事务 1 持续了 8 秒：

```
mysql ==tables in use 1==, locked 1  涉及一张表  
LOCK WAIT 2 lock struct(s) 有两个锁  
insert into t_insert values(2,101) 这是 SQL 语句  
WAITING FOR THIS LOCK TO BE GRANTED 唯一行锁处于等待  
RECORD LOCKS space id 37 page no 4 n bits 72 index no 加锁的是索引字段 no  
lock mode S waiting 锁等待为 S 锁

```

事务 2 的日志：

```
*** (2) TRANSACTION:
TRANSACTION 2178, ACTIVE 17 sec inserting
mysql tables in use 1, locked 1
3 lock struct(s), heap size 1136, 2 row lock(s), undo log entries 2
MySQL thread id 33, OS thread handle 140317663659776, query id 824 localhost root update
insert into t_insert values(3,100)
*** (2) HOLDS THE LOCK(S):
RECORD LOCKS space id 37 page no 4 n bits 72 index no of table `test`.`t_insert` trx id 2178 lock_mode X locks rec but not gap
Record lock, heap no 2 PHYSICAL RECORD: n_fields 2; compact format; info bits 0
 0: len 5; hex 8000000065; asc     e;;
 1: len 5; hex 8000000001; asc      ;;

*** (2) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 37 page no 4 n bits 72 index no of table `test`.`t_insert` trx id 2178 lock_mode X locks gap before rec insert intention waiting
Record lock, heap no 2 PHYSICAL RECORD: n_fields 2; compact format; info bits 0
 0: len 5; hex 8000000065; asc     e;;
 1: len 5; hex 8000000001; asc      ;;

```

* `HOLDS THE LOCK(S)` 持有锁的内容
* `lock_mode X locks` 持有锁的锁等待内容是一个 x 锁
* `WAITING FOR THIS LOCK TO BE GRANTED` 等待锁的内容
* `lock_mode X locks gap before rec insert intention waiting` 等待锁的锁等待内容也是一个 x 锁

通过这些日志，我们发现日志中的事务 1，持有 S 锁，S 锁的出现是因为需要检查数据唯一性，我们的 no 字段确实有唯一索引，这一点也正好验证了。日志中的事务 1，持有一个 X 锁，又等待一个 X 锁。所以场景 1 中的两个事务都在锁等，造成了死锁。

### 小技巧——换种思路提高事务能力

在数据中如果是单一事务，那没的说，一个一个的事务来执行，毫无压力。现实是不允许这样的，肯定是有大量的并发连接，并发事务在所难免。如果高并发的环境中，事务处理效率肯定大幅下降，这个时候我们有没有方法提高并发事务能力呢？

我们解决技术处理问题的限制，这次我们换一种思路来提高事务能力。比如：

**合理的在线、离线数据库**

比如我们的系统数据量日益增加，还有一些业务需要查询大量的数据，我们可以改造系统为在线、离线数据库，在线表提供高效事务能力，离线表提供数据查询服务，互不影响。

**提高 delete 操作效率的思考**

如果你对表有大量数据的 delete 操作，比如定期的按日、月、年删除数据，可以设计表为日表、月表、年表亦或是相对应的分区表，这样清理数据会由大事务降低为小事务。

---

© 2019 - 2023 [Liangliang Lee](/cdn-cgi/l/email-protection#b0dcdcdc898481818087f0d7ddd1d9dc9ed3dfdd).
Powered by [gin](https://github.com/gin-gonic/gin) and [hexo-theme-book](https://github.com/kaiiiz/hexo-theme-book).