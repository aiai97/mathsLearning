# 延迟初始化（虚拟代理）：
#
# 网页加载中的图片延迟加载：在网页中，当有大量的图片需要加载时，可以使用代理模式来延迟初始化图片对象，只有当用户滚动到可见区域时才加载图片。
# 大型游戏中的资源加载：在大型游戏中，可能有大量的资源需要加载，如纹理、音频等。可以使用代理模式来延迟初始化这些资源对象，只有当需要使用时才进行加载。
# 访问控制（保护代理）：
#
# 操作系统中的权限控制：操作系统可以使用代理模式来限制特定用户或程序对关键资源的访问权限，只有具有特定权限的客户端才能访问受保护的资源。
# Web应用中的身份验证和授权：Web应用程序可以使用代理模式来验证用户身份并控制其对敏感数据或功能的访问权限。
# 本地执行远程服务（远程代理）：
#
# 远程API调用：在分布式系统中，客户端可以通过代理模式访问远程服务器上的API，代理负责处理网络通信和序列化等复杂细节，使得客户端可以像调用本地对象一样调用远程服务。
# 微服务架构中的服务调用：在微服务架构中，服务之间通过代理进行通信，代理可以处理负载均衡、故障转移等网络通信方面的任务，以提供可靠的服务调用。
# 记录日志请求（日志记录代理）：
#
# 网络请求日志记录：在Web开发中，可以使用代理模式来记录每个请求的详细信息，如请求URL、参数、响应时间等，以便进行监控、故障排查和性能优化。
# 数据库查询日志记录：在数据库访问中，可以使用代理模式来记录每个查询的日志，包括查询语句、执行时间等，以便分析和优化查询性能。
# 缓存请求结果（缓存代理）：
#
# 数据库查询结果缓存：在数据库查询中，可以使用代理模式来缓存查询结果，避免重复查询相同的数据，提高系统性能。
# API响应结果缓存：在Web开发中，可以使用代理模式来缓存API的响应结果，减少对后端服务的请求次数，提高响应速度。
# 智能引用：
#
# 垃圾回收机制：在编程语言中，可以使用代理模式来实现垃圾回收机制，通过代理记录对象的引用情况，当没有客户端引用对象时，可以及时销毁对象以释放资源。
# 对象池管理：在需要频繁创建和销毁对象的场景中，可以使用代理模式来实现对象的复用和管理，当没有客户端使用对象时，代理可以销毁对象并释放相关资源。
# class Image:
#     def display(self):
#         pass
#
# class RealImage(Image):
#     def __init__(self, filename):
#         self.filename = filename
#         self.load_image()
#
#     def load_image(self):
#         print("Loading image:", self.filename)
#
#     def display(self):
#         print("Displaying image:", self.filename)
#
# class ImageProxy(Image):
#     def __init__(self, filename):
#         self.filename = filename
#         self.real_image = None
#
#     def display(self):
#         if self.real_image is None:
#             self.real_image = RealImage(self.filename)
#         self.real_image.display()
#
# # Usage
# image_proxy = ImageProxy("image.jpg")
# # Image is not loaded yet
# image_proxy.display()
# Image is loaded and displayed
# import requests
#
# class RemoteService:
#     def request(self, data):
#         pass
#
# class RemoteServiceProxy(RemoteService):
#     def __init__(self, remote_url):
#         self.remote_url = remote_url
#
#     def request(self, data):
#         response = requests.post(self.remote_url, data=data)
#         return response.text
#
# # Usage
# remote_service_proxy = RemoteServiceProxy("http://api.example.com")
# response = remote_service_proxy.request({"key": "value"})
# print(response)
# class ProductService:
#     def get_product(self, product_id):
#         pass
#
# class ProductServiceProxy(ProductService):
#     def __init__(self, product_service):
#         self.product_service = product_service
#
#     def get_product(self, product_id):
#         self.log_request(product_id)
#         return self.product_service.get_product(product_id)
#
#     def log_request(self, product_id):
#         print(f"Request received for product ID: {product_id}. Logging the request.")
#
# # Usage
# product_service = ProductService()  # Actual product service object
# product_service_proxy = ProductServiceProxy(product_service)  # Proxy with logging capability
#
# product_service_proxy.get_product(123)  # Logs the request before calling the actual service
# class DataService:
#     def get_data(self, query):
#         pass
#
# class DataServiceProxy(DataService):
#     def __init__(self, data_service):
#         self.data_service = data_service
#         self.cache = {}
#
#     def get_data(self, query):
#         if query in self.cache:
#             print("Fetching data from cache.")
#             return self.cache[query]
#         else:
#             print("Fetching data from service.")
#             data = self.data_service.get_data(query)
#             self.cache[query] = data
#             return data
#
# # Usage
# data_service = DataService()  # Actual data service object
# data_service_proxy = DataServiceProxy(data_service)  # Proxy with caching capability
#
# data_service_proxy.get_data("SELECT * FROM users")  # Fetches data from the service
# data_service_proxy.get_data("SELECT * FROM users")  # Retrieves data from the cache
import sys

class HeavyObject:
    def __init__(self):
        print("Creating heavy object...")

    def process(self):
        print("Processing heavy object...")

class HeavyObjectProxy:
    def __init__(self):
        self.heavy_object = None

    def process(self):
        if self.heavy_object is None:
            self.heavy_object = HeavyObject()
        self.heavy_object.process()

    def __del__(self):
        if sys.getrefcount(self) == 2:  # Only the proxy and one reference from the client
            self.destroy_heavy_object()

    def destroy_heavy_object(self):
        print("Destroying heavy object...")
        del self.heavy_object

# Usage
proxy = HeavyObjectProxy()
proxy.process()  # Creates and processes the heavy object

proxy_copy = proxy  # Reference to the proxy
del proxy_copy  # Reference to the proxy is deleted, but the heavy object is not destroyed yet

proxy.process()  # Reuses the existing heavy object
del proxy  # Reference to the proxy is deleted, heavy object is destroyed
# proxy.process()  # Reuses the existing heavy object
# del proxy  # Reference to the proxy is deleted, heavy object is destroyed
