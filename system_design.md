

Performance vs Scalability
A service is scalable if it results in increased performance in a manner proportional to resources added. Generally, increasing performance means serving more units of work, but it can also be to handle larger units of work, such as when datasets grow.1

Another way to look at performance vs scalability:

If you have a performance problem, your system is slow for a single user.
If you have a scalability problem, your system is fast for a single user but slow under heavy load.
从另一个角度来看，性能与可扩展性的区别如下：
如果一个服务在增加资源的情况下能够以与之成比例的方式提高性能，那么它就具有可扩展性。通常，提高性能意味着能够处理更多的工作单元，但也可以是处理更大的工作单元，比如数据集增大的情况。

如果你面临性能问题，意味着你的系统对于单个用户而言速度较慢。
如果你面临可扩展性问题，意味着你的系统对于单个用户而言速度很快，但在高负载下速度变慢。
Latency vs throughput
Latency is the time to perform some action or to produce some result.

Throughput is the number of such actions or results per unit of time.

Generally, you should aim for maximal throughput with acceptable latency.

延迟和吞吐量是衡量系统性能的两个重要指标。延迟指的是系统响应请求所需的时间。吞吐量指的是系统同时能够处理的请求数量。

一般来说，我们应该追求在可接受的延迟范围内实现最大的吞吐量。也就是说，系统应该能够快速响应请求并且能够同时处理多个请求。
Consistency patterns
With multiple copies of the same data, we are faced with options on how to synchronize them so clients have a consistent view of the data. 
Recall the definition of consistency from the CAP theorem - Every read receives the most recent write or an error.

Weak consistency
After a write, reads may or may not see it. A best effort approach is taken.

This approach is seen in systems such as memcached. Weak consistency works well in real time use cases such as VoIP, video chat, and realtime multiplayer games. 
For example, if you are on a phone call and lose reception for a few seconds, when you regain connection you do not hear what was spoken during connection loss.

Eventual consistency
After a write, reads will eventually see it (typically within milliseconds). Data is replicated asynchronously.

This approach is seen in systems such as DNS and email. Eventual consistency works well in highly available systems.

Strong consistency
After a write, reads will see it. Data is replicated synchronously.

This approach is seen in file systems and RDBMSes. Strong consistency works well in systems that need transactions.

在具有多个相同数据副本的情况下，我们面临如何同步这些副本以使客户端对数据具有一致的视图的选择。回想一下CAP定理中对一致性的定义 - 每次读取都会获取到最新的写入或者一个错误。

弱一致性
在写入之后，读取可能会看到该写入，也可能不会看到。采取的是尽力而为的方法。

这种方法在诸如memcached的系统中可以看到。弱一致性在实时应用场景中非常有效，例如VoIP、视频聊天和实时多人游戏。例如，如果你在通话过程中失去信号几秒钟，在恢复连接后你不会听到连接中断期间的对话内容。

最终一致性
在写入之后，读取最终会看到它（通常在毫秒级别内）。数据是异步复制的。

这种方法在诸如DNS和电子邮件的系统中可以看到。最终一致性在高可用性的系统中非常有效。

强一致性
在写入之后，读取会看到它。数据是同步复制的。

这种方法在文件系统和关系型数据库管理系统（RDBMS）中可以看到。强一致性适用于需要事务支持的系统。
Availability patterns
There are two main patterns to support high availability: fail-over and replication.

Fail-over
Active-passive
With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.

The length of downtime is determined by whether the passive server is already running in 'hot' standy or whether it needs to start up from 'cold' standby. Only the active server handles traffic.

Active-passive failover can also be referred to as master-slave failover.

Active-active
In active-active, both servers are managing traffic, spreading the load between them.

If the servers are public-facing, the DNS would need to know about the public IPs of both servers. If the servers are internal-facing, application logic would need to know about both servers.

Active-active failover can also be referred to as master-master failover.

Disadvantage(s): failover
Fail-over adds more hardware and additional complexity.
There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive.
Replication
Master-slave replication
The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.


Source: Scalability, availability, stability, patterns

Disadvantage(s): master-slave replication
Additional logic is needed to promote a slave to a master.
See Disadvantage(s): replication for points related to both master-slave and master-master.
Master-master replication
Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.


Source: Scalability, availability, stability, patterns

