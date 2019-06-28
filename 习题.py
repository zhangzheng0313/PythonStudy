# 1、编写程序，要求用户输入1-100之间的整数并且判断，输入符合要求打印“正确”，否则打印“错误”
"""
temp = input("请输入一个1-100之间的整数：")
if temp.isdigit():
    temp = int(temp)
    if 1 <= temp <= 100:
        print("正确")
    else:
        print("错误")
else:
    print("错误")
"""

# 2、判定给定年份是否为闰年
'''
year = input("请输入年份：")
if year.isdigit():
    year = int(year)
    if year % 4 == 0:
        print(str(year) + "是闰年")
    else:
        print(str(year) + "不是闰年")
else:
    print("让你输入年份！")
'''


# 3、给用户3次机会，猜想程序生成的一个数字A，每次用户猜想后会提示数字是否正确以及用户输入的数字是大于A还是小鱼A，当机会用尽后会提示用户输掉游戏
'''
import random
A = random.randint(1,100)
times = 3
while times:
    num = input("请输入数字：")
    if num.isdigit():
        tmp = int(num)
        if tmp == A:
            print("你猜对了！")
            break
        elif tmp < A:
            print("你输入的数字小了")
 #           times = times - 1
        else:
            print("你输入的数字大了")
 #           times = times - 1
    else:
        print("让你输入数字呢")
#print("你的机会用完了")
'''


# 4、打印0-100所有奇数
'''
ls = range(0,101)
for i in ls:
    print(i)
'''


# 5、爱因斯坦阶梯
'''
x = 0
while x < 1000:
    if (x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5) and (x % 7 == 0):
        print(x)
        break
    else:
        x += 1
print("循环结束")
'''


# 6、x=1,y=2,z=3,如何快速交换他们的值
'''
x = 1
y = 2
z = 3
x, y ,z = z, x, y
print(x)
print(y)
print(z)
'''


# 7、验证用户密码，用户只有三次输入机会不过用户输入内容包括“*”则不计算在内
'''
password = "123456"
times = 3
while times:
    input_password = input("请输入密码：")
    if '*' in input_password:
        print("密码中不能包含“*”")
    elif input_password == password:
        print("密码正确")
        break
    else:
        print("密码错误")
        times = times - 1
        print("你还有{0}次机会".format(times))
    if times == 0:
        print("三次机会已用完")
'''


# 8、简单图形打印
'''
打印以下图形
* * * * *
* * * * *
* * * * *
* * * * *
'''
'''
for i in range(0,4):
    for x in range(0,5):
        print("*", end=" ")
    print()
'''


# 9、打印以下图形
'''
* * * * * 
*       * 
*       * 
* * * * *
'''
'''
for i in range(4):
    if i == 0 or i == 3:
        print("* " * 5)
    if i == 1 or i == 2:
        for j in range(5):
            if j == 0 or j == 4:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
'''


# 10、打印以下图形
'''
* 
* * 
* * * 
* * * * 
* * * * *
'''
'''
for i in range(5):
    for j in range(i + 1):
        print("* ", end="")
    print()
'''


# 11、打印空心三角形
'''
for i in range(5):
    for j in range(i + 1):
        if i == 4:
            print("* ", end="")
            continue
        if j == 0 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
'''


# 12、打印倒立三角
'''
for i in range(5):
    for j in range(5 - i):
        print("* ", end="")
    print()
'''


# 13、打印倒空三角
'''
for i in range(5):
    for j in range(5 - i):
        if i == 0:
            print("* ", end="")
            continue
        if j == 0 or j == 5-i-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
'''


# 14、打印正三角形
'''
for i in range(5):
    for j in range(5-i):
        print(" ", end="")
    for m in range(i+1):
        print("* ", end="")
    print()
'''


# 15、打印空三角
'''
for i in range(1, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(6-i, 6):
        if i == 5 or j == 6-i or j == 5:
            print("* ", end="")
        else:
            print(" ", end=" ")
    print()
'''


# 16、求100-999之间所有的水仙花数（即一个3位数等于其各位数字的立方和）
'''
for i in range(100,1000):
    temp = str(i)
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    if a**3 + b**3 + c**3 == i:
        print(i)
'''


# 17、红黄蓝三色球，红球3个，黄球3个，绿球6个，从中任意摸出8个球，计算摸出求的各种颜色搭配
'''
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                print("红球有{}个".format(red))
                print("黄球有{}个".format(yellow))
                print("绿球有{}个".format(green))
                print("="* 10)
'''


# 18、登录注册
'''
user_pass = {"zhangzheng":"123", "chenyi":"123"}


def creat_user(username, password):
    usernames = user_pass.keys()
    if username in usernames:
        print("该用户名已经被注册")
    else:
        user_pass[username] = password
        print("注册成功")


# creat_user("ergou", 123)
# print(user_pass)


def login_user(username, password):
    usernames = user_pass.keys()
    if username not in usernames:
        print("你还没有注册")
    elif password != user_pass[username]:
        print("密码错误")
    else:
        print("登录成功")


login_user("chenyi", "123")
'''


# 19、汉诺塔
'''
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
hanoi(2, 'A', 'B', 'C')
'''