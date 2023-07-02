A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user. Generally, static files such as HTML/CSS/JSS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. The site's DNS resolution will tell clients which server to contact.

Serving content from CDNs can significantly improve performance in two ways:

Users receive content at data centers close to them
Your servers do not have to serve requests that the CDN fulfills
Push CDNs
Push CDNs receive new content whenever changes occur on your server. You take full responsibility for providing content, uploading directly to the CDN and rewriting URLs to point to the CDN. You can configure when content expires and when it is updated. Content is uploaded only when it is new or changed, minimizing traffic, but maximizing storage.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs. Content is placed on the CDNs once, instead of being re-pulled at regular intervals.

Pull CDNs
Pull CDNs grab new content from your server when the first user requests the content. You leave the content on your server and rewrite URLs to point to the CDN. This results in a slower request until the content is cached on the server.

A time-to-live (TTL) determines how long content is cached. Pull CDNs minimize storage space on the CDN, but can create redundant traffic if files expire and are pulled before they have actually changed.

Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.

Disadvantage(s): CDN
CDN costs could be significant depending on traffic, although this should be weighed with additional costs you would incur not using a CDN.
Content might be stale if it is updated before the TTL expires it.
CDNs require changing URLs for static content to point to the CDN.
推送式CDN和拉取式CDN的划分主要基于以下几个维度：

内容更新方式：推送式CDN要求您手动上传并推送新的内容到CDN服务器，而拉取式CDN则是在用户首次请求时从源服务器上拉取最新的内容。

缓存策略：推送式CDN在内容更改时会立即更新CDN上的内容，因此内容在整个CDN网络中都是一致的。而拉取式CDN会根据用户的请求动态地从源服务器获取内容，并在CDN上进行缓存，因此不同地区的CDN节点上可能存在不一致的内容。

存储需求：推送式CDN需要在CDN服务器上存储所有的内容副本，因此需要更大的存储空间。而拉取式CDN只在需要时从源服务器获取内容，可以节省存储空间。

流量分发：推送式CDN在内容更新时需要将内容推送到所有CDN节点，适用于流量较小或内容更新频率较低的网站。而拉取式CDN仅在用户请求时才从源服务器拉取内容，适用于流量较大且内容更新频繁的网站
静态cdn和动态cdn
CDN可以根据内容的特性分为静态CDN和动态CDN。

静态CDN主要用于提供静态文件，如HTML、CSS、JS、图片和视频等。这些文件在发布后通常不会经常变化。静态CDN将这些文件缓存到分布在全球各地的节点上，使用户能够从离他们更近的节点获取内容。静态CDN可以显著提高静态文件的加载速度和性能。

动态CDN则适用于动态生成的内容，例如根据用户请求实时生成的页面内容。动态CDN具有更复杂的缓存和动态内容管理机制，可以根据用户请求的参数、地理位置等动态地生成和分发内容。动态CDN可以帮助提高动态内容的传输效率和响应速度。

需要注意的是，并非所有的CDN都同时支持静态和动态内容。一些CDN服务提供商专注于静态内容的传输和缓存，而另一些则提供了更全面的动态内容管理和加速功能。

Load balancers distribute incoming client requests to computing resources such as application servers and databases. In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:

Preventing requests from going to unhealthy servers
Preventing overloading resources
Helping eliminate single points of failure
Load balancers can be implemented with hardware (expensive) or with software such as HAProxy.

Additional benefits include:

SSL termination - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
Removes the need to install X.509 certificates on each server
Session persistence - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions
To protect against failures, it's common to set up multiple load balancers, either in active-passive or active-active mode.

Load balancers can route traffic based on various metrics, including:

Random
Least loaded
Seesion/cookies
Round robin or weighted round robin
Layer 4
Layer 7
Layer 4 load balancing
Layer 4 load balancers look at info at the transport layer to decide how to distribute requests. Generally, this involves the source, destination IP addresses, and ports in the header, but not the contents of the packet. Layer 4 load balancers forward network packets to and from the upstream server, performing Network Address Translation (NAT).

