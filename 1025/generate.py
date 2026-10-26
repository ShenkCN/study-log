# 生成 200 行假日志的代码
import random

levels = ["INFO", "WARNING", "ERROR"]
messages = ["connection refused", "timeout", "disk full", "login success"]

with open("sample.log", "w", encoding="utf-8") as f:
    for _ in range(200):
        level = random.choice(levels)
        msg = random.choice(messages)
        f.write(f"[{level}] {msg}\n")

print("成功生成 sample.log 文件！")
