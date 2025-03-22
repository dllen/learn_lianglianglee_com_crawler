# MySQL · 引擎特性 · InnoDB崩溃恢复 

Source: https://learn.lianglianglee.com/%e6%96%87%e7%ab%a0/MySQL%20%c2%b7%20%e5%bc%95%e6%93%8e%e7%89%b9%e6%80%a7%20%c2%b7%20InnoDB%e5%b4%a9%e6%ba%83%e6%81%a2%e5%a4%8d.md

MySQL · 引擎特性 · InnoDB崩溃恢复 



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

# MySQL · 引擎特性 · InnoDB崩溃恢复

## 前言

数据库系统与文件系统最大的区别在于数据库能保证操作的原子性，一个操作要么不做要么都做，即使在数据库宕机的情况下，也不会出现操作一半的情况，这个就需要数据库的日志和一套完善的崩溃恢复机制来保证。本文仔细剖析了InnoDB的崩溃恢复流程，代码基于5.6分支。

## 基础知识

\*\*lsn: \*\* 可以理解为数据库从创建以来产生的redo日志量，这个值越大，说明数据库的更新越多，也可以理解为更新的时刻。此外，每个数据页上也有一个lsn，表示最后被修改时的lsn，值越大表示越晚被修改。比如，数据页A的lsn为100，数据页B的lsn为200，checkpoint lsn为150，系统lsn为300，表示当前系统已经更新到300，小于150的数据页已经被刷到磁盘上，因此数据页A的最新数据一定在磁盘上，而数据页B则不一定，有可能还在内存中。
\*\*redo日志: \*\* 现代数据库都需要写redo日志，例如修改一条数据，首先写redo日志，然后再写数据。在写完redo日志后，就直接给客户端返回成功。这样虽然看过去多写了一次盘，但是由于把对磁盘的随机写入(写数据)转换成了顺序的写入(写redo日志)，性能有很大幅度的提高。当数据库挂了之后，通过扫描redo日志，就能找出那些没有刷盘的数据页(在崩溃之前可能数据页仅仅在内存中修改了，但是还没来得及写盘)，保证数据不丢。
\*\*undo日志: \*\* 数据库还提供类似撤销的功能，当你发现修改错一些数据时，可以使用rollback指令回滚之前的操作。这个功能需要undo日志来支持。此外，现代的关系型数据库为了提高并发(同一条记录，不同线程的读取不冲突，读写和写读不冲突，只有同时写才冲突)，都实现了类似MVCC的机制，在InnoDB中，这个也依赖undo日志。为了实现统一的管理，与redo日志不同，undo日志在Buffer Pool中有对应的数据页，与普通的数据页一起管理，依据LRU规则也会被淘汰出内存，后续再从磁盘读取。与普通的数据页一样，对undo页的修改，也需要先写redo日志。
\*\*检查点: \*\* 英文名为checkpoint。数据库为了提高性能，数据页在内存修改后并不是每次都会刷到磁盘上。checkpoint之前的数据页保证一定落盘了，这样之前的日志就没有用了(由于InnoDB redolog日志循环使用，这时这部分日志就可以被覆盖)，checkpoint之后的数据页有可能落盘，也有可能没有落盘，所以checkpoint之后的日志在崩溃恢复的时候还是需要被使用的。InnoDB会依据脏页的刷新情况，定期推进checkpoint，从而减少数据库崩溃恢复的时间。检查点的信息在第一个日志文件的头部。
\*\*崩溃恢复: \*\* 用户修改了数据，并且收到了成功的消息，然而对数据库来说，可能这个时候修改后的数据还没有落盘，如果这时候数据库挂了，重启后，数据库需要从日志中把这些修改后的数据给捞出来，重新写入磁盘，保证用户的数据不丢。这个从日志中捞数据的过程就是崩溃恢复的主要任务，也可以成为数据库前滚。当然，在崩溃恢复中还需要回滚没有提交的事务，提交没有提交成功的事务。由于回滚操作需要undo日志的支持，undo日志的完整性和可靠性需要redo日志来保证，所以崩溃恢复先做redo前滚，然后做undo回滚。

我们从源码角度仔细剖析一下数据库崩溃恢复过程。整个过程都在引擎初始化阶段完成(`innobase_init`)，其中最主要的函数是`innobase_start_or_create_for_mysql`，innodb通过这个函数完成创建和初始化，包括崩溃恢复。首先来介绍一下数据库的前滚。