layer 7 load balancing
Layer 7 load balancers look at the application layer to decide how to distribute requests. This can involve contents of the header, message, and cookies. Layer 7 load balancers terminates network traffic, reads the message, makes a load-balancing decision, then opens a connection to the selected server. For example, a layer 7 load balancer can direct video traffic to servers that host videos while directing more sensitive user billing traffic to security-hardened servers.

At the cost of flexibility, layer 4 load balancing requires less time and computing resources than Layer 7, although the performance impact can be minimal on modern commodity hardware.

Horizontal scaling
Load balancers can also help with horizontal scaling, improving performance and availability. Scaling out using commodity machines is more cost efficient and results in higher availability than scaling up a single server on more expensive hardware, called Vertical Scaling. It is also easier to hire for talent working on commodity hardware than it is for specialized enterprise systems.

Disadvantage(s): horizontal scaling
Scaling horizontally introduces complexity and involves cloning servers
Servers should be stateless: they should not contain any user-related data like sessions or profile pictures
Sessions can be stored in a centralized data store such as a database (SQL, NoSQL) or a persistent cache (Redis, Memcached)
Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out
Disadvantage(s): load balancer
The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
Introducing a load balancer to help eliminate single points of failure results in increased complexity.
A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.
负载均衡器将客户端的请求分发给应用服务器和数据库等计算资源。在每种情况下，负载均衡器将来自计算资源的响应返回给适当的客户端。
Load balancer distribute incoming requests to computing requests such as application servers and databases.
In each case,the load balancers returns the response from the computing resource to appropriate client.

负载均衡器在以下方面非常有效：
防止请求发送到不健康的服务器 unhealthy servers
防止资源过载 overloading resources
帮助消除单点故障 eliminate single points of failure
负载均衡器可以通过硬件（昂贵）或使用诸如HAProxy等软件实现。

其他优势包括：

SSL终止 - 对传入请求进行解密并加密服务器响应，从而避免后端服务器执行这些可能昂贵的操作
无需在每个服务器上安装X.509证书
会话持久性 - 发放Cookie，并将特定客户端的请求路由到同一实例（如果Web应用程序不跟踪会话）
为了防止故障，通常会设置多个负载均衡器，以主动-被动或主动-主动模式运行。

1）pick a worker to forward request
Random 
Round robin
least busy
sticky sessions/cookies
by request parameters
2) wait for its response
3) forward the response to client


负载均衡器可以根据多种指标来路由流量，包括：

随机
最低负载
会话/cookie
轮询或加权轮询
第4层
第7层
第4层负载均衡
第4层负载均衡器通过查看传输层的信息来决定如何分发请求。通常，这涉及到头部中的源IP地址、目标IP地址和端口，但不包括数据包的内容。第4层负载均衡器将网络数据包转发到上游服务器并执行网络地址转换（NAT）。

第7层负载均衡
第7层负载均衡器通过查看应用层的信息来决定如何分发请求。这可以涉及头部、消息和Cookie的内容。第7层负载均衡器终止网络流量，读取消息，做出负载均衡决策，然后与所选服务器建立连接。例如，第7层负载均衡器可以将视频流量定向到托管视频的服务器，同时将更敏感的用户账单流量定向到安全加固的服务器。

以灵活性为代价，与第7层相比，第4层负载均衡需要更少的时间和计算资源，尽管在现代常规硬件上对性能的影响可以忽略不计。


提及第四层和第七层负载均衡是因为它们代表了不同的负载均衡策略和功能。

第四层负载均衡（Layer 4 Load Balancing）是在传输层（Transport Layer）操作，主要根据源IP地址、目标IP地址、端口号等信息来决定如何分发请求。它关注的是网络传输层的信息，而不关心数据包的内容。第四层负载均衡器会将网络数据包转发到上游服务器，并执行网络地址转换（NAT）等操作。

