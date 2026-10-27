# 1. 准备一个字典，用来存计数
# 为什么初始值是 0？因为如果日志里没有这一行，我们也要显示 0
count_dict = {"INFO": 0, "WARNING": 0, "ERROR": 0}

# 2. 打开我们刚才生成的 sample.log 文件
# "r" 代表只读，encoding="utf-8" 防止中文乱码（虽然我们造的是英文，但这是个好习惯）
with open("sample.log", "r", encoding="utf-8") as f:
    
    # 3. 逐行读取
    for line in f:
        
        # 4. 检查这行文字里有没有关键词
        if "INFO" in line:
            count_dict["INFO"] += 1   # 也可以写成 count_dict["INFO"] = count_dict["INFO"] + 1
            
        elif "WARNING" in line:
            # 请在这里补全 WARNING 的统计代码
            count_dict["WARNING"] += 1  
            
        elif "ERROR" in line:
            # 请在这里补全 ERROR 的统计代码
            count_dict["ERROR"] += 1  

# 5. 循环结束后，打印最终结果
print("统计结果：", count_dict)
