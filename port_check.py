import socket

# 定义一个函数，用来检查某个 IP 的某个端口
def check_port(ip, port):
    print(f"正在探测 {ip} 的 {port} 端口...")
    
    # 创建一个网络连接（就像拿起电话）
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # 设定超时时间，1秒钟没回应就算失败，防止卡死
    
    try:
        # 尝试连接 (0 代表成功，其他数字代表失败)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"✅ 成功！{port} 端口是开放的！")
        else:
            print(f"❌ 失败！{port} 端口没开。")
    except Exception as e:
        print(f"探测出错：{e}")
    finally:
        s.close() # 挂断电话

# 试试探测你自己电脑的 3306 端口（通常是 MySQL 数据库）
# 如果以后你有了自己的云服务器，把 "127.0.0.1" 换成你的公网 IP 就能扫真实的服务器了
check_port("127.0.0.1", 3306)
