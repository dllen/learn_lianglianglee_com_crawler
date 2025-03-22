# 漫画讲解 git rebase VS git merge 

Source: https://learn.lianglianglee.com/%e6%96%87%e7%ab%a0/%e6%bc%ab%e7%94%bb%e8%ae%b2%e8%a7%a3%20git%20rebase%20VS%20git%20merge.md

漫画讲解 git rebase VS git merge 



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

# 漫画讲解 git rebase VS git merge

关于 `git rebase` ，首先要理解的是它解决了和 `git merge` 同样的问题。这两个命令都旨在将更改从一个分支合并到另一个分支，但二者的合并方式却有很大的不同。

当你在专用分支上开发新 feature 时，然后另一个团队成员在 `master` 分支提交了新的 commit，这会发生什么？这会导致分叉的历史记录，这个问题对使用 Git 作为协作工具的任何人来说都应该很熟悉，那么该如何解决呢，这就是本文要讲解的内容。

Chat 内容：

1. 分析代码冲突的原因，并通过漫画的形式举例讲解。
2. 分析 `git merge` 合并分支代码
3. `git rebase` 合并分支代码，并通过漫画的形式举例讲解
4. `git merge` 对比 `git rebase` 该如何选择？
5. 加餐学习：`git stash` 解决线上代码冲突

## 分析代码冲突的原因，并通过漫画的形式举例讲解

代码冲突是团队协同开发绕不开的问题，要更好的解决它，首先我们就得深入的认识它。首先我们有一个基本的认识就是**代码冲突都是在代码合并的时候才产生**。所以代码冲突通常会在以下两个场景出现：

1. 本地仓库拉取远端仓库时产生
2. 本地主分支合并代码分支时产生

下面我通过漫画的形式来演示两种场景。首先准备两个本地客户端和一个代码仓库，两个客户端为了好记，姑且就叫熊大熊二吧（简称A和B）。

![在这里插入图片描述](assets/ff588160-e255-11eb-ba41-db0ddab65c9b)

码云（gitee.com）代码提交仓库网络图展现很好，后面将代码托管在码云上演示。

我这里提前在码云创建一个`git-conflict-demo`的项目，此时里面暂时没有任何内容。

![在这里插入图片描述](assets/074aa790-e256-11eb-9ac8-8334dbfe7cef)

### 本地仓库拉取远端仓库时产生

![在这里插入图片描述](assets/0f5537c0-e256-11eb-9839-c199edf90ba6)

```
git clone https://gitee.com/chandler2code/git-conflict-demo.git
cd git-conflict-demo
echo "apple">today-food-menu.txt
git add .
git commit -m "熊大 add today-food-menu.txt"
git push origin master

```

熊大添加了一个`today-food-menu.txt`文件，并在里面填入了apple，表示他今晚的食物想吃苹果。

![在这里插入图片描述](assets/17c31da0-e256-11eb-ba41-db0ddab65c9b)

于此同时，熊二也和他大哥一样的想法，但是他呢稍微慢了一步，此时熊大已经将代码提交到远端仓库，所以此时仓库里面已经有了`today-food-menu.txt`文件，并且里面的食物清单是苹果。

![在这里插入图片描述](assets/21469230-e256-11eb-8735-4b8052bf93fe)

因为熊二不想吃苹果，所以他果断将`today-food-menu.txt`里面的内容改为了蜂蜜`honey`。

```
git clone https://gitee.com/chandler2code/git-conflict-demo.git
sed -i 's/apple/honey/g' today-food-menu.txt
git add .
git commit -m 'update today-food-menu.txt'
git push origin master

```

![在这里插入图片描述](assets/297d3b70-e256-11eb-ba41-db0ddab65c9b)

熊大在提交代码后就有点后悔了，他觉得昨天才吃过苹果，今天换换口味吃香蕉了。

![在这里插入图片描述](assets/2f40c1d0-e256-11eb-8ae8-213f64a14867)

于是他将食物清单改为香蕉后再次提交。

```
sed -i 's/apple/banana/g' -i today-food-menu.txt
git add .
git commit -m 'update apple to banana'
git push origin master

```

