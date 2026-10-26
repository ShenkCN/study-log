🚀 Day 1 总结：破冰与筑基（P1 阶段：Python 工程化）

日期：2026年10月25日

当前坐标：35天 AI 转型计划 - Day 1

目标定位：运维底盘 + AI 工程（AI运维/LLMOps/AI应用交付）



🎯 一、今日战果（产出清单）

成功搭建了 Python + Git 的开发环境，并完成了首个 study-log GitHub 仓库的代码提交。

今天手敲并跑通了 4 个核心脚本（已上传至 GitHub）：



generate.py：随机生成 200 行模拟服务器日志。



log\_counter.py：读取日志并统计不同级别（INFO, WARNING, ERROR）的出现次数。



port\_check.py：使用 socket 模块检测本机端口开放情况。



read\_config.py：读取 config.json 配置文件并提取参数。



环境及测试文件：

config.json, log\_counter\_analyze.py (函数封装版), sample.log, test.py, test.txt。



🧠 二、知识图谱（学到了什么）

基础语法：变量、字符串切片（掌握了核心的“包左不包右”原则）、f-string 格式化、类型转换（int(), float()）。



控制流与结构：if...elif...else 条件判断、for...in... 循环遍历。



数据结构：list（列表，用 append 追加）、dict（字典，键值对存储和提取）、set（集合）。



文件操作：with open() 上下文管理器，掌握了 "w"（清空覆写）和 "r"（读取）模式。



工具链：Git 本地初始化、add/commit/push 三连击，以及 SSH 授权和 IDLE 清屏操作。



💣 三、踩坑与排雷（程序员的日常）

今天踩爆了无数新手必踩的坑，但都一一解决了：



中英文符号问题：输入法没切干净，中文双引号、单引号导致各种 SyntaxError。



JSON 解析失败：复制代码时不小心多带了 json 字母，导致 JSONDecodeError。



变量未清零：计算 1 到 100 的和时，total 忘记重置，结果算出了两遍总和（10100）。



print 被覆盖：手贱写了 print = "你好"，把系统自带的函数给覆盖了，导致后面一直报错 TypeError: 'str' object is not callable。



数据类型遍历报错：尝试用 for t in total: 去遍历一个整数，报错 TypeError: 'int' object is not iterable。



文件路径与后缀：忘记加 .py 或 .txt 后缀导致 FileNotFoundError。



📝 四、考核复盘（20 道单选测验）

首轮成绩：8/20（凭直觉答题，暴露了大量细节盲区）



二轮重考成绩：17/20（正确率 85%）



错题教训：



文件模式 "w" 会清空原文件，追加应该用 "a"。



len() 函数不仅能数字符串长度，还能数列表元素个数。



切片 \[:5] 取的是前 5 个字符，不包含第 6 个（冒号）。



💡 五、Shenk 的心得体会

“万事开头难，编程绝对不是靠‘背’的。今天最初连 (100+50)\*2/3 都不知道往哪敲，到后面能自己发现 total 变量忘记清零的 Bug，并推导出 print() 会脱去字符串伪装直指本质。我发现只要理解逻辑，搞懂变量和容器的层级关系，代码其实很有灵性。 今天我的黑框框里全是红字报错，但我一点都不慌，因为我知道这就是排障的过程。”



🔮 六、明日预告（D2）

核心任务：深入数据结构（list/dict/set/tuple）与字符串高阶方法。



项目实战：解析真实的服务器 auth.log 登录日志，找出失败登录次数最多的 TOP 10 IP（黑客追踪剧本）。



八股文：可变/不可变对象、深浅拷贝。



“你的最优区间是AI运维/LLMOps/AI应用交付，用运维底盘+AI工程去打错位竞争。” —— 摘自《Shenk 2026-2027 职业规划》



