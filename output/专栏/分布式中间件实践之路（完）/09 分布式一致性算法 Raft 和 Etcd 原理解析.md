# 09 分布式一致性算法 Raft 和 Etcd 原理解析 

Source: https://learn.lianglianglee.com/专栏/分布式中间件实践之路（完）/09 分布式一致性算法 Raft 和 Etcd 原理解析.md

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# 09 分布式一致性算法 Raft 和 Etcd 原理解析

“工欲善其事，必先利其器。”懂得原理方能触类旁通，立于不败之地。本文首先详细解读了著名的分布式一致性算法 Raft，在此基础上，介绍了 Etcd 的架构和典型应用场景。本文内容是学习下一篇 “基于 Etcd 的分布式锁”的基础。

### 1. Raft 算法简介

#### 1.1 Raft 背景

在分布式系统中，一致性算法至关重要。在所有一致性算法中，Paxos 最负盛名，它由莱斯利·兰伯特（Leslie Lamport）于 1990 年提出，是一种基于消息传递的一致性算法，被认为是类似算法中最有效的。

Paxos 算法虽然很有效，但复杂的原理使它实现起来非常困难，截止目前，实现 Paxos 算法的开源软件很少，比较出名的有 Chubby、LibPaxos。此外，Zookeeper 采用的 ZAB（Zookeeper Atomic Broadcast）协议也是基于 Paxos 算法实现的，不过 ZAB 对 Paxos 进行了很多改进与优化，两者的设计目标也存在差异——ZAB 协议主要用于构建一个高可用的分布式数据主备系统，而 Paxos 算法则是用于构建一个分布式的一致性状态机系统。

由于 Paxos 算法过于复杂、实现困难，极大地制约了其应用，而分布式系统领域又亟需一种高效而易于实现的分布式一致性算法，在此背景下，Raft 算法应运而生。

Raft 算法在斯坦福 Diego Ongaro 和 John Ousterhout 于 2013 年发表的《In Search of an Understandable Consensus Algorithm》中提出。相较于 Paxos，Raft 通过逻辑分离使其更容易理解和实现，目前，已经有十多种语言的 Raft 算法实现框架，较为出名的有 etcd、Consul 。

#### 1.2 Raft 角色

根据官方文档解释，一个 Raft 集群包含若干节点，Raft 把这些节点分为三种状态：Leader、 Follower、Candidate，每种状态负责的任务也是不一样的。正常情况下，集群中的节点只存在 Leader 与 Follower 两种状态。

* **Leader（领导者）**：负责日志的同步管理，处理来自客户端的请求，与Follower保持heartBeat的联系；
* **Follower（追随者）**：响应 Leader 的日志同步请求，响应Candidate的邀票请求，以及把客户端请求到Follower的事务转发（重定向）给Leader；
* **Candidate（候选者）**：负责选举投票，集群刚启动或者Leader宕机时，状态为Follower的节点将转为Candidate并发起选举，选举胜出（获得超过半数节点的投票）后，从Candidate转为Leader状态。

#### 1.3 Raft 三个子问题

通常，Raft 集群中只有一个 Leader，其它节点都是 Follower。Follower 都是被动的，不会发送任何请求，只是简单地响应来自 Leader 或者 Candidate 的请求。Leader 负责处理所有的客户端请求（如果一个客户端和 Follower 联系，那么 Follower 会把请求重定向给 Leader）。

为简化逻辑和实现，Raft 将一致性问题分解成了三个相对独立的子问题。

* **选举（Leader Election）**：当 Leader 宕机或者集群初创时，一个新的 Leader 需要被选举出来；
* **日志复制（Log Replication）**：Leader 接收来自客户端的请求并将其以日志条目的形式复制到集群中的其它节点，并且强制要求其它节点的日志和自己保持一致；
* **安全性（Safety）**：如果有任何的服务器节点已经应用了一个确定的日志条目到它的状态机中，那么其它服务器节点不能在同一个日志索引位置应用一个不同的指令。

### 2. Raft 算法之 Leader Election 原理

