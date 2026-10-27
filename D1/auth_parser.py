# 3.1在循环外面，准备一个空字典
ip_counts = {}

# 1.0.在这个文件里写
with open("auth.log", "r", encoding="utf-8") as f:
    for line in f:
        if "Failed" in line:
# 1.1如果 "Failed" 在 line 里面
#       if "Failed" in line:
#        print(line.strip())  # strip() 用来去掉行尾的换行符
            
            # 2.1. 把整行按空格切开，变成列表 parts
            parts = line.split(" ")
            
            # 2.2. 找到 "from" 这个单词在列表里的索引位置
            from_index = parts.index("from")
            
            # 2.3. 取出 "from" 后面的那个元素（索引 + 1）
            ip = parts[from_index + 1]

            # 3.2. 核心统计逻辑（复习昨天的字典计数法）
            # 3.3  如果 IP 不在字典里，默认给 0，然后 +1
            ip_counts[ip] = ip_counts.get(ip,0) + 1
            
            
            print("===抓取到的黑客IP 攻击统计===")
            print(ip_counts)

for key_ip, count in ip_counts.items():
    print(f"{key_ip} 攻击了 {count} 次！")
