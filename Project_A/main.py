import json
import time
from concurrent.futures import ThreadPoolExecutor
from logger import get_logger
from notifier import Notifier

# 初始化日志记录器
log = get_logger("ProjectA")

def main():
    log.info("--- 开始巡检日志 ---")
    
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    rules = config["rules"]
    alert_messages = []
    
    with open(config["log_file"], "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            for rule in rules:
                if rule.lower() in line.lower():
                    alert_messages.append(f"发现异常[{rule}]: {line}")
                    
    if not alert_messages:
        log.info("✅ 日志正常，未发现异常。")
        return

    log.warning(f"⚠️ 共发现 {len(alert_messages)} 条异常，准备并发发送告警...")
    
    start_time = time.time()
    channels = ["钉钉机器人", "飞书机器人", "企业微信"]
    
    with ThreadPoolExecutor(max_workers=3) as pool:
        for channel in channels:
            # 实例化 Notifier 类
            notifier = Notifier(channel)
            pool.submit(notifier.send, f"共{len(alert_messages)}条异常，详情请查看日志")

    log.info(f"--- 告警发送完毕，总耗时: {time.time() - start_time:.2f} 秒 ---")

if __name__ == "__main__":
    main()