#str = input("请输入：")
#print("你输入的内容是:", str)

# 打开和关闭文件
fo = open("test.txt", "w")
fo.write("This taste is very nice \nI like it very much!")

# read() 方法从一个打开的文件中读取一个字符串
fo1 = open("test1.txt", "r")
print(fo1.name)
for line in fo1.readlines():
    print(line)
fo1.close()