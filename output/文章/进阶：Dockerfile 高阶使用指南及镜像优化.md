# 进阶：Dockerfile 高阶使用指南及镜像优化 

Source: https://learn.lianglianglee.com/%e6%96%87%e7%ab%a0/%e8%bf%9b%e9%98%b6%ef%bc%9aDockerfile%20%e9%ab%98%e9%98%b6%e4%bd%bf%e7%94%a8%e6%8c%87%e5%8d%97%e5%8f%8a%e9%95%9c%e5%83%8f%e4%bc%98%e5%8c%96.md

进阶：Dockerfile 高阶使用指南及镜像优化 



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

# 进阶：Dockerfile 高阶使用指南及镜像优化

### Dockerfile 高阶使用及新特性解读

通过之前的学习，我们已经知道 Dockerfile 是一种可用于镜像构建，具备特定语法的文本文件。而 Docker 自身在使用此文件进行构建镜像的过程中，遵循其固定的行为。

比如在上次 [Chat](https://gitbook.cn/gitchat/activity/5cd527e864de19331ba79278) 提到的**缓存**。

Docker 构建系统中，默认情况下为了加快构建的速度，会将构建过程中的每层都进行缓存，我们建议在编写 Dockerfile 的时候，将更新最为频繁的步骤写到最后面，以避免因为该步骤的内容变更，进而导致后续步骤的缓存失效（缓存的控制是 Docker 固定的行为，我们在之后的 Chat 中会进一步深入内部进行分析）。

而同时，我们通过深入到 Docker 镜像内部，发现了它内部的组织形式，对于镜像而言，它其实是使用配置元信息，将对应内容的层（layer）组织起来的一个集合。

那么在使用 Dockerfile 构建镜像的时候，除了上次 [Chat](https://gitbook.cn/gitchat/activity/5cd527e864de19331ba79278) 聊到的内容外，有哪些值得掌握的高级技巧呢？ 我们来正式开始本次 Chat 。

### 打开 BuildKit 支持

在上次 [Chat](https://gitbook.cn/gitchat/activity/5cd527e864de19331ba79278) 的最后，我们提到可以通过 BuildKit 以提高构建效率，这里我们来对它进行更加详细的解读和分析。

首先，我们知道 Docker 是一个典型的 C/S 架构模型，我们平时使用的 `docker` 命令，是它的 CLI 客户端，而它的服务端是 dockerd ，在 Linux 系统中，通常它是由 systemd 进行管理的，我们可以通过 `systemctl status docker` 查看当前 dockerd 的运行状态。

对于构建镜像而言，它同样是需要将待构建的内容（我们称之为 context），发送给 dockerd，并由 dockerd 的特定模块最终完成构建。

#### builder

这里我们需要引入一个概念 **builder** .

builder 就是上面提到的特定模块，也就是说构建内容 context 是由 Docker CLI 发送给 dockerd；并最终由 builder 完成构建。

![enter image description here](assets/7141ec30-830d-11e9-8eb9-49b38b06f9d6.jpg)

在 `docker` 的顶级命令中，我们可以看到有一个 `builder` 的命令组。它有一个子命令 `prune` 用于清理所有构建过程中的缓存。

以下是 Docker 18.09 的输出信息。

```
/ # docker builder

Usage:  docker builder COMMAND

Manage builds

Commands:
  prune       Remove build cache

Run 'docker builder COMMAND --help' for more information on a command.

```

而在 Docker 19.03 中，它新增了一个子命令：

```
/ # docker builder

Usage:  docker builder COMMAND

Manage builds

Commands:
  build       Build an image from a Dockerfile
  prune       Remove build cache

Run 'docker builder COMMAND --help' for more information on a command.

```

这里新增的这个 `build` 子命令，其实就是我们平时使用的 `docker build` 或者是 `docker image build`，现在将它放到 builder 的子目录下也是为了凸显 builder 的概念。

builder 其实很早就存在于 Docker 当中了，我们之前在使用或者说默认在使用的就是 builder 的 v1 版本（在 Docker 内部也将它的版本号定为 1），但是由于它太久了，有一些功能缺失和不足，由此诞生了 builder 的 v2 版本，该项目被称之为 BuildKit 。

#### [BuildKit](https://github.com/moby/buildkit)

BuildKit 的产生主要是由于 v1 版本的 builder 的性能，存储管理和扩展性方面都有不足（毕竟它已经产生了很久，而且近些年 Docker 火热，问题也就逐步暴露出来了）, 所以它的重点也在于解决这些问题，关键的功能列在下面：

* 支持自动化的垃圾回收
* 可扩展的构建格式
* 并发依赖解决
* 高效的缓存系统
* 插件化的架构

这些功能我们暂且略过，先回到我们的主线上来。

BuildKit 在 Docker v18.06 版本之后可通过 `export DOCKER_BUILDKIT=1` 环境变量来设置是否启用。对于 Docker v18.06 需要将 dockerd 也以实现性模式运行。即，修改 /etc/docker/daemon.json 文件，增加 `"experimental": true` 配置，然后使用 `systemctl restart docker` 重启 dockerd 。

如果将 /etc/docker/daemon.json 文件中添加以下配置：

```
{
  "experimental": true,
  "features": {
    "buildkit": true
  }
}

```

则会默认使用 BuildKit 进行构建，就不再需要指定环境了。

#### 小结

* 在上面的内容中，我们知道了 Docker 是 C/S 架构，而我们通常使用的 `docker` 命令便是它的 CLI 客户端，服务端是 dockerd 通常由 systemd 进行管理；
* 我们介绍了一个概念 builder，它是 Docker 构建系统中的实际执行者；用于将构建的上下文 context 按照 Dockerfile 的描述最终生成 Docker 镜像（image）;
* BuildKit 是 v2 版本的 builder ；
* 我们可以通过增加 `export DOCKER_BUILDKIT=1` 的环境变量，或是修改 dockerd 的配置文件来临时启用或者默认启用 BuildKit 作为 builder。

我们来体验一下开启 BuildKit 的镜像构建：

```
(MoeLove) ➜  ~ docker build -t local/spring-boot:buildkit https://github.com/tao12345666333/spring-boot-hello-world.git
[+] Building 0.2s (0/1)
[+] Building 0.6s (0/1) 
...
[+] Building 6.4s (0/1)
 => [internal] load git source https://github.com/tao12345666333/spring-boot-hello-world.git                6.4s 
 => => # 已初始化空的 Git 仓库于 /var/lib/docker/overlay2/xieo69jwu3qd18uqmuwa6er9l/diff/
         898cc478c6bbec5dab019a36fdfdd2dd172cee9erefs/heads/master
[+] Building 394.0s (12/12) FINISHED
 => [internal] load git source https://github.com/tao12345666333/spring-boot-hello-world.git                6.4s 
 => [internal] load metadata for docker.io/library/openjdk:8-jre-alpine                                     3.6s
 => [internal] load metadata for docker.io/library/maven:3.6.1-jdk-8-alpine                                 3.3s 
 => CACHED [stage-2 1/2] FROM docker.io/library/openjdk:8-jre-alpine@sha256:f362b165b870ef129cbe730f29065f  0.0s
 => => resolve docker.io/library/openjdk:8-jre-alpine@sha256:f362b165b870ef129cbe730f29065ff37399c0aa8bcab  0.0s
 => [builder 1/6] FROM docker.io/library/maven:3.6.1-jdk-8-alpine@sha256:16691dc7e18e5311ee7ae38b40dcf98e  14.3s
 => => resolve docker.io/library/maven:3.6.1-jdk-8-alpine@sha256:16691dc7e18e5311ee7ae38b40dcf98ee1cfe4a48  0.0s
 => => sha256:e4ef40f7698347c89ee64b2e5c237d214cae777f33735c52039824eb44feb796 2.18MB / 2.18MB              2.7s
...
 => => extracting sha256:c2274a1a0e2786ee9101b08f76111f9ab8019e368dce1e325d3c284a0ca33397                   0.7s
 => [builder 2/6] WORKDIR /app                                                                              0.3s
 => [builder 3/6] COPY pom.xml /app/                                                                        0.0s
 => [builder 4/6] RUN mvn dependency:go-offline                                                           352.4s
 => [builder 5/6] COPY src /app/src                                                                         0.1s
 => [builder 6/6] RUN mvn -e -B package                                                                    16.3s
 => [stage-2 2/2] COPY --from=builder /app/target/gs-spring-boot-0.1.0.jar /                                0.1s
 => exporting to image                                                                                      0.1s
 => => exporting layers                                                                                     0.1s
 => => writing image sha256:82f3748307e8c43af8e28fc5c303b89973e22ba0d2e85c1b43648a5f0c332219                0.0s
 => => naming to docker.io/local/spring-boot:buildkit                                                       0.0s

```

以上便是一个开启了 BuildKit 的镜像构建过程，可以看到与我们之前默认的 builder 的输出之类的都不一样，这里暂不展开了，我们开始下一步的学习。

### 构建历史

我们仍然使用上次 [Chat](https://gitbook.cn/gitchat/activity/5cd527e864de19331ba79278) 中的[例子](https://github.com/tao12345666333/spring-boot-hello-world.git)：一个 Spring Boot 的项目，同样的本次 Chat 中并不涉及 Spring Boot 的任何知识。只需要知道对于这个项目而言， 需要先安装依赖、构建，才能运行。

```
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ ls -l 
总用量 20
-rw-rw-r--. 1 tao tao    0 5月  15 06:52 Dockerfile
drwxrwxr-x. 2 tao tao 4096 5月  15 06:54 docs
-rw-rw-r--. 1 tao tao 1992 5月  15 06:33 pom.xml
-rw-rw-r--. 1 tao tao   89 5月  15 06:50 README.md
drwxrwxr-x. 4 tao tao 4096 5月  15 06:33 src
drwxrwxr-x. 9 tao tao 4096 5月  15 06:52 target

```

我们来看下该项目的 Dockerfile 的内容：

```
FROM maven:3.6.1-jdk-8-alpine AS builder

WORKDIR /app

COPY pom.xml /app/
RUN mvn dependency:go-offline
COPY src /app/src
RUN mvn -e -B package

FROM builder AS dev

RUN apk add --no-cache vim

FROM openjdk:8-jre-alpine

COPY --from=builder /app/target/gs-spring-boot-0.1.0.jar /

CMD [ "java", "-jar", "/gs-spring-boot-0.1.0.jar" ]

```

我们以此 Dockerfile 来构建镜像，这里我增加了 `-q` 参数忽略掉默认的输出。

```
(MoeLove) ➜  spring-boot-hello-world git:(master) docker build -q -t local/spring-boot:1 .
sha256:01e4898d1141763400d39111609425ba6232b8bf42f46a6033fdb2b7306dc75b 

```

可以看到镜像已经构建成功了，这里我们来介绍一个新的命令 `docker image history`，对新构建的镜像执行此命令：

```
(MoeLove) ➜  spring-boot-hello-world git:(master) docker image history local/spring-boot:1
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
01e4898d1141        292 years ago       CMD ["java" "-jar" "/gs-spring-boot-0.1.0.ja…   0B                  buildkit.dockerfile.v0
<missing>           2 days ago          COPY /app/target/gs-spring-boot-0.1.0.jar / …   18.2MB              buildkit.dockerfile.v0
<missing>           2 weeks ago         /bin/sh -c set -x  && apk add --no-cache   o…   79.4MB              
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV JAVA_ALPINE_VERSION=8…   0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV JAVA_VERSION=8u212       0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV PATH=/usr/local/sbin:…   0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV JAVA_HOME=/usr/lib/jv…   0B                  
<missing>           2 weeks ago         /bin/sh -c {   echo '#!/bin/sh';   echo 'set…   87B
<missing>           2 weeks ago         /bin/sh -c #(nop)  ENV LANG=C.UTF-8             0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6a…   5.53MB

```

可以看到我们镜像的构建记录（以逆序排列），最上面的部分是我们多阶段构建中的。

```
COPY --from=builder /app/target/gs-spring-boot-0.1.0.jar /

CMD [ "java", "-jar", "/gs-spring-boot-0.1.0.jar" ]

```

这两步所对应的内容。

而下面的部分，则是我们的基础镜像 `openjdk:8-jre-alpine` 的构建记录。我们的操作基本都可以在 history 中看到。

#### 构建历史的不安全性

假如，我们的项目在构建过程当中，需要连接远端的数据库获取对应的信息（比如：获取某个特定的配置），之后才可以进行构建，我们通常情况下会如何去做呢？

* 将密码硬编码写入代码中，如果使用此方法，当密码变更的时候，便需要修改代码才能支持，并且镜像分发的时候，会造成信息泄漏，导致安全问题；
* 通过环境变量的方式构建，相对灵活，比较容易满足需求。

这里我们对 Dockerfile 做一点小改变，比如：我们使用 ENV 将密码通过环境变量的方式注入到镜像中。

```
# 以下省略了基础镜像的构建记录
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ docker build -q -t local/spring-boot:2 .                    
sha256:2f85141a35c386bbeac0ba77acd470025682bebc7da9eb204295ff8fafb6e0a8                                         
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ docker image history local/spring-boot:2                    
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
2f85141a35c3        292 years ago       CMD ["java" "-jar" "/gs-spring-boot-0.1.0.ja…   0B                  buildkit.dockerfile.v0
<missing>           292 years ago       ENV CACHE_PASSWD=moelove                        0B                  buildkit.dockerfile.v0
<missing>           2 days ago          COPY /app/target/gs-spring-boot-0.1.0.jar / …   18.2MB              buildkit.dockerfile.v0
<missing>           2 weeks ago         /bin/sh -c set -x  && apk add --no-cache   o…   79.4MB 
...

```

很明显，刚才增加的 ENV 可以直接通过 docker history/docker image history 看到。 **不建议真的这样做**。

由此，得出了我们的第一个结论，**Docker 镜像的构建历史是不安全的，通过 ENV 设置的信息可在 history 中看到**。

这也引出了我们的第一个问题：**Docker 镜像的构建记录是可查看的，如何管理构建过程中需要的密码/密钥等敏感信息？**

#### 高阶特性：密码管理

为了应对类似前面这样的问题，当开启 BuildKit 时，我们可以使用高阶用法，即：Dockerfile 的实验特性。

Dockerfile 的实验特性，通过给它的顶部添加 `# syntax = docker/dockerfile:experimental` 来实现，这也是 BuildKit 扩展性的一种表现形式。

具体用法如下：

```
# syntax = docker/dockerfile:experimental

COPY fetch_remote_data.sh .
RUN --mount=type=secret,id=moelove,target=/cache_builder,required ./fetch_remote_data.sh

```

然后通过以下命令进行构建:

```
docker build --secret id=moelove,src=./secret -t local/spring-boot:4 .

```

构建成功后，我们来看下 history 的记录：

```
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ docker history local/spring-boot:4        
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
b5fcff644568        292 years ago       CMD ["java" "-jar" "/gs-spring-boot-0.1.0.ja…   0B                  buildkit.dockerfile.v0
<missing>           2 minutes ago       RUN /bin/sh -c ./fetch_remote_data.sh # buil…   19B                 buildkit.dockerfile.v0
<missing>           2 minutes ago       COPY fetch_remote_data.sh . # buildkit          37B                 buildkit.dockerfile.v0
<missing>           2 days ago          COPY /app/target/gs-spring-boot-0.1.0.jar / …   18.2MB              buildkit.dockerfile.v0
...

```

并没有在记录中看到我们的密码，同时，当我们用该镜像启动一个容器后会发现，刚才挂载进去的文件变成空的了。

#### 高阶特性：密钥管理

另一种很常见的情况是，在构建过程中，可能需要 `git clone` 一个私有仓库，或者是 `ssh` 到某个远程主机上获取一些数据之类的操作。

对于这种情况，我们也可以使用高阶特性, （这里就不在上面例子的基础上来写了，写了一个新的 Dockerfile）。

```
# syntax = docker/dockerfile:experimental
FROM alpine

# 安装必要的包
RUN apk add --no-cache git openssh-client

# 创建必要的目录 .ssh 由于要使用 ssh 连接，所以需要使用 ssh-keyscan 先获取 public SSH host key
# 当然也可以给 .ssh/config 写配置文件来跳过验证，但容易带来安全问题，不推荐
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

# clone 私有项目仓库，并创建分支
RUN --mount=type=ssh,required git clone [email protected]:tao12345666333/moe.git \
        && cd moe \
        && git checkout -b release

```

**注意** ：使用此功能的时候，需要使用 [`ssh-agent(1)`](https://linux.die.net/man/1/ssh-agent) 进行认证代理，所以需要提前安装。

构建方式如下：

```
(MoeLove) ➜  d eval $(ssh-agent)
Agent pid 28184
(MoeLove) ➜  d ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/tao/.ssh/id_rsa: 
Identity added: /home/tao/.ssh/id_rsa (/home/tao/.ssh/id_rsa)
(MoeLove) ➜  d docker build --ssh=default -t local/ssh .
[+] Building 0.5s (10/10) FINISHED                                                                        
 => [internal] load build definition from Dockerfile                                                 0.1s
 => => transferring dockerfile: 96B                                                                  0.0s
 => [internal] load .dockerignore                                                                    0.1s
 => => transferring context: 2B                                                                      0.0s
 => resolve image config for docker.io/docker/dockerfile:experimental                                0.0s
 => CACHED docker-image://docker.io/docker/dockerfile:experimental                                   0.0s
 => [internal] load metadata for docker.io/library/alpine:latest                                     0.0s
 => [1/4] FROM docker.io/library/alpine                                                              0.0s
 => CACHED [2/4] RUN apk add --no-cache git openssh-client                                           0.0s
 => CACHED [3/4] RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts         0.0s
 => CACHED [4/4] RUN --mount=type=ssh,required git clone [email protected]:tao12345666333/moe.git       0.0s
 => exporting to image                                                                               0.0s
 => => exporting layers                                                                              0.0s
 => => writing image sha256:35d3ded5595a48de50054121feed13ebadf9b5e73b6cefeeba4215e1a20a20fd         0.0s
 => => naming to docker.io/local/ssh

```

我们使用该镜像启动一个容器：

```
(MoeLove) ➜  d docker run --rm -it local/ssh
/ # du -sh moe/
108.0K  moe/
/ # ls -al ~/.ssh/*
-rw-r--r--    1 root     root           788 May 30 06:35 /root/.ssh/known_hosts

```

可以看到，代码仓库已经成功的 clone 下来了。同时，在 `~/.ssh` 目录内也并没有保留任何我们公/私钥的信息。

```
(MoeLove) ➜  d docker history local/ssh
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
35d3ded5595a        35 minutes ago      RUN /bin/sh -c git clone [email protected]:tao1…   16.9kB              buildkit.dockerfile.v0
<missing>           35 minutes ago      RUN /bin/sh -c mkdir -p -m 0700 ~/.ssh && ss…   392B                buildkit.dockerfile.v0
<missing>           36 minutes ago      RUN /bin/sh -c apk add --no-cache git openss…   20.8MB              buildkit.dockerfile.v0
<missing>           2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B                  
<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6a…   5.53MB      

```

镜像的 history 中也没有任何额外的敏感信息。

如果没有运行 `ssh-agent` 或者是密钥没有 ssh-add 添加进去， 你就会看到类似下面的问题：

```
(MoeLove) ➜  d docker build --no-cache --ssh=default -t local/ssh .
[+] Building 11.9s (9/9) FINISHED
 => [internal] load .dockerignore                                                                    0.1s
 => => transferring context: 2B                                                                      0.0s
 => [internal] load build definition from Dockerfile                                                 0.1s
 => => transferring dockerfile: 96B                                                                  0.0s
 => resolve image config for docker.io/docker/dockerfile:experimental                                0.0s
 => CACHED docker-image://docker.io/docker/dockerfile:experimental                                   0.0s
 => [internal] load metadata for docker.io/library/alpine:latest                                     0.0s
 => CACHED [1/4] FROM docker.io/library/alpine                                                       0.0s
 => [2/4] RUN apk add --no-cache git openssh-client                                                  5.5s
 => [3/4] RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts                3.0s
 => ERROR [4/4] RUN --mount=type=ssh,required git clone [email protected]:tao12345666333/moe.git        2.9s
------
 > [4/4] RUN --mount=type=ssh,required git clone [email protected]:tao12345666333/moe.git         && cd moe         && git checkout -b release:                                                                        
#9 0.691 Cloning into 'moe'...
#9 1.923 Warning: Permanently added the RSA host key for IP address '192.30.253.112' to the list of known hosts.                                                                                                    
#9 2.842 [email protected]: Permission denied (publickey).
#9 2.843 fatal: Could not read from remote repository.
#9 2.843
#9 2.843 Please make sure you have the correct access rights
#9 2.843 and the repository exists.
------
rpc error: code = Unknown desc = executor failed running [/bin/sh -c git clone [email protected]:tao12345666333/moe.git         && cd moe         && git checkout -b release]: exit code: 128

```

#### 小结

在上面的内容中，我们学习到了通过 `docker image history` 可以查看镜像的构建历史，但构建历史是透明的，凡是可以拿到该镜像的人均可查看到其构建历史；所以它是不安全的。

尤其是当我们通过 ENV 或者 RUN 指令等，将密码/配置信息等传递进去，或者是将自己的私钥之类的文件拷贝到镜像中， **这些操作都是不安全的，不应该这样使用** ，在启用 BuildKit 之后，我们可以通过使用新的实验性语法做到更安全的操作。

实验性语法是在 Dockerfile 的头部增加了一个表示当前语法规则的 `# syntax = docker/dockerfile:experimental` （事实上，我们将它称之为 frontend）它其实是一个真实存在的 Docker 镜像，在构建过程中，会将它拉取下来使用，这里的详细内容我们可以之后对 frontend 详解的时候再进行讨论。

在 Dockerfile 中通过使用 `RUN --mount=type=ssh` 或是 `RUN --mount=type=secret` 的方式，配合 `docker build` 时，传递 `--ssh` 或 `--secret` 参数即可使用。可参考[官方文档](https://docs.docker.com/develop/develop-images/build_enhancements/)了解更多。

这是一种**推荐**且**安全**的处理方式，虽然就结果而言这并不是唯一的解决方案，但我还是推荐你及时升级 `Docker` 并使用这种方式。

### Docker 19.03 构建系统解读

Docker 19.03 在（2019/05/30 发布了 beta5 版本）正式版也将在不久之后会发布。相比其他版本而言，19.03 在构建系统方面的变化是比较大的，虽然一些特性是 18.09 时就已经增加的。

#### builder cache 管理

在 18.09 之前，有一个命令 `docker system prune` 可以清除所有的停止状态的容器、所有未被使用的网络、所有 dangling 状态的镜像以及所有 dangling 状态的构建缓存。

但有时候你可能并不想把他们都删掉。在 18.09 版本中，新增了 `docker builder prune` 命令，该命令可以只删除所有的 BuildKit 的构建缓存。

同样的，之前 builder 产生的构建缓存是需要手动进行清理的，否则磁盘空间将会浪费很多。在 18.09 之后也为 BuildKit 增加了可配置的垃圾回收策略。

具体配置方式是（Docker 19.03 中）在 /etc/docker/daemon.json 中写入以下内容：

```
{
  "experimental": true,
  "features": {
    "buildkit": true
  },
  "builder": {
    "gc": {
      "enabled": true,
      "defaultKeepStorage": "20GB"
    }
  }
}

```

以上配置中 experimental 表示是否开启实验性功能，features 中是选择开启 BuildKit 支持，builder 中的 gc 则表示控制垃圾回收的策略，上面配置的含义是：保留 20G 的缓存，超出则会进行清理。

#### 多实例 builder 管理

我们知道 Docker CLI 是提供插件支持的，并且开发一个插件也并不难，不过这不是今天的重点，之后开 Chat 再聊。

Docker 19.03 会提供两个主要的插件 app 和 buildx；buildx 就是这一小节的主角。

如果你安装了 Docker 19.03 但你输入 `docker buildx` 发现报错时，那说明你的 Docker 还尚未安装 buildx，可以使用下面的命令进行安装：

```
(MoeLove) ➜  export DOCKER_BUILDKIT=1
(MoeLove) ➜  docker build --platform=local -o . git://github.com/docker/buildx
(MoeLove) ➜  mkdir -p ~/.docker/cli-plugins/
(MoeLove) ➜  mv buildx ~/.docker/cli-plugins/docker-buildx

```

完成后，执行 `docker buildx` 就会看到以下内容的输出：

```
(MoeLove) ➜  ~ docker buildx 

Usage:  docker buildx COMMAND

Build with BuildKit

Management Commands:
  imagetools  Commands to work on images in registry

Commands:
  bake        Build from a file
  build       Start a build
  create      Create a new builder instance
  inspect     Inspect current builder instance
  ls          List builder instances
  rm          Remove a builder instance
  stop        Stop builder instance
  use         Set the current builder instance
  version     Show buildx version information 

Run 'docker buildx COMMAND --help' for more information on a command.

```

buildx 主要作用其实是为了扩展 BuildKit 的能力，包括多 builder 实例的管理；多 node 构建以支持扩平台构建等能力。

我们主要来看下如何使用它，深入的分析之后再进行讨论。

我们来演示多实例构建。首先需要创建一个 builder 实例。

```
(MoeLove) ➜  docker buildx create --name d1809 172.17.0.3
d1809                                               
(MoeLove) ➜  docker buildx ls
NAME/NODE DRIVER/ENDPOINT       STATUS   PLATFORMS
d1809     docker-container
  d18090  tcp://172.17.0.3:2375 inactive
d1903 *   docker-container
  d19030  tcp://172.17.0.2:2375 running  linux/amd64
default   docker
  default default               running  linux/amd64

```

`docker buildx create` 通过 `--name` 来指定 builder 的名称，最后跟的是 host/IP 地址，默认使用 2375 端口。

如果要使用新创建的 builder 需要先通过 `docker buildx use` 命令来进行切换，当前在使用的 builder 通过 `ls` 命令的时候会带有一个 `*` 标记。当然你也可能注意到了它当前的状态是 inactive，这是因为只有当它真正开始构建任务了或者是执行过构建任务了 agent 才会启动，将它注册回来。

```
(MoeLove) ➜  ~ docker buildx use d1809
(MoeLove) ➜  ~ docker buildx ls
NAME/NODE DRIVER/ENDPOINT       STATUS   PLATFORMS
d1809 *   docker-container               
  d18090  tcp://172.17.0.3:2375 inactive 
d1903     docker-container               
  d19030  tcp://172.17.0.2:2375 running  linux/amd64
default   docker                         
  default default               running  linux/amd64

```

接下来还是以前面的 Spring Boot 的项目为例进行构建：

```
(MoeLove) ➜  spring-boot-hello-world git:(master) docker buildx build --load -t remote/spring-boot:1 .
[+] Building 31.1s (6/14)                                                                                       
[+] Building 686.6s (16/16) FINISHED                                                                            
 => [internal] booting buildkit                                                                            21.2s
 => => pulling image moby/buildkit:master                                                                  20.7s
 => => creating container buildx_buildkit_d18090                                                            0.5s
 => => unpacking docker.io/library/openjdk:8-jre-alpine@sha256:f362b165b870ef129cbe730f29065ff37399c0aa8bc  2.2s
 => [builder 2/6] WORKDIR /app                                                                              0.0s
 => [builder 3/6] COPY pom.xml /app/                                                                        0.1s
 => [builder 4/6] RUN mvn dependency:go-offline                                                           596.4s
 => [builder 5/6] COPY src /app/src                                                                         0.2s
 => [builder 6/6] RUN mvn -e -B package                                                                    25.3s
 => [stage-2 2/2] COPY --from=builder /app/target/gs-spring-boot-0.1.0.jar /                                0.2s
 => exporting to oci image format                                                                           2.3s
 => => exporting layers                                                                                     1.3s
 => => exporting manifest sha256:f5af6ad923434c4d7d2d6f94f095ccacfe6983cec592de6b8a0a3af37206686a           0.0s
 => => exporting config sha256:644867602b8a4a5162dee8534378e3dab28807f593759c6b25bcf16492d807bc             0.0s
 => => sending tarball                                                                                      0.9s
 => importing to docker                                                                                     0.3s
(MoeLove) ➜  spring-boot-hello-world git:(master) docker image ls remote/spring-boot                            
REPOSITORY           TAG                 IMAGE ID            CREATED              SIZE                          
remote/spring-boot   1                   644867602b8a        About a minute ago   103MB

```

镜像构建成功了。**注意** 这里给 `docker buildx build` 命令传递了 `--load` 参数，表示我们要将构建好的镜像加载到我们现在在用的 dockerd 当中。

此时再查看 builder 的状态：

```
(MoeLove) ➜  spring-boot-hello-world git:(master) docker buildx ls
NAME/NODE DRIVER/ENDPOINT       STATUS  PLATFORMS
d1809 *   docker-container
  d18090  tcp://172.17.0.3:2375 running linux/amd64
d1903     docker-container
  d19030  tcp://172.17.0.2:2375 running linux/amd64
default   docker
  default default               running linux/amd64

```

可以看到它状态已经上报回来了，处于了 running 状态了。

我们到这个 builder 实际对应的机器上查看该机器上容器的状态：

```
/ # docker ps
CONTAINER ID        IMAGE                  COMMAND             CREATED             STATUS              PORTS               NAMES
ff4a9e18658e        moby/buildkit:master   "buildkitd"         About an hour ago   Up About an hour                        buildx_buildkit_d18090

```

可以看到实际上是在该机器的 Docker 中运行了一个 BuildKit 的后端容器，以此来进行构建相关的操作。

当然，buildx 还有很多特性，比如可以构建多架构平台的镜像等。可以通过[官方文档](https://github.com/docker/buildx/blob/master/README.md)对它进一步了解。

#### 小结

通过这一小节，我们了解到在 Docker 19.03 版本中，我们可以通过 `docker builder prune` 清理构建缓存；并且可以通过给 /etc/docker/daemon.json 中写配置的方式来开启构建缓存的自动垃圾回收机制，以减轻磁盘压力。

buildx 是 Docker 的一个 CLI 插件，默认安装完 19.03 后将会同时安装它，当然你也可以手动进行安装。我们通过 buildx 可以进行多个 builder 实例的管理，通过这种方式，可以将很多机器组成一个集群来分担构建压力，或者是分担不同架构的构建任务等。

### 发现并优化镜像大小 dive

镜像的构建系统我们了解的差不多了，我们再聊聊如何发现，并优化镜像大小。这里分两个部分，其一是，发现；其二是，优化。

#### 发现

首先推荐一个工具 [dive](https://github.com/wagoodman/dive) ; 通过上次的 Chat 我们已经知道了镜像的组成和结构，dive 是一个命令行工具，使用它可以浏览 Docker 镜像每层的内容，以此来发现我们镜像中是否有什么不需要的东西存在。

关于 dive 这里不做过多介绍了，该项目的文档中介绍还是比较详细的，我们可以用它来分析下刚才我们构建成功的镜像：

![enter image description here](assets/2f5601d0-830d-11e9-a8d7-c164a8393e9a.jpg)

第二种方法，则是比较一般的，通过之前介绍的 `docker image history` 来查看构建记录和每层的大小，以此来观察是否有非必要的操作之类的。

#### 优化

我们对前面所举例中的 Spring Boot 项目的 Dockerfile 做点小改动：

```
FROM maven:3.6.1-jdk-8-alpine AS builder

WORKDIR /app

COPY pom.xml /app/
RUN mvn dependency:go-offline
COPY src /app/src
RUN mvn -e -B package

FROM builder AS dev

RUN apk add --no-cache vim

FROM openjdk:8-jre-alpine

COPY --from=builder /app/target/gs-spring-boot-0.1.0.jar /

# 增加两句完全没必要的操作，仅做演示
COPY --from=builder /app/target/gs-spring-boot-0.1.0.jar /tmp/
RUN rm /tmp/gs-spring-boot-0.1.0.jar

CMD [ "java", "-jar", "/gs-spring-boot-0.1.0.jar" ]

```

给它增加了两句完全没有必要的操作，现在构建该镜像。

```
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ docker image ls remote/spring-boot  
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
remote/spring-boot   2                   11559170c3fd        7 minutes ago       121MB
remote/spring-boot   1                   644867602b8a        About an hour ago   103MB

```

可以看到使用上面修改后的 Dockerfile 构建的镜像比之前的镜像大了 18M；我们之前也讲过了，镜像是层的叠加，后面操作删掉的文件，并不会减少镜像的体积。

**那我们如何在不修改 Dockerfile 的情况下让镜像体积变小呢？答案就在构建系统上。**

我们可以通过给 `docker build` 传递 `--squash` 的参数，来将镜像的层进行合并。

```
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ docker build --squash -t remote/spring-boot:3 .             
[+] Building 2.5s (16/16) FINISHED                                                                 
...
 => exporting to image                                                                                      0.0s
 => => exporting layers                                                                                     0.0s
 => => writing image sha256:2d5ba7eb86d2ad5594f82a896637c91137d150dab61fe8dc3acbdfcd164f6686                0.0s
 => => naming to docker.io/remote/spring-boot:3                                                             0.0s

```

查看构建好的镜像大小：

```
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ docker image ls remote/spring-boot
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
remote/spring-boot   3                   a2c1e139697b        5 seconds ago       103MB
remote/spring-boot   2                   11559170c3fd        12 minutes ago      121MB
remote/spring-boot   1                   644867602b8a        About an hour ago   103MB

```

可以看到镜像的体积又恢复了正常，这表示我们对之前层的删除操作生效了。我们来看看构建历史：

```
(MoeLove) ➜  spring-boot-hello-world git:(master) ✗ docker image history remote/spring-boot:3                   
IMAGE               CREATED              CREATED BY                                      SIZE                COMMENT
a2c1e139697b        About a minute ago                                                   103MB               create new from sha256:2d5ba7eb86d2ad5594f82a896637c91137d150dab61fe8dc3acbdfcd164f6686                             
<missing>           292 years ago        CMD ["java" "-jar" "/gs-spring-boot-0.1.0.ja…   0B                  buildkit.dockerfile.v0
<missing>           About a minute ago   RUN /bin/sh -c rm /tmp/gs-spring-boot-0.1.0.…   0B                  buildkit.dockerfile.v0
<missing>           About a minute ago   COPY /app/target/gs-spring-boot-0.1.0.jar /t…   0B                  buildkit.dockerfile.v0
<missing>           3 days ago           COPY /app/target/gs-spring-boot-0.1.0.jar / …   0B                  buildkit.dockerfile.v0
<missing>           2 weeks ago          /bin/sh -c set -x  && apk add --no-cache   o…   0B                     
<missing>           2 weeks ago          /bin/sh -c #(nop)  ENV JAVA_ALPINE_VERSION=8…   0B                     
<missing>           2 weeks ago          /bin/sh -c #(nop)  ENV JAVA_VERSION=8u212       0B                     
<missing>           2 weeks ago          /bin/sh -c #(nop)  ENV PATH=/usr/local/sbin:…   0B                     
<missing>           2 weeks ago          /bin/sh -c #(nop)  ENV JAVA_HOME=/usr/lib/jv…   0B                     
<missing>           2 weeks ago          /bin/sh -c {   echo '#!/bin/sh';   echo 'set…   0B                     
<missing>           2 weeks ago          /bin/sh -c #(nop)  ENV LANG=C.UTF-8             0B                     
<missing>           2 weeks ago          /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B                     
<missing>           2 weeks ago          /bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6a…   0B 

```

可以看到之前的每层大小都已经变成了 0，这是因为把所有的层都合并到了最终的镜像上去了。

**特别注意：** `--squash` 虽然在 1.13.0 版本中就已经加入了 Docker 中，但他至今仍然是实验形式；所以你需要按照我在本篇文章开始部分的介绍那样，打开实验性功能的支持。

但直接传递 `--squash` 的方式，相对来说足够的简单，也更安全。

### 总结

通过本次 Chat 我们学习到了关于 Docker builder 的概念，以及了解到了下一代版本的 BuildKit；学习了 Docker 19.03 中多实例的构建，以及对构建缓存的垃圾回收配置等；学习了 Dockerfile 的高阶特性，并通过这些特性来管理密码和密钥等信息；学习了如何发现并优化镜像的体积。

以上内容中虽然没有具体到它们的全部功能，也没有深入到源码级的分析，但已经涵盖了 Docker 构建系统的最新特性，希望能对你有所帮助。

---

© 2019 - 2023 [Liangliang Lee](/cdn-cgi/l/email-protection#137f7f7f2a272222232453747e727a7f3d707c7e).
Powered by [gin](https://github.com/gin-gonic/gin) and [hexo-theme-book](https://github.com/kaiiiz/hexo-theme-book).