但是这次可没有这么顺利就修改成功了，Git 报错信息

> To <https://gitee.com/chandler2code/git-conflict-demo.git> ! [rejected] master -> master (fetch first) error: failed to push some refs to ‘[https://gitee.com/chandler2code/git-conflict-demo.git’](https://gitee.com/chandler2code/git-conflict-demo.git') hint: Updates were rejected because the remote contains work that you do hint: not have locally. This is usually caused by another repository pushing hint: to the same ref. You may want to first integrate the remote changes hint: (e.g., ‘git pull …’) before pushing again. hint: See the ‘Note about fast-forwards’ in ‘git push –help’ for details.

意思就是当前分支与远端的分支相比，远端已经发生了修改，如果要继续操作，则要先执行命令`git pull`合并远端的代码。

下面来执行一下`git pull`，此时冲突就产生了，报错信息：

> remote: Enumerating objects: 5, done. remote: Counting objects: 100% (5⁄5), done. remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 Unpacking objects: 100% (3⁄3), done. From <https://gitee.com/chandler2code/git-conflict-demo> 5026b5e..484cb3d master -> origin/master Auto-merging today-food-menu.txt CONFLICT (content): Merge conflict in today-food-menu.txt Automatic merge failed; fix conflicts and then commit the result.

提示`today-food-menu.txt`产生了冲突，我们打开查看文件内容：

```
<<<<<<< HEAD
banana
=======
honey
>>>>>>> 484cb3d499b2c8cb762dad09e8fd64c035b90992

```

可以看到是本地的 banana 与远端的 honey 冲突了，那咋办呀？解决冲突呗。于是熊大和熊二坐在一起讨论，最终决定还是吃香蕉吧，于是熊大把蜂蜜部分去掉，保留香蕉再次提交，最后修改成功。

```
git add .
git commit -m 'merge conflic'
git push origin master

```

![在这里插入图片描述](assets/38e775d0-e256-11eb-a751-c93d727cbe27)

**总结：这里我们可以看到，冲突的原因就是当本地的文件和远端的文件都做了修改时，本地拉取远端时首先会告知由于远端有变更，需要git pull，执行git pull之后 Git 迷糊了，心想你们到底想要哪个内容呢，算了我不管了，直接给你们算冲突吧，你们自己决定保留哪些内容。**

### 本地主分支合并代码分支时产生

熊大在有了上次的本地拉取远端代码冲突时有了新的思考。

![在这里插入图片描述](assets/3fa8e430-e256-11eb-9ac8-8334dbfe7cef)

于是第二天在修改食物清单时，他选择自己先在本地创建分支，然后在自己的分支上修改，这样就可以时不时的切换到 master 分支拉取最新的代码。

```
#创建并切换到本地food分支
git checkout -b food
#今天他想吃苹果了
sed -i 's/banana/apple/g' -i today-food-menu.txt
git add .
#更改提交到本地
git commit -m 'update today-food-menu.txt: eat apple'

```

熊二今天依旧想吃蜂蜜，于是他将昨天的更新改拉取到本地后，将其更改为honey。

![在这里插入图片描述](assets/46f97330-e256-11eb-8735-4b8052bf93fe)

```
git pull
sed -i 's/banana/honey/g' -i today-food-menu.txt
git add .
git commit -m 'update today-food-menu.txt'
git push origin master

```

![在这里插入图片描述](assets/4cfa29a0-e256-11eb-9ac8-8334dbfe7cef)

熊大切换到master分支拉取，查看代码变化。

```
git checkout master
git pull

```

熊大拉取代码后发现`today-food-menu.txt`被更改为了honey。

![在这里插入图片描述](assets/5284c5b0-e256-11eb-b23b-e34e5b5fc461)

熊大考虑到仓库的蜂蜜快坏了，所以他这下坚持要吃苹果，于是他将自己的 food 分支的更改合并到 master 分支。有两种方式可以做到，分别是`git merge`和`git rabase`，后面都会详细的做讲解。我这里先用`git merge`解决冲突。

```
git merge food

```