根据 Raft 协议，一个应用 Raft 协议的集群在刚启动时，所有节点的状态都是 Follower。由于没有 Leader，Followers 无法与 Leader 保持心跳（Heart Beat），因此，Followers 会认为 Leader 已经下线，进而转为 Candidate 状态。然后，Candidate 将向集群中其它节点请求投票，同意自己升级为 Leader。如果 Candidate 收到超过半数节点的投票（N/2 + 1），它将获胜成为 Leader。

**第一阶段：所有节点都是 Follower。**

上面提到，一个应用 Raft 协议的集群在刚启动（或 Leader 宕机）时，所有节点的状态都是 Follower，初始 Term（任期）为 0。同时启动选举定时器，每个节点的选举定时器超时时间都在 100~500 毫秒之间且并不一致（避免同时发起选举）。

![enter image description here](assets/0e6c7fa0-b831-11e8-9da0-3bed0a166513)

**第二阶段：Follower 转为 Candidate 并发起投票。**

没有 Leader，Followers 无法与 Leader 保持心跳（Heart Beat），节点启动后在一个选举定时器周期内未收到心跳和投票请求，则状态转为候选者 Candidate 状态，且 Term 自增，并向集群中所有节点发送投票请求并且重置选举定时器。

注意，由于每个节点的选举定时器超时时间都在 100-500 毫秒之间，且彼此不一样，以避免所有 Follower 同时转为 Candidate 并同时发起投票请求。换言之，最先转为 Candidate 并发起投票请求的节点将具有成为 Leader 的“先发优势”。

![enter image description here](assets/192d60c0-b832-11e8-9da0-3bed0a166513)

**第三阶段：投票策略。**

节点收到投票请求后会根据以下情况决定是否接受投票请求：

1. 请求节点的 Term 大于自己的 Term，且自己尚未投票给其它节点，则接受请求，把票投给它；
2. 请求节点的 Term 小于自己的 Term，且自己尚未投票，则拒绝请求，将票投给自己。

![enter image description here](assets/cf56fbe0-b832-11e8-9da0-3bed0a166513)

**第四阶段：Candidate 转为 Leader。**

一轮选举过后，正常情况下，会有一个 Candidate 收到超过半数节点（N/2 + 1）的投票，它将胜出并升级为 Leader。然后定时发送心跳给其它的节点，其它节点会转为 Follower 并与 Leader 保持同步，到此，本轮选举结束。

注意：有可能一轮选举中，没有 Candidate 收到超过半数节点投票，那么将进行下一轮选举。

![enter image description here](assets/206d5880-b833-11e8-9469-d363e3097731)

### 3. Raft 算法之 Log Replication 原理

在一个 Raft 集群中，只有 Leader 节点能够处理客户端的请求（如果客户端的请求发到了 Follower，Follower 将会把请求重定向到 Leader），客户端的每一个请求都包含一条被复制状态机执行的指令。Leader 把这条指令作为一条新的日志条目（Entry）附加到日志中去，然后并行得将附加条目发送给 Followers，让它们复制这条日志条目。

当这条日志条目被 Followers 安全复制，Leader 会将这条日志条目应用到它的状态机中，然后把执行的结果返回给客户端。如果 Follower 崩溃或者运行缓慢，再或者网络丢包，Leader 会不断得重复尝试附加日志条目（尽管已经回复了客户端）直到所有的 Follower 都最终存储了所有的日志条目，确保强一致性。

**第一阶段：客户端请求提交到 Leader。**

如下图所示，Leader 收到客户端的请求，比如存储数据 5。Leader 在收到请求后，会将它作为日志条目（Entry）写入本地日志中。需要注意的是，此时该 Entry 的状态是未提交（Uncommitted），Leader 并不会更新本地数据，因此它是不可读的。

![enter image description here](assets/46017c00-b835-11e8-9469-d363e3097731)

**第二阶段：Leader 将 Entry 发送到其它 Follower**

Leader 与 Floolwers 之间保持着心跳联系，随心跳 Leader 将追加的 Entry（AppendEntries）并行地发送给其它的 Follower，并让它们复制这条日志条目，这一过程称为复制（Replicate）。

有几点需要注意：

**1.** 为什么 Leader 向 Follower 发送的 Entry 是 AppendEntries 呢？

