# 创建人：gw
# 开发时间：2022/7/17 10:52


"""
集合
   python语言提供的内置数据结构
   与列表、字典一样都属于可变类型的序列
   集合是没有value的字典
   集合是无序的
"""


# 1.集合的创建方式：直接{}，或者使用内置函数set（）
s = {1, 2, 3, 4, 5, 6, 7}  # 直接使用{}创建。集合中元素不允许重复，否则会自动合并为一个
s1 = set(range(6))      # 使用set（）创建
print(s1, type(s1))
s2 = set([1, 2, 2, 3, 5, 5])   # 使用set将列表转为集合，同时去掉其中重复元素
print(s2, type(s2))
s3 = set((1, 2, 98, 7, 2))      # 使用set将元组转为集合，同时去掉其中重复元素
print(s3, type(s3))
s4 = set('python')      # 使用set将字符串转为集合，同时去掉其中重复元素
print(s4, type(s4))
s5 = set()    # 定义空集合，不能直接{}，否则会创建空字典，只能使用set（）或者{‘’}
s6 = {''}
print(type(s5), type(s6))


# 2.集合的相关操作
# 集合元素的判断操作:in 或 not in
print(10 in s)
print(10 not in s)
# 集合元素的新增操作: add()或者update（）
s.add(8)   # 一次添加一个元素
print(s)
s.update({9, 10, 11})   # 一次至少添加一个元素,可以添加集合、元组等
print(s)
# 集合元素的删除操作：remove（）、discard（）、pop（）、clear（）
s.remove(2)   # 一次删除一个指定元素，如果指定元素不存在，则报error
print(s)
s.discard(3)  # 一次删除一个元素，如果指定元素不存在，不会报error
print(s)
s.pop()    # 一次删除一个任意元素
print(s)
s.clear()   # 清空集合
print(s)


# 3.集合间的关系
# 两个集合是否相等：可以使用运算符==或者！=进行判断
print(s == s1)
print(s != s1)
# 一个集合是否是另一个集合的子集：调用issubset进行判断
print(s1.issubset(s2))
print(s2.issubset(s1))
# 一个集合是否是另一个集合的超集：调用issuperset进行判断
print(s1.issuperset(s2))
print(s2.issuperset(s1))
# 两个集合是否没有交集：调用isdisjoint进行判断 (如果没有交集，则为true)
print(s2.isdisjoint(s3))


# 4.集合的数学操作
# 求交集操作
print(s2.intersection(s3))  # 使用intersection()求交集
print(s2 & s3)   # 使用&求交集
# 求并集操作
print(s1.union(s2))  # 使用union（）求并集
print(s1 | s2)      # 使用|求并集
# 求差集操作
print(s2.difference(s3))   # 使用difference（）求差集
print(s2-s3)     # 使用-求差集
# 求对称差集操作
print(s2.symmetric_difference(s3))   # 使用symmetric_difference（）求对称差集
print(s2 ^ s3)    # 使用^求对称差集


# 5.集合生成式
s0 = {i*i for i in range(1, 10)}
print(s0)




"""
数据结构            是否可变           是否重复             是否有序              定义符号
列表（list）         可变              可重复               有序                  []
元组（tuple）       不可变             可重复                有序                 （）
字典（dict）         可变       key不可重复，value可重复      无序               {key:value}
集合（set）          可变             不可重复               无序                  {}
"""




