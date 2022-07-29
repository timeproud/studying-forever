# 创建人：gw
# 开发时间：2022/6/27 3:51

"""
range()函数
        用于生成一个整数序列
        创建range对象的三种方式
                  range(stop):从0开始，到stop结束，步长为1
                  range(start,stop):从start开始，到stop结束，步长为1
                  range(start,stop，step):从start开始，到stop结束，步长为step
        返回值是一个迭代器对象
        优点：不管对象表示的整数序列有多长，所有对象占用的内存空间都是相同的，因为仅仅需要存储start、stop、step，只有当用到range对象时，才会去计算序列中的相关元素
        可以用in、 not in 来判断整数序列中是否存在（不存在）指定的整数
"""
r = range(10)
print(r)
print(list(r))    # list可以用于查看range对象中的整数序列
r = range(1,10)
print(list(r))
r = range(1,10,5)
print(list(r))

print(10 in r)    # 判断整数是否在序列中
print(1 in r)