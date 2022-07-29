# 创建人：gw
# 开发时间：2022/6/26 22:30


"""
选择结构：程序根据判断条件的布尔值选择性地执行部分代码，明确地让计算机知道在什么条件下，该去做什么
       单分支结构：如果...就...   语法：if 条件表达式：条件执行体
       双分支结构：如果...就...否则，就...   语法：if 条件表达式：条件执行体1 else：条件执行体2
       多分支结构：语法：if 条件表达式1：条件执行体1  elif 条件表达式2：条件执行体2  elif 条件表达式n：条件执行体n 【else：】条件执行体n+1
       if的嵌套：if语句中嵌套if语句
       条件表达式：if...else...的简写
"""
# money = 1000
# s = int(input('请输入取款金额'))  # 取款金额
# #判断余额是否充足
# if money >= s:
#     money = money - s
#     print('取款成功，余额为：', money)
# else:
#     print('余额不足')

#多分支结构
"""
从键盘录入一个成绩：90-100，A；80-89，B；70-79，C；60-69，D；0-60，F
小于0或者大于100为非法数据（不是成绩）
"""
# score = int(input('pls input a score:'))  # 输入成绩
# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score <= 89:
#     print('B')
# elif 70 <= score <= 79:
#     print('C')
# elif 60 <= score <= 69:
#     print('D')
# elif 0 <= score <= 59:
#     print('F')
# else:
#     print('成绩有误')
# 条件表达式
num_a = int(input('the first number is:'))
num_b = int(input('the second number is:'))
# print('the first one is bigger' if num_a >= num_b else 'the second one is bigger')
print(str(num_a)+' >= '+str(num_b) if num_a >= num_b else str(num_b)+' >= '+str(num_a))

"""if语句可以直接判断对象的布尔值"""
age = int(input("输入年龄："))
if age:
    print('the age is:',age)
else:
    print('刚出生')
