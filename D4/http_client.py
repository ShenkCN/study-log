import time
import logging
import requests

# 配置日志（借用你昨天学的知识）
logger = logging.getLogger("HttpClient")
logger.setLevel(logging.INFO)
if not logger.handlers:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


class HttpClient:
    def __init__(self, timeout=5, max_retries=3):
        """
        初始化方法：就像出厂设置
        """
        self.timeout = timeout
        self.max_retries = max_retries
        # Session 就像是一个会话池，它能自动保持连接、复用 TCP，比每次直接 requests.get() 快很多
        self.session = requests.Session() 
        
    def request(self, method, url, **kwargs):
        """
        核心方法：发送网络请求，自带重试、超时和日志功能
        """
        # 把方法名转成大写（比如传 get 变成 GET）
        method = method.upper()
        
        # 重试循环机制
        # 比如 max_retries=3，那么 range 就是 0,1,2，最多尝试 3 次
        for attempt in range(self.max_retries):
            try:
                logger.info(f"正在发起请求：{method} {url} (第 {attempt + 1} 次尝试)")
                
                # 记录开始时间
                start_time = time.time()
                
                # 发送请求！
                response = self.session.request(
                    method=method, 
                    url=url, 
                    timeout=self.timeout, 
                    **kwargs
                )
                
                # 计算耗时
                elapsed = time.time() - start_time
                
                # 如果 HTTP 状态码不是 200 左右（比如 404, 500），主动抛出异常
                response.raise_for_status()
                
                logger.info(f"✅ 请求成功！状态码：{response.status_code}，耗时：{elapsed:.2f}秒")
                return response
                
            except requests.exceptions.Timeout:
                logger.warning(f"⚠️ 请求超时！已经等了 {self.timeout} 秒。")
            except requests.exceptions.RequestException as e:
                logger.error(f"❌ 网络异常：{e}")
            
            # 如果这不是最后一次尝试，那就睡一会儿再重试
            if attempt < self.max_retries - 1:
                logger.info("等待 1 秒后重试...")
                time.sleep(1)
                
        # 如果循环结束还没 return，说明彻底失败了
        logger.error(f"💀 彻底失败：已达到最大重试次数 {self.max_retries}。")
        return None
