# 41 原子类和 volatile 有什么异同？ 

Source: https://learn.lianglianglee.com/专栏/Java 并发编程 78 讲-完/41 原子类和 volatile 有什么异同？.md

因收到Google相关通知，网站将会择期关闭。[相关通知内容](https://lumendatabase.org/notices/44265620)

---

# 41 原子类和 volatile 有什么异同？

本课时我们主要讲解原子类和 volatile 有什么异同。

## **案例****说明** **volatile** **和原子类的异同**

我们首先看一个案例。如图所示，我们有两个线程。

![img](assets/CgpOIF49B7qAIJThAAB6qxJtvhs898.png)

在图中左上角可以看出，有一个公共的 boolean flag 标记位，最开始赋值为 true，然后线程 2 会进入一个 while 循环，并且根据这个 flag 也就是标记位的值来决定是否继续执行或着退出。

最开始由于 flag 的值是 true，所以首先会在这里执行一定时期的循环。然后假设在某一时刻，线程 1 把这个 flag 的值改为 false 了，它所希望的是，线程 2 看到这个变化后停止运行。

但是这样做其实是有风险的，线程 2 可能并不能立刻停下来，也有可能过一段时间才会停止，甚至在最极端的情况下可能永远都不会停止。

为了理解发生这种情况的原因，我们首先来看一下 CPU 的内存结构，这里是一个双核的 CPU 的简单示意图：

![img](assets/Cgq2xl49B9GAHIQWAABs3zG_-08605.png)

可以看出，线程 1 和线程 2 分别在不同的 CPU 核心上运行，每一个核心都有自己的本地内存，并且在下方也有它们共享的内存。

最开始它们都可以读取到 flag 为 true ，不过当线程 1 这个值改为 false 之后，线程 2 并不能及时看到这次修改，因为线程 2 不能直接访问线程 1 的本地内存，这样的问题就是一个非常典型的可见性问题。

![img](assets/Cgq2xl49B-mAArdMAACJefFgK2k906.png)

要想解决这个问题，我们只需要在变量的前面加上 volatile 关键字修饰，只要我们加上这个关键字，那么每一次变量被修改的时候，其他线程对此都可见，这样一旦线程 1 改变了这个值，那么线程 2 就可以立刻看到，因此就可以退出 while 循环了。

![img](assets/Cgq2xl49CACANaAbAACTXNZMnjQ802.png)

之所以加了关键字之后就就可以让它拥有可见性，原因在于有了这个关键字之后，线程 1 的更改会被 flush 到共享内存中，然后又会被 refresh 到线程 2 的本地内存中，这样线程 2 就能感受到这个变化了，所以 volatile 这个关键字最主要是用来解决可见性问题的，可以一定程度上保证线程安全。

现在让我们回顾一下很熟悉的多线程同时进行 value++ 的场景，如图所示：

![img](assets/CgpOIF49CBeAUzqHAABbWQsq8Q8832.png)

如果它被初始化为每个线程都加 1000 次，最终的结果很可能不是 2000。由于 value++ 不是原子的，所以在多线程的情况下，会出现线程安全问题。但是如果我们在这里使用 volatile 关键字，能不能解决问题呢？

![img](assets/CgpOIF49CCqALcWIAABfoeCHiaA363.png)

很遗憾，答案是即便使用了 volatile 也是不能保证线程安全的，因为这里的问题不单单是可见性问题，还包含原子性问题。

我们有多种办法可以解决这里的问题，第 1 种是使用 synchronized 关键字，如图所示：

![img](assets/CgpOIF49CD6AQpviAACRYw_n1i4430.png)

这样一来，两个线程就不能同时去更改 value 的数值，保证了 value++ 语句的原子性，并且 synchronized 同样保证了可见性，也就是说，当第 1 个线程修改了 value 值之后，第 2 个线程可以立刻看见本次修改的结果。

解决这个问题的第 2 个方法，就是使用我们的原子类，如图所示：

![img](assets/CgpOIF49Ca2AL79uAACSZRAVJcg684.png)

比如用一个 AtomicInteger，然后每个线程都调用它的 incrementAndGet 方法。

在利用了原子变量之后就无需加锁，我们可以使用它的 incrementAndGet 方法，这个操作底层由 CPU 指令保证原子性，所以即便是多个线程同时运行，也不会发生线程安全问题。

## **原子类和** **volatile** **的使用场景**

那下面我们就来说一下原子类和 volatile 各自的使用场景。

我们可以看出，volatile 和原子类的使用场景是不一样的，如果我们有一个可见性问题，那么可以使用 volatile 关键字，但如果我们的问题是一个组合操作，需要用同步来解决原子性问题的话，那么可以使用原子变量，而不能使用 volatile 关键字。

通常情况下，volatile 可以用来修饰 boolean 类型的标记位，因为对于标记位来讲，直接的赋值操作本身就是具备原子性的，再加上 volatile 保证了可见性，那么就是线程安全的了。

而对于会被多个线程同时操作的计数器 Counter 的场景，这种场景的一个典型特点就是，它不仅仅是一个简单的赋值操作，而是需要先读取当前的值，然后在此基础上进行一定的修改，再把它给赋值回去。这样一来，我们的 volatile 就不足以保证这种情况的线程安全了。我们需要使用原子类来保证线程安全。