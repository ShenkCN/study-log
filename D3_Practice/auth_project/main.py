import json
import logger
import parser

def run():
    log = logger.get_logger()
    log.info("程序开始启动...")
    
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        
    log.info(f"正在分析文件：{config['log_file']}，匹配关键字：{config['keyword']}")
    
    try:
        result = parser.analyze_log(config['log_file'], config['keyword'])
        log.info("解析完成！战报如下：")
        
        for ip, count in result.items():
            log.warning(f"🚨 发现恶意 IP：{ip}，攻击了 {count} 次！")
            
    except FileNotFoundError:
        log.error("找不到日志文件，请检查路径！")

if __name__ == '__main__':
    run()