因为 Leader 与 Follower 的心跳是周期性的，而一个周期间 Leader 可能接收到多条客户端的请求，因此，随心跳向 Followers 发送的大概率是多个 Entry，即 AppendEntries。当然，在本例中，我们假设只有一条请求，自然也就是一个Entry了。

**2.** Leader 向 Followers 发送的不仅仅是追加的 Entry（AppendEntries）。

在发送追加日志条目的时候，Leader 会把新的日志条目紧接着之前条目的索引位置（prevLogIndex）， Leader 任期号（Term）也包含在其中。如果 Follower 在它的日志中找不到包含相同索引位置和任期号的条目，那么它就会拒绝接收新的日志条目，因为出现这种情况说明 Follower 和 Leader 不一致。

**3.** 如何解决 Leader 与 Follower 不一致的问题？

在正常情况下，Leader 和 Follower 的日志保持一致，所以追加日志的一致性检查从来不会失败。然而，Leader 和 Follower 一系列崩溃的情况会使它们的日志处于不一致状态。Follower可能会丢失一些在新的 Leader 中有的日志条目，它也可能拥有一些 Leader 没有的日志条目，或者两者都发生。丢失或者多出日志条目可能会持续多个任期。

要使 Follower 的日志与 Leader 恢复一致，Leader 必须找到最后两者达成一致的地方（说白了就是回溯，找到两者最近的一致点），然后删除从那个点之后的所有日志条目，发送自己的日志给 Follower。所有的这些操作都在进行附加日志的一致性检查时完成。

Leader 为每一个 Follower 维护一个 nextIndex，它表示下一个需要发送给 Follower 的日志条目的索引地址。当一个 Leader 刚获得权力的时候，它初始化所有的 nextIndex 值，为自己的最后一条日志的 index 加 1。如果一个 Follower 的日志和 Leader 不一致，那么在下一次附加日志时一致性检查就会失败。在被 Follower 拒绝之后，Leader 就会减小该 Follower 对应的 nextIndex 值并进行重试。最终 nextIndex 会在某个位置使得 Leader 和 Follower 的日志达成一致。当这种情况发生，附加日志就会成功，这时就会把 Follower 冲突的日志条目全部删除并且加上 Leader 的日志。一旦附加日志成功，那么 Follower 的日志就会和 Leader 保持一致，并且在接下来的任期继续保持一致。

![enter image description here](assets/87e3fb10-b836-11e8-a627-cbcd94258d1d)

**第三阶段：Leader 等待 Followers 回应。**

Followers 接收到 Leader 发来的复制请求后，有两种可能的回应：

1. 写入本地日志中，返回 Success；
2. 一致性检查失败，拒绝写入，返回 False，原因和解决办法上面已做了详细说明。

需要注意的是，此时该 Entry 的状态也是未提交（Uncommitted）。完成上述步骤后，Followers 会向 Leader 发出 Success 的回应，当 Leader 收到大多数 Followers 的回应后，会将第一阶段写入的 Entry 标记为提交状态（Committed），并把这条日志条目应用到它的状态机中。

![enter image description here](assets/1802d130-b837-11e8-9d9d-aba50ff29480)

**第四阶段：Leader 回应客户端。**

完成前三个阶段后，Leader会向客户端回应 OK，表示写操作成功。

![enter image description here](assets/6ea4b440-b837-11e8-9469-d363e3097731)

**第五阶段，Leader 通知 Followers Entry 已提交**

Leader 回应客户端后，将随着下一个心跳通知 Followers，Followers 收到通知后也会将 Entry 标记为提交状态。至此，Raft 集群超过半数节点已经达到一致状态，可以确保强一致性。

需要注意的是，由于网络、性能、故障等各种原因导致“反应慢”、“不一致”等问题的节点，最终也会与 Leader 达成一致。

![enter image description here](assets/080b5580-b838-11e8-9469-d363e3097731)

### 4. Raft 算法之安全性

前面描述了 Raft 算法是如何选举 Leader 和复制日志的。然而，到目前为止描述的机制并不能充分地保证每一个状态机会按照相同的顺序执行相同的指令。例如，一个 Follower 可能处于不可用状态，同时 Leader 已经提交了若干的日志条目；然后这个 Follower 恢复（尚未与 Leader 达成一致）而 Leader 故障；如果该 Follower 被选举为 Leader 并且覆盖这些日志条目，就会出现问题，即不同的状态机执行不同的指令序列。