合并分支时冲突产生，错误信息：

> Auto-merging today-food-menu.txt CONFLICT (content): Merge conflict in today-food-menu.txt Automatic merge failed; fix conflicts and then commit the result.

再查看冲突的内容：

```
<<<<<<< HEAD
honey
=======
apple
>>>>>>> food

```

可以看到 master 的 honey 和 food 分支的 apple 冲突了，于是又要解决冲突啦。熊大找到了熊二坐在一起讨论，“弟啊！苹果快坏了，咱今天就吃苹果哈！”，熊二也没有办法，最终再次屈服了。于是熊大把蜜蜂部分去掉，保留苹果部分，再次提交到远端仓库。

```
git add .
git commit -m 'master merge food:eat apple'
git push origin master

```

![在这里插入图片描述](assets/58b4f090-e256-11eb-83cb-07ac0d3b70bf)

**总结：在前面我们看到，如果 master 分支上开发。由于 master 分支时刻保持最新的发行代码，所以变动频繁，因此拉取 master 分支非常容易造成冲突。因此这里是将更改在本地分支上进行，在需要合并时，切换到 master 分支拉取最新代码后，根据拉取的内容，再去合并分支。同时这种方式也是更受大家推崇的。**

## 分析 git merge 合并分支代码的特点

上一节演示了冲突是如何产生的，并演示了通过`git merge`方式合并分支冲突。这一章节我们来分析一下`get merge`合并分支代码冲突的特点。

云端仓库查看 commit 记录

![在这里插入图片描述](assets/5e09fdb0-e256-11eb-b23b-e34e5b5fc461)

熊二将食物清单更新为 honey 并提交到远端仓库后，此时熊大在本地 commit，所以我们看到熊大的 commit 时间在熊二提交更新之前。熊二提交更新后，熊大切换到 master 分支，并更新代码到本地后，在合并分支时产生了冲突。为了合并冲突，多出了一次 merge 的 commit 记录。

我们再来云端看一下提交结构图：

![在这里插入图片描述](assets/6368a7c0-e256-11eb-808b-51f805f15e47)

从图中可以看到，`master merge food: eat apple`这次commit将前面的两次提交进行了合并，因为前面的这两次commit的代码完全相同的点在`merge confilc`这次提交，所以从`merge confic`到`master merge food:eat apple`这里多出来一个分叉的历史记录（绿线）。

在实际的生产开发过程中，采用这种方式会导致分叉的 commit 记录非常多，不利于开发人员代码审查。下面我们来看一下`git rebase`又是如何解决的呢？

## git rebase 合并分支代码，并通过漫画的形式举例讲解

熊大在本机创建 food2 分支，在本地分支上将内容修改为 honey。

![在这里插入图片描述](assets/68b0bc90-e256-11eb-b23b-e34e5b5fc461)

```
git checkout -b food2
sed -i 's/apple/honey/g' -i today-food-menu.txt
git add .
git commit -m 'update today-food-menu.txt:honey'

```

在熊大还没有 push 到远端时，他想起之前答应了熊二要像请他喝咖啡，于是他又改变为喝咖啡了。

![在这里插入图片描述](assets/6da24cf0-e256-11eb-b9fd-1da92bc1a30d)

```
sed -i 's/honey/coffee/g' -i today-food-menu.txt
git add .
git commit -m 'update today-food-menu.txt:coffee'

```

就在熊二还没有 push 到远端的时候，熊二本来计划吃蜂蜜的，但是想到蜂蜜不多了，决定留着过年吃，今天还是吃香蕉。于是将修改后的内容推送到了远端。

![在这里插入图片描述](assets/740d5df0-e256-11eb-a751-c93d727cbe27)

```
git pull
sed -i 's/apple/banana/g' -i today-food-menu.txt 
git add .
git commit -m 'update today-food-menu.txt:banana'
git push origin master

```

熊大此时准备将代码push到远端，首先他切换到master分支，拉取最新的代码。

```
git checkout master
git pull

```

此时熊大发现，`today-food-menu.txt`有变动，势必会造成代码冲突。下面通过`git rebase`来合并分支代码。

