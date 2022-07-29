# 创建人：gw
# 开发时间：2022/7/5 14:48
"""
else语句
       三种使用情况：
                  1.if...else...（if条件表达式不成立时执行else）
                  2.while...else...
                  3.for...else...（没有碰到break时，循环正常结束，执行else）
"""

"""
嵌套循环：循环结构中嵌套了另外的完整循环结构，其中内层循环作为外层循环的循环体执行.
        当嵌套循环中有break和continue，只用于控制当前层的循环结束
"""
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')  # 不换行输出
    print()


#输出九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print(''+str(y)+'*'+str(x)+'='+str(x*y)+'', end='\t')
    print()
