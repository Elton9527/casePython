# 1.基础语法

# 变量 数据类型(数字 字符串 列表 元祖 字典)
counter = 100
print(counter)

a = b = c = 1
print(a, b, c)

name = "John"
print(name)

# 字符串
# 格式: str[begin:end:step]
# str,字符串.
# begin,起始位置.
# end,结束位置.
# step,间隔.s不等于0.默认为1
# 注:
# 区间为左闭右开.
# step>0,表示从左往右.
# step<0,表示从右往左.
str = "abcdefghijklmn"
print(str[0:3])
print(str[-1:-5:-1])
print(str[-3::-4])

# 元祖
tuple = ('Elton', 123, 33.33, 'John', 80.3)
tinytuple=(125, 'Mona', 123)
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tinytuple + tuple)

# 字典
dict = {}
dict['a'] = "This is one"
dict[2] = "This is two"

tinydict = {'name':'elton', 'age':30}

print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())


# 算术运算符
# ** 返回x的y次幂
print(2**3)
# // 取整除，返回商的整数部分（向下取整）
print(9//2)

# 成员运算符
# in | not in
a = 10
b = 20
a_list = [1, 2, 3, 4, 5]

if (a in a_list):
    print("变量a在给定的列表中")
else:
    print("变量a不在给定的列表中")

a = 2
if (a in a_list):
    print("变量a在给定的列表中")
else:
    print("变量a不在给定的列表中")

# is | is not 判断两个标识符是不是引用自一个对象
# is 用于判断两个变量引用对象是否为同一个(同一块内存空间) == 用于判断引用变量的值是否相等
a = 20
b = 20
if (a is b):
    print("a和b有相同的标识")
else:
    print("a和b没有相同的标识")

# for 循环语句，遍历任何序列的项目，如一个列表或者一个字符串
for letter in 'Python':
    print(letter)

fruits = ['apple', 'pear', 'mango']
for fruit in fruits:
    print('当前水果:', fruit)


# pass 是空语句，是为了保持程序结构的完整性，pass不做任何事，一般用作占位语句

for letter in 'Python':
    if letter == 'h':
        pass
        print('这是个占位')
    print('当前字母：', letter)
print('Good Bye')
