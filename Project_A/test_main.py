import sys
from main import main

# 测试 1：测试不存在的文件（异常兜底）
def test_file_not_found(caplog):
    sys.argv = ["main.py", "--log_file", "不存在的文件.txt"]
    main()
    # 断言：检查 caplog 里记录的日志文本，是否包含“找不到文件”
    assert "找不到文件" in caplog.text


# 测试 2：测试正常文件
def test_normal_file(caplog):
    sys.argv = ["main.py", "--log_file", "app.log", "--rules", "ERROR"]
    main()
    # 断言：检查 caplog 里记录的日志文本，是否包含“告警发送完毕”
    assert "告警发送完毕" in caplog.text