鉴于此，在 Leader 选举的时候需增加一些限制来完善 Raft 算法。这些限制可保证任何的 Leader 对于给定的任期号（Term），都拥有之前任期的所有被提交的日志条目（所谓 Leader 的完整特性）。关于这一选举时的限制，下文将详细说明。

#### 4.1 选举限制

在所有基于 Leader 机制的一致性算法中，Leader 都必须存储所有已经提交的日志条目。为了保障这一点，Raft 使用了一种简单而有效的方法，以保证所有之前的任期号中已经提交的日志条目在选举的时候都会出现在新的 Leader 中。换言之，日志条目的传送是单向的，只从 Leader 传给 Follower，并且 Leader 从不会覆盖自身本地日志中已经存在的条目。

Raft 使用投票的方式来阻止一个 Candidate 赢得选举，除非这个 Candidate 包含了所有已经提交的日志条目。Candidate 为了赢得选举必须联系集群中的大部分节点。这意味着每一个已经提交的日志条目肯定存在于至少一个服务器节点上。如果 Candidate 的日志至少和大多数的服务器节点一样新（这个新的定义会在下面讨论），那么它一定持有了所有已经提交的日志条目（多数派的思想）。投票请求的限制中请求中包含了 Candidate 的日志信息，然后投票人会拒绝那些日志没有自己新的投票请求。

Raft 通过比较两份日志中最后一条日志条目的索引值和任期号，确定谁的日志比较新。如果两份日志最后条目的任期号不同，那么任期号大的日志更加新。如果两份日志最后的条目任期号相同，那么日志比较长的那个就更加新。

#### 4.2 提交之前任期内的日志条目

如同 4.1 节介绍的那样，Leader 知道一条当前任期内的日志记录是可以被提交的，只要它被复制到了大多数的 Follower 上（多数派的思想）。如果一个 Leader 在提交日志条目之前崩溃了，继任的 Leader 会继续尝试复制这条日志记录。然而，一个 Leader 并不能断定被保存到大多数 Follower 上的一个之前任期里的日志条目 就一定已经提交了。这很明显，从日志复制的过程可以看出。

鉴于上述情况，Raft 算法不会通过计算副本数目的方式去提交一个之前任期内的日志条目。只有 Leader 当前任期里的日志条目通过计算副本数目可以被提交；一旦当前任期的日志条目以这种方式被提交，那么由于日志匹配特性，之前的日志条目也都会被间接的提交。在某些情况下，Leader 可以安全地知道一个老的日志条目是否已经被提交（只需判断该条目是否存储到所有节点上），但是 Raft 为了简化问题使用了一种更加保守的方法。

当 Leader 复制之前任期里的日志时，Raft 会为所有日志保留原始的任期号，这在提交规则上产生了额外的复杂性。但是，这种策略更加容易辨别出日志，即使随着时间和日志的变化，日志仍维护着同一个任期编号。此外，该策略使得新 Leader 只需要发送较少日志条目。

### 5. Etcd 介绍

