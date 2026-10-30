import time
import threading
from concurrent.futures import ThreadPoolExecutor

# 模拟一个网络请求，耗时1秒
def fetch_url(url):
    time.sleep(1)  # 假装在等网络
    print(f"完成: {url}")
    return f"数据:{url}"

# 1. 先体验“同步排队”写法
def run_sync(urls):
    start = time.time()
    for url in urls:
        fetch_url(url)
    print(f"同步总耗时: {time.time() - start:.2f} 秒\n")

# 2. 再体验“并发+限流”写法
def run_concurrent(urls):
    start = time.time()
    # 规定：最多同时只能有 3 个请求在运行
    sem = threading.Semaphore(3) 
    
    def wrapped_fetch(url):
        with sem: # 拿到号码牌才能干活
            return fetch_url(url)
            
    # 开一个能容纳5个线程的池子
    with ThreadPoolExecutor(max_workers=5) as pool:
        pool.map(wrapped_fetch, urls)
        
    print(f"并发(限流3)总耗时: {time.time() - start:.2f} 秒")

if __name__ == "__main__":
    urls = [f"网页{i}" for i in range(1, 6)] # 准备5个任务
    print("--- 开始同步执行 ---")
    run_sync(urls)
    print("--- 开始并发执行 ---")
    run_concurrent(urls)