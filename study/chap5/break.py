# 创建人：gw
# 开发时间：2022/7/5 13:50


"""
break语句：用于结束循环结构，通常与if一起使用
"""
#从键盘录入密码，如果正确则结束，最多录入3次
for item in range(3):
    pwd = input('pls input your password:')
    if pwd == 'password':
        print('right password')
        money = 10000
        costMoney = int(input('pls input how much money you want to take:'))
        if costMoney <= money:
            leftMoney = money - costMoney
            print('there are ' + str(leftMoney) + ' yuan left')
        else:
            print('you do not have so much money')

        break
    else:
        lefttimes = 2-item
        if lefttimes == 0:
            print('you have no chance anymore. pls find the workers in bank')
        else:
            print('wrong password.pls input your password again.only '+str(lefttimes)+' times left.')
