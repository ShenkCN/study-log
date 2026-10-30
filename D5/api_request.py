import requests

# 真实请求必须带请求头（Headers），'Authorization' 就是通行证
headers = {
    "Authorization": "Bearer 你的DeepSeek_API_KEY_写在这里",  # 真实场景千万别把密码传到 GitHub！
    "Content-Type": "application/json"
}

# 1. 测试一下不用通行证能不能查天气（公开接口）
print("--- 正在测试公开 API ---")
response = requests.get("https://httpbin.org/get", timeout=5)
# 200 代表成功
print(f"状态码: {response.status_code}, 返回数据: {response.json()['headers']}")