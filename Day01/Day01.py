# num = "秦淮"
# age = 18
# job = "学生"
# print(f"我的名字是{num}, 我今年{age}岁了,我是一名{job}" )

# 输入与输出
# name = input("请输入你的名字:")
# age = input("请输入你的年龄:")
# job = input("请输入你的职业:")
# print(f"我的名字是{name}, 我今年{age}岁了,我是一名{job}" )

# 银行取钱案例
# base = 10000
# s1 = input ("请输入取钱金额:")
# s2 = input ("请输入取钱密码:")
# money = base - int(s1)
# s3 = input (f"您已经取款{int(s1)}元，您的余额还有{money}元")

# if条件判断
# score = 690
# if score > 680:
#     print("恭喜你被清华大学录取了！")

#if案例
# ID = 2658602223
# password = "13579a"
# s1 = input("请输入你的账号:")
# s2 = input("请输入你的密码:")
# if s1 ==  str(ID) and s2 == password:
#     print("登录成功！")
# else:
#     print("登录失败！")

#三角形判断，根据输入的三边长判断是等边三角形、等腰三角形、普通三角形还是无法构成三角形
# a = int(input("请输入三角形的第一条边长:"))
# b = int(input("请输入三角形的第二条边长:"))
# c = int(input("请输入三角形的第三条边长:"))
# if a == b == c:
#     print("这是一个等边三角形") 
# elif a == b or a == c or b == c:
#     print("这是一个等腰三角形")
# elif  a + b > c and a + c > b and b + c > a:
#     print("这是一个普通三角形")
# else:
#     print("无法构成三角形")

#match案例
# day = input("请输入日期:")
# match day:
#     case "1":
#         print("今天是周一")
#     case "2":
#         print("今天是周二")
#     case "3":
#         print("今天是周三")
#     case "4":
#         print("今天是周四")
#     case "5":
#         print("今天是周五")
#     case "6":
#         print("今天是周六")
#     case "7":
#         print("今天是周日")
#     case _:
#         print("输入错误，请重新输入！")

#通过match语句实现一个简单的计算器，用户输入两个数字和一个运算符，程序根据运算符进行相应的计算并输出结果。
# num1 = float(input("请输入第一个数字:"))
# num2 = float(input("请输入第二个数字:"))
# operator = input("请输入运算符（+、-、*、/）:")
# match operator:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/":
#         if int(num2) != 0:
#             print(f"{num1} / {num2} = {num1 / num2}")
#         else:
#             print("除数不能为零！")
#     case _:
#         print("输入错误，请重新输入！")

#for循环
msg  = "Hello, World!"
s = 1
for i in msg:
    print(i)
    s = s + 1
    if  i == "r":
        break
print(s)
    