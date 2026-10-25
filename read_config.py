import json

#打开刚才创建的json文件
with open("config.json", "r", encoding="utf-8") as f:
    #把文本变成python的字典
    config = json.load(f)

    #提取数据并输出
    print("读取成功")
    print(f"服务器IP是: {config['server_ip']}")
    print(f"管理员是: {config['admin']}")
