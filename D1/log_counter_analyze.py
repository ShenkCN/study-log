# 定义一个叫做 analyze_log 的盒子
def analyze_log():
    # 这里的代码是从你截图里原封不动搬过来的
    count_dict = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    with open("sample.log", "r", encoding="utf-8") as f:
        for line in f:
            if "INFO" in line:
                count_dict["INFO"] += 1
            elif "WARNING" in line:
                count_dict["WARNING"] += 1
            elif "ERROR" in line:
                count_dict["ERROR"] += 1
                
    print("统计结果：", count_dict)

# 只有写了下面这句，这个盒子才会被真正启动
analyze_log()
