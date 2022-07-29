# 创建人：gw
# 开发时间：2022/6/26 11:16


"""
input()
     作用：接收来自用户的输入
     返回值类型：输入值的类型为str
     值的存储：使用 = 对输入的值进行存储
"""
#示例
# present = input('生日想要什么礼物？')
# print(present, type(present))
#练习题：要求在键盘区输入两个整数，并求这两个数的和
s1 = input('第一个数:')
s2 = input('第二个数:')
s3 = int(s1) + int(s2)
print('the sum is '+str(s3)+'')
"""
s1 = int(input('第一个数:'))
s2 = int(input('第二个数:'))
print('the sum is :'+str(s1+s2)+''),
"""