## redo日志前滚数据库

前滚数据库，主要分为两阶段，首先是日志扫描阶段，扫描阶段按照数据页的space\_id和page\_no分发redo日志到hash\_table中，保证同一个数据页的日志被分发到同一个哈希桶中，且按照lsn大小从小到大排序。扫描完后，再遍历整个哈希表，依次应用每个数据页的日志，应用完后，在数据页的状态上至少恢复到了崩溃之前的状态。我们来详细分析一下代码。
首先，打开所有的ibdata文件(`open_or_create_data_files`)(ibdata可以有多个)，每个ibdata文件有个flush\_lsn在头部，计算出这些文件中的max\_flush\_lsn和min\_flush\_lsn，因为ibdata也有可能有数据没写完整，需要恢复，后续(`recv_recovery_from_checkpoint_start_func`)通过比较checkpont\_lsn和这两个值来确定是否需要对ibdata前滚。
接着，打开系统表空间和日志表空间的所有文件(`fil_open_log_and_system_tablespace_files`)，防止出现文件句柄不足，清空buffer pool(`buf_pool_invalidate`)。接下来就进入最最核心的函数:recv\_recovery\_from\_checkpoint\_start\_func，注意，即使数据库是正常关闭的，也会进入。
虽然`recv_recovery_from_checkpoint_start_func`看过去很冗长，但是很多代码都是为了LOG\_ARCHIVE特性而编写的，真正数据崩溃恢复的代码其实不多。
首先，初始化一些变量，查看`srv_force_recovery`这个变量，如果用户设置跳过前滚阶段，函数直接返回。
接着，初始化`recv_sys`结构，分配hash\_table的大小，同时初始化flush list rbtree。`recv_sys`结构主要在崩溃恢复前滚阶段使用。hash\_table就是之前说的用来存不同数据页日志的哈希表，哈希表的大小被初始化为buffer\_size\_in\_bytes/512, 这个是哈希表最大的长度，超过就存不下了，幸运的是，需要恢复的数据页的个数不会超过这个值，因为buffer poll最多(数据库崩溃之前脏页的上线)只能存放buffer\_size\_in\_bytes/16KB个数据页，即使考虑压缩页，最多也只有buffer\_size\_in\_bytes/1KB个，此外关于这个哈希表内存分配的大小，可以参考bug#53122。flush list rbtree这个主要是为了加入插入脏页列表，InnoDB的flush list必须按照数据页的最老修改lsn(oldest\_modifcation)从小到大排序，在数据库正常运行时，可以通过log\_sys->mutex和log\_sys->log\_flush\_order\_mutex保证顺序，在崩溃恢复则没有这种保证，应用数据的时候，是从第一个元素开始遍历哈希表，不能保证数据页按照最老修改lsn(oldest\_modifcation)从小到大排序，这样就需要线性遍历flush\_list来寻找插入位置，效率太低，因此引入红黑树，加快查找插入的位置。
接着，从ib\_logfile0的头中读取checkpoint信息，主要包括checkpoint\_lsn和checkpoint\_no。由于InnoDB日志是循环使用的，且最少要有2个，所以ib\_logfile0一定存在，把checkpoint信息存在里面很安全，不用担心被删除。checkpoint信息其实会写在文件头的两个地方，两个checkpoint域轮流写。为什么要两个地方轮流写呢？假设只有一个checkpoint域，一直更新这个域，而checkpoint域有512字节(`OS_FILE_LOG_BLOCK_SIZE`)，如果刚好在写这个512字节的时候，数据库挂了，服务器也挂了(先不考虑硬件的原子写特性，早期的硬件没有这个特性)，这个512字节可能只写了一半，导致整个checkpoint域不可用。这样数据库将无法做崩溃恢复，从而无法启动。如果有两个checkpoint域，那么即使一个写坏了，还可以用另外一个尝试恢复，虽然有可能这个时候日志已经被覆盖，但是至少提高了恢复成功的概率。两个checkpoint域轮流写，也能减少磁盘扇区故障带来的影响。checkpoint\_lsn之前的数据页都已经落盘，不需要前滚，之后的数据页可能还没落盘，需要重新恢复出来，即使已经落盘也没关系，因为redo日志时幂等的，应用一次和应用两次都一样(底层实现: 如果数据页上的lsn大于等于当前redo日志的lsn，就不应用，否则应用。checkpoint\_no可以理解为checkpoint域写盘的次数，每次刷盘递增1，同时这个值取模2可以用来实现checkpoint\_no域的轮流写。正常逻辑下，选取checkpoint\_no值大的作为最终的checkpoint信息，用来做后续崩溃恢复扫描的起始点。
接着，使用checkpoint域的信息初始化recv\_sys结构体的一些信息后，就进入日志解析的核心函数`recv_group_scan_log_recs`，这个函数后续我们再分析，主要作用就是解析redo日志，如果内存不够了，就直接调用应用(`recv_apply_hashed_log_recs`)日志，然后再接着解析。如果需要应用的日志很少，就仅仅解析分发日志，到`recv_recovery_from_checkpoint_finish`函数中在应用日志。
接着，依据当前刷盘的数据页状态做一次checkpoint，因为在`recv_group_scan_log_recs`里可能已经应用部分日志了。至此`recv_recovery_from_checkpoint_start_func`函数结束。
在`recv_recovery_from_checkpoint_finish`函数中，如果srv\_force\_recovery设置正确，就开始调用函数`recv_apply_hashed_log_recs`应用日志，然后等待刷脏的线程退出(线程是崩溃恢复时临时启动的)，最后释放recv\_sys的相关资源以及hash\_table占用的内存。
至此，数据库前滚结束。接下来，我们详细分析一下redo日志解析函数以及redo日志应用函数的实现细节。

## redo日志解析函数

解析函数的最上层是`recv_group_scan_log_recs`，这个函数调用底层函数(`log_group_read_log_seg`)，按照RECV\_SCAN\_SIZE(64KB)大小分批读取。读取出来后，首先通过block\_no和lsn之间的关系以及日志checksum判断是否读到了日志最后(所以可以看出，并没一个标记在日志头标记日志的有效位置，完全是按照上述两个条件判断是否到达了日志尾部)，如果读到最后则返回(之前说了，即使数据库是正常关闭的，也要走崩溃恢复逻辑，那么在这里就返回了，因为正常关闭的checkpoint值一定是指向日志最后)，否则则把日志去头掐尾放到一个recv\_sys->buf中，日志头里面存了一些控制信息和checksum值，只是用来校验和定位，在真正的应用中没有用。在放到recv\_sys->buf之前，需要检验一下recv\_sys->buf有没有满(`RECV_PARSING_BUF_SIZE`，2M)，满了就报错(如果上一批解析有不完整的日志，日志解析函数不会分发，而是把这些不完整的日志留在recv\_sys->buf中，直到解析到完整的日志)。接下的事情就是从recv\_sys->buf中解析日志(`recv_parse_log_recs`)。日志分两种：single\_rec和multi\_rec，前者表示只对一个数据页进行一种操作，后者表示对一个或者多个数据页进行多种操作。日志中还包括对应数据页的space\_id，page\_no，操作的type以及操作的内容(`recv_parse_log_rec`)。解析出相应的日志后，按照space\_id和page\_no进行哈希(如果对应的表空间在内存中不存在，则表示表已经被删除了)，放到hash\_table里面(日志真正存放的位置依然在buffer pool)即可，等待后续应用。这里有几个点值得注意：

* 如果是multi\_rec类型，则只有遇到MLOG\_MULTI\_REC\_END这个标记，日志才算完整，才会被分发到hash\_table中。查看代码，我们可以发现multi\_rec类型的日志被解析了两次，一次用来校验完整性(寻找MLOG\_MULTI\_REC\_END)，第二次才用来分发日志，感觉这是一个可以优化的点。
* 目前日志的操作type有50多种，每种操作后面的内容都不一样，所以长度也不一样，目前日志的解析逻辑，需要依次解析出所有的内容，然后确定长度，从而定位下一条日志的开始位置。这种方法效率略低，其实可以在每种操作的头上加上一个字段，存储后面内容的长度，这样就不需要解析太多的内容，从而提高解析速度，进一步提高崩溃恢复速度，从结果看，可以提高一倍的速度(从38秒到14秒，详情可以参见bug#82937)。
* 如果发现checkpoint之后还有日志，说明数据库之前没有正常关闭，需要做崩溃恢复，因此需要做一些额外的操作(`recv_init_crash_recovery`)，比如在错误日志中打印我们常见的“Database was not shutdown normally!”和“Starting crash recovery.”，还要从double write buffer中检查是否发生了数据页半写，如果有需要恢复(`buf_dblwr_process`)，还需要启动一个线程用来刷新应用日志产生的脏页(因为这个时候buf\_flush\_page\_cleaner\_thread还没有启动)。最后还需要打开所有的表空间。。注意是所有的表。。。我们在阿里云RDS MySQL的运维中，常常发现数据库hang在了崩溃恢复阶段，在错误日志中有类似“Reading tablespace information from the .ibd files…”字样，这就表示数据库正在打开所有的表，然后一看表的数量，发现有几十甚至上百万张表。。。数据库之所以要打开所有的表，是因为在分发日志的时候，需要确定space\_id对应哪个ibd文件，通过打开所有的表，读取space\_id信息来确定，另外一个原因是方便double write buffer检查半写数据页。针对这个表数量过多导致恢复过慢的问题，MySQL 5.7做了优化，WL#7142， 主要思想就是在每次checkpoint后，在第一次修改某个表时，先写一个新日志mlog\_file\_name(包括space\_id和filename的映射)，来表示对这个表进行了操作，后续对这个表的操作就不用写这个新日志了，当需要崩溃恢复时候，多一次扫描，通过搜集mlog\_file\_name来确定哪些表被修改过，这样就不需要打开所有的表来确定space\_id了。
* 最后一个值得注意的地方是内存。之前说过，如果有太多的日志已经被分发，占用了太多的内存，日志解析函数会在适当的时候应用日志，而不是等到最后才一起应用。那么问题来了，使用了多大的内存就会出发应用日志逻辑。答案是：buffer\_pool\_size\_in\_bytes - 512 \* buffer\_pool\_instance\_num \* 16KB。由于buffer\_pool\_instance\_num一般不会太大，所以可以任务，buffer pool的大部分内存都被用来存放日志。剩下的那些主要留给应用日志时读取的数据页，因为目前来说日志应用是单线程的，读取一个日志，把所有日志应用完，然后就可以刷回磁盘了，不需要太多的内存。

## redo日志应用函数

应用日志的上层函数为`recv_apply_hashed_log_recs`(应用日志也可能在io\_helper函数中进行)，主要作用就是遍历hash\_table，从磁盘读取对每个数据页，依次应用哈希桶中的日志。应用完所有的日志后，如果需要则把buffer\_pool的页面都刷盘，毕竟空间有限。有以下几点值得注意：

* 同一个数据页的日志必须按照lsn从小到大应用，否则数据会被覆盖。只应用redo日志lsn大于page\_lsn的日志，只有这些日志需要重做，其余的忽略。应用完日志后，把脏页加入脏页列表，由于脏页列表是按照最老修改lsn(oldest\_modification)来排序的，这里通过引入一颗红黑树来加速查找插入的位置，时间复杂度从之前的线性查找降为对数级别。
* 当需要某个数据页的时候，如果发现其没有在Buffer Pool中，则会查看这个数据页周围32个数据页，是否也需要做恢复，如果需要则可以一起读取出来，相当于做了一次io合并，减少io操作(`recv_read_in_area`)。由于这个是异步读取，所以最终应用日志的活儿是由io\_helper线程来做的(`buf_page_io_complete`)，此外，为了防止短时间发起太多的io，在代码中加了流量控制的逻辑(`buf_read_recv_pages`)。如果发现某个数据页在内存中，则直接调用`recv_recover_page`应用日志。由此我们可以看出，InnoDB应用日志其实并不是单线程的来应用日志的，除了崩溃恢复的主线程外，io\_helper线程也会参与恢复。并发线程数取决于io\_helper中读取线程的个数。

执行完了redo前滚数据库，数据库的所有数据页已经处于一致的状态，undo回滚数据库就可以安全的执行了。数据库崩溃的时候可能有一些没有提交的事务或者已经提交的事务，这个时候就需要决定是否提交。主要分为三步，首先是扫描undo日志，重新建立起undo日志链表，接着是，依据上一步建立起的链表，重建崩溃前的事务，即恢复当时事务的状态。最后，就是依据事务的不同状态，进行回滚或者提交。

## undo日志回滚数据库

在`recv_recovery_from_checkpoint_start_func`之后，`recv_recovery_from_checkpoint_finish`之前，调用了`trx_sys_init_at_db_start`，这个函数做了上述三步中的前两步。
第一步在函数`trx_rseg_array_init`中处理，遍历整个undo日志空间(最多TRX\_SYS\_N\_RSEGS(128)个segment)，如果发现某个undo segment非空，就进行初始化(`trx_rseg_create_instance`)。整个每个undo segment，如果发现undo slot非空(最多TRX\_RSEG\_N\_SLOTS(1024)个slot)，也就行初始化(`trx_undo_lists_init`)。在初始化undo slot后，就把不同类型的undo日志放到不同链表中(`trx_undo_mem_create_at_db_start`)。undo日志主要分为两种：TRX\_UNDO\_INSERT和TRX\_UNDO\_UPDATE。前者主要是提供给insert操作用的，后者是给update和delete操作使用。之前说过，undo日志有两种作用，事务回滚时候用和MVCC快照读取时候用。由于insert的数据不需要提供给其他线程用，所以只要事务提交，就可以删除TRX\_UNDO\_INSERT类型的undo日志。TRX\_UNDO\_UPDATE在事务提交后还不能删除，需要保证没有快照使用它的时候，才能通过后台的purge线程清理。
第二步在函数`trx_lists_init_at_db_start`中进行，由于第一步中，已经在内存中建立起了undo\_insert\_list和undo\_update\_list(链表每个undo segment独立)，所以这一步只需要遍历所有链表，重建起事务的状态(`trx_resurrect_insert`和`trx_resurrect_update`)。简单的说，如果undo日志的状态是TRX\_UNDO\_ACTIVE，则事务的状态为TRX\_ACTIVE，如果undo日志的状态是TRX\_UNDO\_PREPARED，则事务的状态为TRX\_PREPARED。这里还要考虑变量srv\_force\_recovery的设置，如果这个变量值为非0，所有的事务都会回滚(即事务被设置为TRX\_ACTIVE)，即使事务的状态应该为TRX\_STATE\_PREPARED。重建起事务后，按照事务id加入到trx\_sys->trx\_list链表中。最后，在函数`trx_sys_init_at_db_start`中，会统计所有需要回滚的事务(事务状态为TRX\_ACTIVE)一共需要回滚多少行数据，输出到错误日志中，类似：5 transaction(s) which must be rolled back or cleaned up。InnoDB: in total 342232 row operations to undo的字样。
第三步的操作在两个地方被调用。一个是在`recv_recovery_from_checkpoint_finish`的最后，另外一个是在`recv_recovery_rollback_active`中。前者主要是回滚对数据字典的操作，也就是回滚DDL语句的操作，后者是回滚DML语句。前者是在数据库可提供服务之前必须完成，后者则可以在数据库提供服务(也即是崩溃恢复结束)之后继续进行(通过新开一个后台线程`trx_rollback_or_clean_all_recovered`来处理)。因为InnoDB认为数据字典是最重要的，必须要回滚到一致的状态才行，而用户表的数据可以稍微慢一点，对外提供服务后，慢慢恢复即可。因此我们常常在会发现数据库已经启动起来了，然后错误日志中还在不断的打印回滚事务的信息。事务回滚的核心函数是`trx_rollback_or_clean_recovered`，逻辑很简单，只需要遍历trx\_sys->trx\_list，按照事务不同的状态回滚或者提交即可(`trx_rollback_resurrected`)。这里要注意的是，如果事务是TRX\_STATE\_PREPARED状态，那么在InnoDB层，不做处理，需要在Server层依据binlog的情况来决定是否回滚事务，如果binlog已经写了，事务就提交，因为binlog写了就可能被传到备库，如果主库回滚会导致主备数据不一致，如果binlog没有写，就回滚事务。

## 崩溃恢复相关参数解析

\*\*innodb\_fast\_shutdown: \*\*
innodb\_fast\_shutdown = 0。这个表示在MySQL关闭的时候，执行slow shutdown，不但包括日志的刷盘，数据页的刷盘，还包括数据的清理(purge)，ibuf的合并，buffer pool dump以及lazy table drop操作(如果表上有未完成的操作，即使执行了drop table且返回成功了，表也不一定立刻被删除)。
innodb\_fast\_shutdown = 1。这个是默认值，表示在MySQL关闭的时候，仅仅把日志和数据刷盘。
innodb\_fast\_shutdown = 2。这个表示关闭的时候，仅仅日志刷盘，其他什么都不做，就好像MySQL crash了一样。
这个参数值越大，MySQL关闭的速度越快，但是启动速度越慢，相当于把关闭时候需要做的工作挪到了崩溃恢复上。另外，如果MySQL要升级，建议使用第一种方式进行一次干净的shutdown。

\*\*innodb\_force\_recovery: \*\*
这个参数主要用来控制InnoDB启动时候做哪些工作，数值越大，做的工作越少，启动也更加容易，但是数据不一致的风险也越大。当MySQL因为某些不可控的原因不能启动时，可以设置这个参数，从1开始逐步递增，知道MySQL启动，然后使用SELECT INTO OUTFILE把数据导出，尽最大的努力减少数据丢失。
innodb\_force\_recovery = 0。这个是默认的参数，启动的时候会做所有的事情，包括redo日志应用，undo日志回滚，启动后台master和purge线程，ibuf合并。检测到了数据页损坏了，如果是系统表空间的，则会crash，用户表空间的，则打错误日志。
innodb\_force\_recovery = 1。如果检测到数据页损坏了，不会crash也不会报错(`buf_page_io_complete`)，启动的时候也不会校验表空间第一个数据页的正确性(`fil_check_first_page`)，表空间无法访问也继续做崩溃恢复(`fil_open_single_table_tablespace`、`fil_load_single_table_tablespace`)，ddl操作不能进行(`check_if_supported_inplace_alter`)，同时数据库也被不能进行写入操作(`row_insert_for_mysql`、`row_update_for_mysql`等)，所有的prepare事务也会被回滚(`trx_resurrect_insert`、`trx_resurrect_update_in_prepared_state`)。这个选项还是很常用的，数据页可能是因为磁盘坏了而损坏了，设置为1，能保证数据库正常启动。
innodb\_force\_recovery = 2。除了设置1之后的操作不会运行，后台的master和purge线程就不会启动了(`srv_master_thread`、`srv_purge_coordinator_thread`等)，当你发现数据库因为这两个线程的原因而无法启动时，可以设置。
innodb\_force\_recovery = 3。除了设置2之后的操作不会运行，undo回滚数据库也不会进行，但是回滚段依然会被扫描，undo链表也依然会被创建(`trx_sys_init_at_db_start`)。srv\_read\_only\_mode会被打开。
innodb\_force\_recovery = 4。除了设置3之后的操作不会运行，ibuf的操作也不会运行(`ibuf_merge_or_delete_for_page`)，表信息统计的线程也不会运行(因为一个坏的索引页会导致数据库崩溃)(`info_low`、`dict_stats_update`等)。从这个选项开始，之后的所有选项，都会损坏数据，慎重使用。
innodb\_force\_recovery = 5。除了设置4之后的操作不会运行，回滚段也不会被扫描(`recv_recovery_rollback_active`)，undo链表也不会被创建，这个主要用在undo日志被写坏的情况下。
innodb\_force\_recovery = 6。除了设置5之后的操作不会运行，数据库前滚操作也不会进行，包括解析和应用(`recv_recovery_from_checkpoint_start_func`)。

## 总结

InnoDB实现了一套完善的崩溃恢复机制，保证在任何状态下(包括在崩溃恢复状态下)数据库挂了，都能正常恢复，这个是与文件系统最大的差别。此外，崩溃恢复通过redo日志这种物理日志来应用数据页的方法，给MySQL Replication带来了新的思路，备库是否可以通过类似应用redo日志的方式来同步数据呢？阿里云RDS MySQL团队在后续的产品中，给大家带来了类似的特性，敬请期待。

---

© 2019 - 2023 [Liangliang Lee](/cdn-cgi/l/email-protection#c1adadadf8f5f0f0f1f681a6aca0a8adefa2aeac).
Powered by [gin](https://github.com/gin-gonic/gin) and [hexo-theme-book](https://github.com/kaiiiz/hexo-theme-book).