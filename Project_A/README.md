# Project A: 日志巡检与并发告警工具 v1

## 1. 项目简介
这是一个基于 Python 开发的自动化日志巡检工具。它能够读取指定的日志文件，根据配置文件中定义的规则（如 ERROR、timeout、OOM）匹配异常，并在发现异常时，通过并发多线程同时向多个渠道（如钉钉、飞书）发送告警，避免告警风暴。

## 2. 技术栈
- Python 3.11
- 并发控制：`concurrent.futures.ThreadPoolExecutor`
- 日志系统：Python 内置 `logging` 模块
- 面向对象：基于类封装通知器（Notifier）
- 配置分离：使用 `json` 进行配置管理

## 3. 目录结构
- `main.py`：核心业务逻辑与并发调度
- `logger.py`：统一日志格式化输出
- `notifier.py`：通知渠道的面向对象封装
- `config.json`：规则与文件路径配置
- `app.log`：用于测试的模拟日志文件

## 4. 如何运行
1. 激活虚拟环境：`.\venv\Scripts\activate`
2. 安装依赖（本版本无第三方依赖，直接运行即可）
3. 运行主程序：`python main.py`

## 5. 运行效果
（把终端里带时间戳的输出截图放到这里，或者把输出文字复制一段贴在这里）

## 6. 后续优化 (D7计划)
- 增加 `argparse` 支持命令行传参，无需硬编码路径
- 补充 `pytest` 单元测试