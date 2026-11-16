# 日志巡检与并发告警工具 (Project A v2)

## 1. 项目简介
这是一个基于 Python 开发的自动化运维工具。它能够读取指定的日志文件，根据配置规则（如 ERROR、timeout、OOM）匹配异常，并在发现异常时，通过多线程并发同时向多个渠道（钉钉、飞书、企微）发送告警，避免告警风暴，提升运维响应速度。

## 2. 技术栈
- 语言：Python 3.11
- 并发控制：`concurrent.futures.ThreadPoolExecutor`
- 日志系统：`logging` 模块定制化输出
- 命令行解析：`argparse`
- 自动化测试：`pytest` + `pytest-cov`

## 3. 目录结构
- `main.py`：核心业务逻辑、参数解析与并发调度
- `logger.py`：统一日志格式化输出
- `notifier.py`：通知渠道的面向对象封装
- `config.json`：巡检规则配置
- `app.log`：测试用模拟日志
- `test_main.py`：自动化单元测试

## 4. 快速开始 (Quick Start)
1. 确保已安装 Python 3.8+
2. 激活虚拟环境并安装依赖：
   ```bash
   .\venv\Scripts\activate
   pip install -r requirements.txt