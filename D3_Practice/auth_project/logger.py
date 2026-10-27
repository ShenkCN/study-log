import logging

def get_logger():
    logger = logging.getLogger("AuthLogger")
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # 防止重复添加，避免日志打印两遍
    if not logger.handlers:
        logger.addHandler(console_handler)
    
    return logger