Disadvantage(s): master-master replication
You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
Most master-master systems are either loosely consistent (violating ACID) or have increased write latency due to synchronization.
Conflict resolution comes more into play as more write nodes are added and as latency increases.
See Disadvantage(s): replication for points related to both master-slave and master-master.
Disadvantage(s): replication
There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
The more read slaves, the more you have to replicate, which leads to greater replication lag.
On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
Replication adds more hardware and additional complexity.
可用性模式availability
支持高可用性有两种主要模式：故障转移fail-over和复制replication

故障转移
主备模式 active-passive
在主备故障转移中，主服务器和备用服务器之间发送心跳信号。如果心跳中断，备用服务器会接管主服务器的IP地址并继续提供服务。

停机时间的长度取决于备用服务器是在热备状态下in hot standby运行还是需要从冷备状态cold standby启动。只有主服务器处理流量。

主备故障转移也可以称为主从故障转移。

主-主模式 active-active
在主-主模式下，两个服务器都管理流量，并在它们之间分担负载。

如果服务器面向公共用户，DNS需要知道两个服务器的公共IP地址。如果服务器面向内部用户，应用程序逻辑需要知道两个服务器。

主-主故障转移active-active failover也可以称为master-master failover主-主故障转移。

缺点：故障转移
故障转移需要增加更多的硬件和额外的复杂性。
如果在新写入的数据能够复制到备用服务器之前，主服务器发生故障，可能会导致数据丢失。
There is a potential for loss of data if any new written data can be replicated to the passive.
复制Replication
主从复制
主服务器提供读写服务，并将写入操作复制到一个或多个从服务器，从服务器仅提供读取服务。
从服务器也可以以树状结构进行复制。如果主服务器离线，系统可以继续以只读模式运行，直到将从服务器提升为主服务器或提供新的主服务器。

缺点：主从复制 master-slave replication
需要额外的逻辑来将从服务器提升为主服务器。 
Additional logic is needed to promote a slave to a master.
有关主从复制和主主复制的相关问题，请参阅复制的缺点部分。
主主复制 Master-master replication
Both servers serve reads and writes and coordinate with each other on writes.
两个主服务器均提供读写服务，并协调写入操作。如果其中一个主服务器发生故障，系统可以继续进行读写操作。

缺点：主主复制  
load balancer 
您需要负载均衡器，或者需要更改应用程序逻辑来确定写入位置。
大多数主主系统要么具有松散的一致性（违反ACID特性），要么由于同步而导致写入延迟增加。
Most systems are either loosely consistent(violating ACID) or have increased write latency due to synchronization.
随着写入节点的增加和延迟的增加，冲突解决变得更加重要。
Conflict resolution comes more into play as more write nodes are added and as latency increase.
有关主从复制和主主复制的相关问题，请参阅复制的缺点部分。
缺点：复制
如果主服务器在新写入的数据能够复制到其他节点之前发生故障，可能会导致数据丢失。
写入操作会被重放到读取副本。如果有大量写入操作，读取副本可能会因为重放写入操作而变慢，无法执行足够的读取操作
Writes can replayed to the read replicas.If there are a lot of writes,the read replicas can be bogged down
with replaying writes and can't do as many reads.
The more read slaves, the more you have to replicate, which leads to greater replication lag.
On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
Replication adds more hardware and additional complexity.
随着读取副本数量的增加，需要进行的复制操作也会增加，这导致了更大的复制延迟。
在某些系统中，写入主服务器可以使用多个线程并行写入，而读取副本只能使用单线程按顺序写入。
复制操作增加了更多的硬件和额外的复杂性。

写入操作重放、读取副本、写入顺序、复制延迟、并行写入、单线程写入、硬件复杂性

热备状态（Hot Standby）是指备用服务器处于运行状态，可以立即接管主服务器的功能和任务。在热备状态下，备用服务器已经启动并处于待命状态，准备接管主服务器的工作。
因此，当主服务器发生故障或不可用时，备用服务器可以立即接管并继续提供服务，从而减少系统的停机时间。
冷备状态（Cold Standby）是指备用服务器处于关闭或未启动的状态，不处理实际的工作负载和请求。在冷备状态下，备用服务器不参与实时的数据同步和服务处理，而是在主服务器发生故障或不可用时才启动。
当主服务器发生故障时，需要手动将备用服务器启动，并将主服务器的功能和数据迁移到备用服务器上，然后备用服务器才能开始处理工作负载和请求。

