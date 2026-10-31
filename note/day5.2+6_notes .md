🚀 Day 5.2 + Day 6 总结：从“排队”到“并发”，从“脚本”到“工程化”
日期：2026年10月30日
当前坐标：35天 AI 转型计划 - Day 5.2 & Day 6
目标定位：AI运维工程师 / LLMOps
状态：✔ 实战打通并发与模块化，拿下 90 分与 85 分高分考核！

🎯 一、今日战果（产出清单）
今天我们把前 5 天的碎片知识，彻底拼成了一个真正的“大厂级”小项目。告别了 IDLE 的儿童三轮车，换上了 VS Code 装甲车：

环境大升级：成功配置 VS Code，遇到 ModuleNotFoundError，自己学会了在终端里激活 venv 并选择正确的解释器，告别全局污染。

D5.2 并发实战：跑通了 real_concurrent.py，用 5 个线程并发请求百度、B站等 5 个真实网站，加了 Semaphore(3) 限流，总耗时仅 0.50 秒！

D6 项目A v1 (日志巡检与告警)：成功产出模块化工程结构：

config.json：存放规则配置（支持 ERROR, timeout, OOM 等）。

logger.py：封装了标准日志，带精准时间戳和级别。

notifier.py：封装了 Notifier 类，把发送告警的渠道抽象成对象。

main.py：总控室。读取日志 -> 匹配规则 -> 封装成多个线程 -> 并发发送告警，避免告警风暴。

🧠 二、知识图谱（学到了什么）
并发 vs 限流：并发就像开了多个打饭窗口，而 Semaphore 就是排队号码牌。不设限，会把对方服务器打崩（返回 429 Too Many Requests）；设了限，既能快，又能保护下游。

鉴权 (Authentication)：调用 API 必须带 headers = {"Authorization": "Bearer sk-xxx"}。这就像通行证，而且必须保密，不能硬编码传到 GitHub，要放在配置里。

模块化解耦（乐高思维）：main.py 只管调度，logger.py 只管记录，notifier.py 只管发送。任何一个模块坏了，或者想新增一个“短信告警”，都只改局部，不牵一发而动全身。

上下文管理器 (with)：不管代码是否报错，退出 with 块时一定会触发 __exit__，自动关闭文件、释放信号量锁。

💣 三、踩坑与排雷（程序员的日常）

日志与 print 并存：一开始在代码里混用 print 和 logger，显得很乱。最后把 main.py 里的 print 全部替换为 logger.info 和 logger.warning，终端的输出瞬间清爽专业了。