第七层负载均衡（Layer 7 Load Balancing）是在应用层（Application Layer）操作，它能够深入到应用层的协议、消息内容、Cookie等信息来做出分发决策。第七层负载均衡器会解析网络流量，根据请求的内容进行负载均衡决策，然后与选定的服务器建立连接。它能够实现更高级的负载均衡策略，如基于请求内容的路由、会话保持等功能。

提及这两种负载均衡方式是为了说明它们在分发请求和处理网络流量时的不同方法和能力。根据应用程序的需求和系统的规模，选择适当的负载均衡方式可以提高性能、可靠性和可扩展性。

水平扩展 horizontal scaling
负载均衡器还可以帮助实现水平扩展，提高性能和可用性。使用廉价机器进行横向扩展比在昂贵的硬件上进行单个服务器的纵向扩展更具成本效益，也更容易招聘擅长常规硬件的人才，而不是企业级系统的专业人才。
Scaling out using commodity machine vs scaling up a single machine

缺点：水平扩展
水平扩展引入了复杂性，并涉及克隆服务器
服务器应该是无状态的：它们不应包含任何用户相关的数据，如会话或个人资料图片
会话可以存储在集中式数据存储（如数据库（SQL、NoSQL）或持久缓存（Redis、Memcached）中）
下游服务器（如缓存和数据库）需要处理更多的并发连接，因为上游服务器进行横向扩展
Downstream servers need to handle more simultaneous connections as upstream servers scale out.
缺点：负载均衡器
如果负载均衡器资源不足或配置不正确，负载均衡器可能成为性能瓶颈。performance bottleneck
为了消除单点故障，引入负载均衡器会增加复杂性。
单个负载均衡器是一个单点故障，配置多个负载均衡器会进一步增加复杂性。

TCP/IP协议并不严格按照OSI七层协议模型进行层次划分。它是一个较为简化的协议栈，通常被划分为四个层次，即：

网络接口层（Network Interface Layer）：也称为网络访问层，负责处理与物理网络介质的交互，包括硬件设备和驱动程序。它处理数据在网络上的传输，例如以太网或Wi-Fi。

网际层（Internet Layer）：在TCP/IP协议中，主要由IP协议负责。它提供了数据在网络中的传输和路由功能，负责将数据包从源主机发送到目标主机。

传输层（Transport Layer）：主要由TCP（传输控制协议）和UDP（用户数据报协议）组成。它负责在源主机和目标主机之间建立可靠的数据传输通道，并提供端到端的数据传输服务。

应用层（Application Layer）：这是TCP/IP协议栈的最高层，包含了各种应用程序使用的协议，例如HTTP、FTP、SMTP等。应用层协议负责定义数据的格式和交换规则，使不同应用程序能够进行数据通信。

Sticky session，也称为Session Affinity，是一种负载均衡技术，用于在分布式系统中保持用户会话的一致性。当用户与应用程序进行交互时，负载均衡器将该用户的请求路由到特定的后端服务器，并在后续的请求中始终将该用户的请求发送到相同的服务器上。

Sticky session 的实现通常使用一种称为"Session ID"的标识符来识别特定用户的会话。一旦用户与服务器建立初始连接，服务器会生成一个唯一的 Session ID，并将该 ID 通过 Cookie 或其他方式返回给用户的浏览器。在后续的请求中，浏览器会自动将该 Session ID 作为标识符发送给服务器，以保持会话的一致性。

通过使用 Sticky session，可以确保用户在整个会话期间都被路由到同一台服务器，这对于某些应用程序非常重要，特别是对于那些需要在会话期间保持状态的应用程序，如购物车信息、登录状态等。这样可以避免用户在不同服务器之间丢失会话数据或需要重新登录的情况。

然而，Sticky session 也有一些限制和缺点。当服务器负载不平衡或服务器故障时，Sticky session 可能导致某些服务器过载而其他服务器闲置。此外，Sticky session 可能会引入一些管理和维护的复杂性，因为服务器之间必须共享会话信息。