n a distributed computer system, you can only support two of the following guarantees:

Consistency - Every read receives the most recent write or an error
Availability - Every request receives a response, without guarantee that it contains the most recent version of the information
Partition Tolerance - The system continues to operate despite arbitrary partitioning due to network failures
Networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability.

CP - consistency and partition tolerance
Waiting for a response from the partitioned node might result in a timeout error. CP is a good choice if your business needs require atomic reads and writes.

AP - availability and partition tolerance
Responses return the most recent version of the data, which might not be the latest. Writes might take some time to propagate when the partition is resolved.

AP is a good choice if the business needs allow for eventual consistency or when the system needs to continue working despite external errors.


在分布式计算系统中，你只能支持以下两种保证中的两种：

一致性（Consistency）- 每次读取都会获得最近的写入结果或者一个错误
可用性（Availability）- 每次请求都会收到一个响应，但不能保证该响应包含最新的信息版本
分区容忍性（Partition Tolerance）- 即使由于网络故障而发生任意分区，系统仍然可以继续运行
由于网络是不可靠的，所以你需要支持分区容忍性。你需要在一致性和可用性之间进行软件折衷。

CP - 一致性和分区容忍性
从分区节点等待响应可能会导致超时错误。如果你的业务需求需要原子读写操作，CP 是一个很好的选择。

AP - 可用性和分区容忍性
响应会返回最新版本的数据，但可能不是最新的。当分区问题解决时，写入可能需要一些时间来传播。

如果业务需求允许最终一致性，或者系统需要在外部错误发生时继续工作，AP 是一个很好的选择。
 
Source: DNS security presentation

A Domain Name System (DNS) translates a domain name such as www.example.com to an IP address.

DNS is hierarchical, with a few authoritative servers at the top level. Your router or ISP provides information about which DNS server(s) to contact when doing a lookup. Lower level DNS servers cache mappings, which could become stale due to DNS propagation delays. DNS results can also be cached by your browser or OS for a certain period of time, determined by the time to live (TTL).

NS record (name server) - Specifies the DNS servers for your domain/subdomain.
MX record (mail exchange) - Specifies the mail servers for accepting messages.
A record (address) - Points a name to an IP address.
CNAME (canonical) - Points a name to another name or CNAME (example.com to www.example.com) or to an Arecord.
Services such as CloudFlare and Route 53 provide managed DNS services. Some DNS services can route traffic through various methods:

Weighted round robin
Prevent traffic from going to servers under maintenance
Balance between varying cluster sizes
A/B testing
Latency-based
Geolocation-based
Disadvantage(s): DNS
Accessing a DNS server introduces a slight delay, although mitigated by caching described above.
DNS server management could be complex, although they are generally managed by governments, ISPs, and large companies.
DNS services have recently come under DDoS attack, preventing users from accessing websites such as Twitter without knowing Twitter's IP address(es).
域名系统（DNS）将域名（例如www.example.com）转换为IP地址。

DNS具有层次结构，在顶级有少数几个权威服务器。您的路由器或ISP提供有关进行查找时要联系的DNS服务器的信息。较低级别的DNS服务器会缓存映射，但由于DNS传播延迟可能会过期。DNS结果也可以由您的浏览器或操作系统缓存一段时间，由生存时间（TTL）确定。

NS记录（名称服务器）- 指定您的域名/子域的DNS服务器。
MX记录（邮件交换）- 指定接受消息的邮件服务器。
A记录（地址）- 将名称指向IP地址。
CNAME（规范）- 将名称指向另一个名称或CNAME（例如，将example.com指向www.example.com）或A记录。
像CloudFlare和Route 53这样的服务提供托管的DNS服务。一些DNS服务可以通过各种方法路由流量：

加权轮询
防止流量发送到正在维护的服务器
在不同集群大小之间平衡
A/B测试
基于延迟的路由
基于地理位置的路由
缺点：DNS
访问DNS服务器会引入轻微的延迟，尽管上面描述的缓存可以减轻延迟。
DNS服务器管理可能很复杂，尽管它们通常由政府、ISP和大型公司管理。
最近，DNS服务遭受了DDoS攻击，导致用户无法访问Twitter等网站，除非知道Twitter的IP地址。
