import time

class Notifier:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        
    def send(self, message):
        # 真实场景这里会是 requests.post()
        time.sleep(0.5)
        print(f"🚨 【{self.channel_name}】告警已发送: {message}")