Etcd 是一个高可用、强一致的分布式键值（Key-Value）数据库，主要用途是共享配置和服务发现。其内部采用 Raft 算法作为分布式一致性协议，因此，Etcd 集群作为一个分布式系统“天然” 具有强一致性；而副本机制（一个 Leader，多个 Follower）又保证了其高可用性（点击进入 [Etcd 官网](https://coreos.com/etcd/)）。

**Etcd 命名的由来**

在 Unix 系统中，`/etc` 目录用于存放系统管理和配置文件。分布式系统（Distributed System）第一个字母是“d”。两者看上去并没有直接联系，但它们加在一起就有点意思了：分布式的关键数据（系统管理和配置文件）存储系统，这便是 Etcd 命名的灵感之源。

#### 5.1 Etcd 架构

Etcd 的架构图如下，从架构图中可以看出，Etcd 主要分为四个部分：HTTP Server、Store、Raft 以及 WAL。

![enter image description here](assets/4577c8b0-b82c-11e8-b3f0-6503db3b148e)

* HTTP Server：用于处理客户端发送的 API 请求以及其它 Etcd 节点的同步与心跳信息请求。
* Store：用于处理 Etcd 支持的各类功能的事务，包括数据索引、节点状态变更、监控与反馈、事件处理与执行等等，是 Etcd 对用户提供的大多数 API 功能的具体实现。
* Raft：Raft 强一致性算法的具体实现，是 Etcd 的核心。
* WAL：Write Ahead Log（预写式日志），是 Etcd 的数据存储方式。除了在内存中存有所有数据的状态以及节点的索引，Etcd 还通过 WAL 进行持久化存储。WAL 中，所有的数据提交前都会事先记录日志。Snapshot 是为了防止数据过多而进行的状态快照。Entry 表示存储的具体日志内容。

通常，一个用户的请求发送过来，会经由 HTTP Server 转发给 Store 进行具体的事务处理；如果涉及到节点的修改，则交给 Raft 模块进行状态的变更、日志的记录，然后再同步给别的 Etcd 节点以确认数据提交；最后进行数据的提交，再次同步。

#### 5.2 Etcd 的基本概念词

由于 Etcd 基于分布式一致性算法 Raft，其涉及的概念词与 Raft 保持一致，如下所示，通过前面 Raft 算法的介绍，相信读者已经可以大体勾勒出 Etcd 集群的运作机制。

* Raft：Etcd 的核心，保证分布式系统强一致性的算法。
* Node：一个 Raft 状态机实例。
* Member：一个 Etcd 实例，它管理着一个 Node，并且可以为客户端请求提供服务。
* Cluster：由多个 Member 构成可以协同工作的 Etcd 集群。
* Peer：对同一个 Etcd 集群中另外一个 Member 的称呼。
* Client：向 Etcd 集群发送 HTTP 请求的客户端。
* WAL：预写式日志，Etcd 用于持久化存储的日志格式。
* Snapshot：Etcd 防止 WAL 文件过多而设置的快照，存储 Etcd 数据状态。
* Leader：Raft 算法中通过竞选而产生的处理所有数据提交的节点。
* Follower：竞选失败的节点作为 Raft 中的从属节点，为算法提供强一致性保证。
* Candidate：当超过一定时间接收不到 Leader 的心跳时， Follower 转变为 Candidate 开始竞选。
* Term：某个节点成为 Leader 到下一次竞选期间，称为一个 Term（任期）。
* Index：数据项编号。Raft 中通过 Term 和 Index 来定位数据。

#### 5.3 Etcd 能做什么

在分布式系统中，有一个最基本的需求，即如何保证分布式部署的多个节点之间的数据共享。如同团队协作，成员可以分头干活，但总是需要共享一些必须的信息，比如谁是 Leader、团队成员列表、关联任务之间的顺序协调等。所以分布式系统要么自己实现一个可靠的共享存储来同步信息，要么依赖一个可靠的共享存储服务，而 Etcd 就是这样一个服务。

[Etcd 官方](https://coreos.com/etcd/)如此介绍：“A distributed, reliable key-value store for the most critical data of a distributed system.”简言之，它是一个可用于存储分布式系统关键数据的可靠的键值数据库。关于可靠性自不必多说，Raft 协议已经阐明，但事实上，Etcd 作为 Key-Value 型数据库还有其它特点，如 Watch 机制、租约机制、Revision 机制等，正是这些机制赋予了 Etcd 强大的能力。

* **Lease 机制**：即租约机制（TTL，Time To Live），Etcd 可以为存储的 Key-Value 对设置租约，当租约到期，Key-Value 将失效删除；同时也支持续约，通过客户端可以在租约到期之前续约，以避免 Key-Value 对过期失效；此外，还支持解约，一旦解约，与该租约绑定的 Key-Value 将失效删除；
* **Prefix 机制**：即前缀机制，也称目录机制，如两个 Key 命名如下：`key1=“/mykey/key1”，key2="/mykey/key2"`，那么，可以通过前缀“/mykey”查询，返回包含两个 Key-Value 对的列表；
* **Watch 机制**：即监听机制，Watch 机制支持监听某个固定的 Key，也支持监听一个范围（前缀机制），当被监听的 Key 或范围发生变化，客户端将收到通知；
* **Revision 机制**：每个 Key 带有一个 Revision 号，每进行一次事务便加一，因此它是全局唯一的，如初始值为 0，进行一次 Put 操作，Key 的 Revision 变为1，同样的操作，再进行一次，Revision 变为 2；换成 Key1 进行 Put 操作，Revision 将变为 3。这种机制有一个作用，即通过 Revision 的大小就可知道写操作的顺序，这对于实现公平锁，队列十分有益。

#### 5.4 Etcd 主要应用场景

从 5.3 节的介绍可以看出，Etcd 的功能非常强大，其功能点或功能组合可以实现众多的需求，以下列举一些典型应用场景。

**应用场景 1：服务发现**

服务发现（Service Discovery）要解决的是分布式系统中最常见的问题之一，即在同一个分布式集群中的进程或服务如何才能找到对方并建立连接。服务发现的实现原理如下。

* 存在一个高可靠、高可用的中心配置节点：基于 Ralf 算法的 Etcd 天然支持，不必多解释。
* 服务提供方会持续的向配置节点注册服务：用户可以在 Etcd 中注册服务，并且对注册的服务配置租约，定时续约以达到维持服务的目的（一旦停止续约，对应的服务就会失效）。
* 服务的调用方会持续地读取中心配置节点的配置并修改本机配置，然后 Reload 服务：服务提供方在 Etcd 指定的目录（前缀机制支持）下注册服务，服务调用方在对应的目录下查询服务。通过 Watch 机制，服务调用方还可以监测服务的变化。

**应用场景 2： 消息发布和订阅**

在分布式系统中，组件间通信常用的方式是消息发布-订阅机制。具体而言，即配置一个配置共享中心，数据提供者在这个配置中心发布消息，而消息使用者则订阅它们关心的主题，一旦有关主题有消息发布，就会实时通知订阅者。通过这种方式可以实现分布式系统配置的集中式管理和实时动态更新。显然，通过 Watch 机制可以实现。

应用在启动时，主动从 Etcd 获取一次配置信息，同时，在 Etcd 节点上注册一个 Watcher 并等待，以后每次配置有更新，Etcd 都会实时通知订阅者，以此达到获取最新配置信息的目的。

**应用场景 3： 分布式锁**

前面已经提及，Etcd 支持 Revision 机制，那么对于同一个 Lock，即便有多个客户端争夺（本质上就是 `put(lockName, value)` 操作），Revision 机制可以保证它们的 Revision 编号有序且唯一，那么，客户端只要根据 Revision 的大小顺序就可以确定获得锁的先后顺序，从而很容易实现“公平锁”。

**应用场景4： 集群监控与 Leader 竞选**

* **集群监控**：通过 Etcd 的 Watch 机制，当某个 Key 消失或变动时，Watcher 会第一时间发现并告知用户。节点可以为 Key 设置租约（TTL），比如每隔 30 s 向 Etcd 发送一次心跳续约，使代表该节点的 Key 保持存活，一旦节点故障，续约停止，对应的 Key 将失效删除。如此，通过 Watch 机制就可以第一时间检测到各节点的健康状态，以完成集群的监控要求。
* **Leader 竞选**：使用分布式锁，可以很好地实现 Leader 竞选（抢锁成功的成为 Leader）。Leader 应用的经典场景是在搜索系统中建立全量索引。如果每个机器分别进行索引建立，不仅耗时，而且不能保证索引的一致性。通过在 Etcd 实现的锁机制竞选 Leader，由 Leader 进行索引计算，再将计算结果分发到其它节点。

#### 5.5 Etcd 的部署方法

Etcd 集群的部署比较简单，官方提供了详细的说明（[点击查看](https://coreos.com/etcd/docs/latest/demo.html)），网上也有很多博客，因此，本文就不在赘述了。另外，Etcd 提供了 Windows 版本，对于只有 Windows 环境的读者，可以放心了（点击访问[官方下载地址](https://github.com/etcd-io/etcd/releases)）。