首先切换到 master 分支拉取最新代码，这个已经做了。下面是切换到 food2 分支指定 rebase 操作。

```
git checkout food2
git rebase master

```

输出信息

> First, rewinding head to replay your work on top of it… Applying: update today-food-menu.txt:honey Using index info to reconstruct a base tree… M today-food-menu.txt Falling back to patching base and 3-way merge… Auto-merging today-food-menu.txt CONFLICT (content): Merge conflict in today-food-menu.txt error: Failed to merge in the changes. Patch failed at 0001 update today-food-menu.txt:honey Use ‘git am –show-current-patch’ to see the failed patch
>
> Resolve all conflicts manually, mark them as resolved with “git add/rm ”, then run “git rebase –continue”. You can instead skip this commit: run “git rebase –skip”. To abort and get back to the state before “git rebase”, run “git rebase –abort”.

又回到了我们熟悉的合并冲突，查看`today-food-menu.txt`内容：

```
<<<<<<< HEAD
banana
=======
honey
>>>>>>> update today-food-menu.txt:honey

```

还记得吗，这次是熊大第一次 commit，他想着给熊二吃蜂蜜，但是发现远端拉取下来是吃香蕉。于是找了熊二商量，考虑到蜂蜜确实不多了，于是还是决定吃香蕉吧。所以此时保留 HEAD，删除`update today-food-menu.txt:honey`的内容。

修改完毕后，添加到本地库，继续 rebase。

```
git add .
git rebase --continue

```

输出信息：

> No changes - did you forget to use ‘git add’? If there is nothing left to stage, chances are that something else already introduced the same changes; you might want to skip this patch.

意思这次 rebase 合并冲突后和远端的内容一致，可以选择跳过这次 rebase。

```
git rebase --skip

```

跳过这次 commit 之后，来到下一次，输出信息：

> Applying: update today-food-menu.txt:coffee Using index info to reconstruct a base tree… M today-food-menu.txt Falling back to patching base and 3-way merge… Auto-merging today-food-menu.txt CONFLICT (content): Merge conflict in today-food-menu.txt error: Failed to merge in the changes. Patch failed at 0002 update today-food-menu.txt:coffee Use ‘git am –show-current-patch’ to see the failed patch
>
> Resolve all conflicts manually, mark them as resolved with “git add/rm ”, then run “git rebase –continue”. You can instead skip this commit: run “git rebase –skip”. To abort and get back to the state before “git rebase”, run “git rebase –abort”.

还记得吗，熊大还提交过一次将蜂蜜改为咖啡，我们来看一下冲突的内容：

```
<<<<<<< HEAD
banana
=======
coffee
>>>>>>> update today-food-menu.txt:coffee

```

这时熊大对熊二说，不好意思哥忘了之前决定了喝咖啡的，于是哥俩商量了一下，决定还是喝咖啡了。所以删除 HEAD 内容，保留`update today-food-menu.txt:coffee`这次 commit 的内容。

修改完毕后，添加到本地库，继续 rebase。

```
git add .
git rebase --continue

```

输出内容：

> Applying: update today-food-menu.txt:coffee

此时没有提示任何的信息，所以 rebase 结束。其实版本高一点的 Git（2.22及以上），是有 rebase 进度条展示的，可以看到 rebase 的进度，如图所示：

![在这里插入图片描述](assets/8542bb60-e256-11eb-8735-4b8052bf93fe)

rebase 结束后切换到 master 分支合并分支代码，然后直接推送到远端即可（此时不用指定 commit）。

```
git checkout master
git merge food2
git push origin master

```

![在这里插入图片描述](assets/8b0cf880-e256-11eb-9839-c199edf90ba6)

可以看到，一共有3次 commit 记录，分别是熊大2次和熊二1次。没有多出来 merge 的 commit 记录。

我们再来云端看一下提交结构图：

![在这里插入图片描述](assets/9067aaf0-e256-11eb-be77-f581c3259eef)

由于没有多出 merge 的 commit 记录，所以不会存在分叉的 commit 记录，代码记录都是以线性的方式，做代码审查一目了然。

