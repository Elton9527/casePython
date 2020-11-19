import time

print("本地时间为,时间戳：", time.time())

# 格式化时间
localtime=time.asctime(time.localtime(time.time()))
print("本地时间：", localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#获取某月日历
import calendar
cal=calendar.month(2020,11)
print(cal)

# --------------------------- 函数 ------------------------------------
def printme(str):
    # "打印传入的字符串到标准显示设备上"
    print(str)
    return
printme("戴戴")

def ChangeInt(a):
    a = 10
    return a
b = 2
ChangeInt(b)
print(b)
print(ChangeInt(b))

# 不定长参数
def printinfo( arg1, *vartuple):
    print("输出：")
    print(arg1)

    for var in vartuple:
        print(var)
    return
printinfo(10)
printinfo(10, 2, 3, 4, 5)

# 匿名函数 lambda
sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为：", sum(10, 20))
