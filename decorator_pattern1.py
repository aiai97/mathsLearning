
# 日志记录器：假设你有一个应用程序，你希望在每个函数或方法的调用时记录日志。使用装饰器模式，你可以创建一个 @log 装饰器，将其应用于需要记录日志的函数上，以实现日志记录的功能。

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
# 授权访问：假设你有一个 Web 应用程序，其中某些页面或资源需要进行身份验证和授权。你可以使用装饰器模式创建一个 @authorize 装饰器，将其应用于需要授权访问的视图函数上。

def user_is_authenticated():
    pass


def authorize(func):
    def wrapper(*args, **kwargs):
        if user_is_authenticated():
            return func(*args, **kwargs)
        else:
            return "Unauthorized"
    return wrapper

# @app.route("/secret")
@authorize
def secret_page():
    return "This is a secret page"

result = secret_page()
print(result)