总之，Sticky session 是一种负载均衡技术，通过将用户的请求路由到特定的后端服务器，并在会话期间保持该路由的一致性，以确保用户的会话数据和状态的连续性。Cookie 是一种常用的实现方式，用于标识用户会话并将其路由到正确的服务器。
A reverse proxy is a web server that centralizes internal services and provides unified interfaces to the public. Requests from clients are forwarded to a server that can fulfill it before the reverse proxy returns the server's response to the client.

Additional benefits include:

Increased security - Hide information about backend servers, blacklist IPs, limit number of connections per client
Increased scalability and flexibility - Clients only see the reverse proxy's IP, allowing you to scale servers or change their configuration
SSL termination - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
Removes the need to install X.509 certificates on each server
Compression - Compress server responses
Caching - Return the response for cached requests
Static content - Serve static content directly
HTML/CSS/JS
Photos
Videos
Etc
Load balancer vs reverse proxy
Deploying a load balancer is useful when you have multiple servers. Often, load balancers route traffic to a set of servers serving the same function.
Reverse proxies can be useful even with just one web server or application server, opening up the benefits described in the previous section.
Solutions such as NGINX and HAProxy can support both layer 7 reverse proxying and load balancing.
Disadvantage(s): reverse proxy
Introducing a reverse proxy results in increased complexity.
A single reverse proxy is a single point of failure, configuring multiple reverse proxies (ie a failover) further increases complexity.
一个反向代理（Reverse Proxy）是一个Web服务器，它集中了内部服务并为公众提供统一的接口。客户端的请求会被转发到能够满足请求的服务器上，然后反向代理将服务器的响应返回给客户端。

反向代理的额外好处包括：

增强安全性 - 隐藏后端服务器的信息，黑名单IP地址，限制每个客户端的连接数
增加可扩展性和灵活性 - 客户端只看到反向代理的IP地址，允许你扩展服务器或更改其配置
SSL终止 - 解密传入请求并加密服务器响应，从而使后端服务器无需执行这些可能耗费性能的操作
无需在每个服务器上安装X.509证书
压缩 - 压缩服务器响应
缓存 - 返回缓存请求的响应
静态内容 - 直接提供静态内容
HTML/CSS/JS
图片
视频
等等
负载均衡器 vs 反向代理
当你有多个服务器时，部署负载均衡器非常有用。通常，负载均衡器将流量路由到一组执行相同功能的服务器上。
即使只有一个Web服务器或应用服务器，反向代理也可以带来好处，提供了上述部分描述的优势。
诸如NGINX和HAProxy等解决方案可以同时支持第7层反向代理和负载均衡。
缺点：反向代理
引入反向代理会增加复杂性。
单个反向代理是一个单点故障，配置多个反向代理（即故障转移）会进一步增加复杂性。
在网络架构中，负载均衡器通常位于反向代理的前面。负载均衡器作为第一层接收客户端请求，并根据负载均衡算法将请求分发给后端服务器。然后，反向代理作为第二层接收负载均衡器转发的请求，并将请求转发给能够处理该请求的后端服务器。

负载均衡器的作用是根据一定的策略将客户端请求分发给后端服务器，以达到负载均衡和高可用性的目的。它可以根据服务器的负载情况、响应时间等指标来做出决策。负载均衡器通常使用硬件设备或软件来实现，如硬件负载均衡器或软件负载均衡器。

反向代理的作用是隐藏后端服务器，并提供统一的接口给客户端。它可以提供一些额外的功能，如SSL终止、缓存、压缩、静态内容提供等。反向代理可以增加网络安全性，通过隐藏后端服务器的信息和执行其他安全措施来保护后端服务器。

综上所述，负载均衡器位于反向代理的前面，负责将请求分发给后端服务器，而反向代理位于负载均衡器的后面，提供额外的功能和保护后端服务器的安全性。
