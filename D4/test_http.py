from http_client import HttpClient
import time

# 1. 实例化对象（最多重试 2 次，超时设为 2 秒）
client = HttpClient(timeout=2, max_retries=2)

print("\n--- 测试一：正常的公开接口 ---")
# 请求一个真实的网站（httpbin 是专门用来测试的网站）
res = client.request("GET", "https://httpbin.org/get")
if res:
    print("拿到数据了，数据长度：", len(res.text))

print("\n--- 测试二：故意超时的接口 ---")
# 这个接口会让服务器硬等 5 秒才返回，但我们客户端设置的是 2 秒超时
res2 = client.request("GET", "https://httpbin.org/delay/5")
if not res2:
    print("测试二：果然超时重试失败了，符合预期！")
