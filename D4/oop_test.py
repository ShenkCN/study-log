class Server:
    def __init__(self, ip):
        self.ip = ip
        print(f"父类初始化：分配 IP {self.ip}")

class WebServer(Server): # 继承语法：括号里写父类名
    def __init__(self, ip, port):
        # super() 等同于 Java 里的 super，用来调用父类的构造方法
        super().__init__(ip) 
        self.port = port
        print(f"子类初始化：绑定 Nginx 端口 {self.port}")

    def start_nginx(self):
        print(f"在 {self.ip}:{self.port} 启动了 Nginx 服务")

# 测试
my_web = WebServer("10.0.0.1", 80)
my_web.start_nginx()


class MyDB:
    def __enter__(self):
        print("1. 【入场】打开数据库连接")
        return self  # 返回对象本身
        
    def query(self):
        print("2. 正在执行查询...")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("3. 【出场】自动关闭数据库连接，释放资源")

# 测试
with MyDB() as db:
    db.query()
# 只要退出 with 缩进，__exit__ 就会自动触发


import time

# 定义一个装饰器（这本质上是一个闭包函数）
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs) # 运行原函数
        end = time.time()
        print(f"【耗时统计】函数 {func.__name__} 运行了 {end - start:.4f} 秒")
        return result
    return wrapper

# 使用装饰器
@time_it
def slow_task():
    time.sleep(1)
    print("任务执行完毕")

slow_task()
