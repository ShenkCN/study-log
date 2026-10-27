# 全局变量（外面的公共大厅）
global_money = 1000

def my_function():
    #局部变量（我自己的房间）
    local_money = 50
    print("函数内部能看到：",local_money)
    print("函数内部也能看到外部的：",global_money)


my_function()
