import time
import requests
from concurrent.futures import ThreadPoolExecutor
import threading

# 复用你 D4 写的请求逻辑（简化版）
def fetch_url(url):
    try:
        # 真实网络请求，超时设为 3 秒
        res = requests.get(url, timeout=3)
        return f"✅ 成功: {url} (状态码: {res.status_code})"
    except Exception as e:
        return f"❌ 失败: {url} (报错: {e})"

urls = [
    "https://www.baidu.com",
    "https://www.bing.com",
    "https://www.qq.com",
    "https://www.taobao.com",
    "https://www.jd.com"
]

def run():
    start = time.time()
    sem = threading.Semaphore(3) # 限流：最多同时3个网站在请求
    
    def wrapped(url):
        with sem:
            print(f"👉 正在请求: {url}")
            return fetch_url(url)

    print("--- 开始并发请求 ---")
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = pool.map(wrapped, urls)
        for res in results:
            print(res)
            
    print(f"全部完成，总耗时: {time.time() - start:.2f} 秒")

if __name__ == "__main__":
    run()