**总结：有的小伙伴可能会说，看着前面的演示步骤好复杂啊。确实是，rebase 其实相当于是 merge 的进阶使用方式，目的就是为了让代码 commit 呈线性记录。**

## git merge 对比 git rebase 该如何选择？

`git merge` 操作合并分支会让两个分支的每一次提交都按照提交时间（并不是 push 时间）排序，并且会将两个分支的最新一次 commit 点进行合并成一个新的 commit，最终的分支树呈现非整条线性直线的形式。

`git rebase` 操作实际上是将当前执行 rebase 分支的所有基于原分支提交点之后的 commit 打散成一个一个的 patch，并重新生成一个新的 commit hash 值，再次基于原分支目前最新的commit点上进行提交，并不根据两个分支上实际的每次提交的时间点排序，rebase 完成后，切到基分支进行合并另一个分支时也不会生成一个新的 commit 点，可以保持整个分支树的完美线性。

**从效果出发，如果代码版本迭代快，项目大，参与人多，建议最好用 rebase 方式合并。反之则直接用 merge 即可。**

## 加餐学习：git stash 解决线上代码冲突

以上的演示合并冲突，是为了让我们的 commit 历史记录更加的便于审查。接下来我要说的`git stash`则是应急所需，平时工作中都是迫不得已的时候采用的，学会了以备不时之需。

1. 当正在 dev 分支上开发某个项目，这时项目中出现一个 bug，需要紧急修复，但是正在开发的内容只是完成一半，还不想提交，这时可以用`git stash`命令将修改的内容保存至堆栈区，然后顺利切换到 hotfix 分支进行 bug 修复，修复完成后，再次切回到 dev 分支，从堆栈中恢复刚刚保存的内容。
2. 由于疏忽，本应该在 dev 分支开发的内容，却在 master上进行了开发，需要重新切回到 dev 分支上进行开发，可以用git stash将内容保存至堆栈中，切回到 dev 分支后，再次恢复内容即可。

`git stash`命令的作用就是将目前还不想提交的但是已经修改的内容保存至堆栈中，后续可以在某个分支上恢复出堆栈中的内容。这也就是说，stash 中的内容不仅仅可以**恢复到原先开发的分支，也可以恢复到其他任意指定的分支上**。`git stash`作用的范围包括工作区和暂存区中的内容，也就是说没有提交的内容都会保存至堆栈中。

下面是一些有关stash的常用命令：

* `git stash`：能够将所有未提交的修改（工作区和暂存区）保存至堆栈中，用于后续恢复当前工作目录
* `git stash list`：查看当前 stash 的列表，因为有些时候会存多个暂存区
* `git stash pop`：将当前 stash 中的内容弹出，并应用到当前工作目录上。
* `git stash apply`：将堆栈中的内容应用到当前目录，不同于`git stash pop`，该命令不会将内容从堆栈中删除，也就说该命令能够将堆栈的内容多次应用到工作目录中，适应于多个分支的情况。
* `git stash clear`：除堆栈中的所有内容

## 总结

本文试图想用全漫画的形式展示，但是发现漫画绘制的时间长，且表达意思没有直接演示命令来的直接，所以曲线救国，采用了故事情节加代码叙述的方式讲解（希望别被骂成标题党）。文章的写作思路是，先从源头出发，了解产生冲突的来源。然后再进一步演示了通过`git merge`、`git rebase`合并分支代码，从提交 commit 记录、云端提交结构图、原理几个方面阐述了两者的差异，我个人比较推崇用`git rebase`。为了让内容更加的充实，文章再最后引入了`git stash`的内容，限于篇幅和侧重点，`git stash`只是起到了抛砖引玉的目的，没有展开和举例讲解，这点小伙伴们可以在网上查找资料补充学习。

---

© 2019 - 2023 [Liangliang Lee](/cdn-cgi/l/email-protection#6c00000055585d5d5c5b2c0b010d0500420f0301).
Powered by [gin](https://github.com/gin-gonic/gin) and [hexo-theme-book](https://github.com/kaiiiz/hexo-theme-book).