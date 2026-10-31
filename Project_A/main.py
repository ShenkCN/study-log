import json
import time
import argparse
from concurrent.futures import ThreadPoolExecutor
from logger import get_logger
from notifier import Notifier

# 初始化日志记录器
log = get_logger("ProjectA")

def main():
    # 1. 解析命令行参数
    parser = argparse.ArgumentParser(description="日志巡检与并发告警工具 v2")
    parser.add_argument("--log_file", type=str, default="app.log", help="要巡检的日志文件路径，默认 app.log")
    parser.add_argument("--rules", type=str, default="ERROR,timeout,OOM", help="巡检规则，逗号分隔")
    args = parser.parse_args()
    
    log.info(f"--- 开始巡检日志: {args.log_file} ---")

    # 2. 处理规则参数
    rules = [r.strip() for r in args.rules.split(",") if r.strip()]
    if not rules:
        log.warning("未提供有效规则，回退到默认规则")
        rules = ["ERROR", "timeout", "OOM"]

    alert_messages = []

    # 3. 读取日志文件 (加入了 try...except 异常兜底)
    try:
        with open(args.log_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                for rule in rules:
                    if rule.lower() in line.lower():
                        alert_messages.append(f"发现异常[{rule}]: {line}")
    except FileNotFoundError:
        log.error(f"找不到文件: {args.log_file}，请检查路径是否正确！")
        return  # 文件找不到，直接退出函数

    if not alert_messages:
        log.info("✅ 日志正常，未发现异常。")
        return

    log.warning(f"⚠️ 共发现 {len(alert_messages)} 条异常，准备并发发送告警...")
    
    # 4. 并发发送告警
    start_time = time.time()
    channels = ["钉钉机器人", "飞书机器人", "企业微信"]
    
    with ThreadPoolExecutor(max_workers=3) as pool:
        for channel in channels:
            notifier = Notifier(channel)
            pool.submit(notifier.send, f"共{len(alert_messages)}条异常，详情请查看日志")

    log.info(f"--- 告警发送完毕，总耗时: {time.time() - start_time:.2f} 秒 ---")

if __name__ == "__main__":
    main()