# 创建人：gw
# 开发时间：2022/6/27 4:08

"""
循环结构：反复做同一件事的情况
      while：语法 while 条件表达式：  条件执行体   一共判断n+1次，执行n次
      for-in：
             in表达从（字符串、序列等）中依次取值，又称为遍历
             for-in遍历的对象必须是可迭代对象
             语法结构： for 自定义的变量 in 可迭代的对象： 循环体
             若循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
"""
#while示例
a = 1
while a < 10:
    print(a)
    a += 1
"""
4步循环法
     1.初始化变量
     2.条件判断
     3.条件执行体
     4.改变变量
     注意：初始化的变量与条件判断的变量与改变的变量为同一个
"""
# 计算0到4之间的累加和
sum1 = 0
a = 0   # 初始化变量为0
while a < 5:   # 条件判断
    # 条件执行体
    sum1 += a
    a += 1  # 改变变量
print('the sum form 0 to 4 is:', sum1)
#练习题：计算0到100之间的偶数和
sum1 = 0
a = 0
while a <= 100:
    sum1 += a
    a += 2
print('0到100之间的偶数和为：', sum1)


#for-in循环示例
for item in 'python':
    print(item)

for i in range(10):
    print(i)

for _ in range(3):
    print('I love you like love somebody')

# 用for循环计算1到100的偶数和
sum2 = 0
for t in range(1, 101):
    if t % 2 == 0:
        sum2 += t
print('0到100之间的偶数和为：', sum2)

# 练习:100到999之间的水仙花数.水仙花数：个位数的三次方加上十位数的三次方加上百位数的三次方和这个数相等，如153 = 1*1*1+5*5*5+3*3*3
for SXH in range(100, 999):
    ge = SXH % 10     # 个位
    shi = (SXH % 100) // 10   # 十位
    bai = SXH // 100     # 百位
    if SXH == ge ** 3 + shi ** 3 + bai ** 3:
        print(SXH)

