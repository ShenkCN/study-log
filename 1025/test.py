#open("test.txt", "r")

#with open("test.txt", "w", encoding="utf-8") as f:
#   f.write("Hello Ops")


with open( "test.txt","r",encoding="utf-8")as f:
    content = f.read()
    print(content)
