# 创建人：gw
# 开发时间：2022/7/11 21:19


"""
列表：变量可以存储一个元素、列表可以存储很多元素，程序可以对这些元素进行整体操作，相当于C语言中的数组。
    1.列表的创建与删除
    2.列表的查询操作
    3.列表1元素的增删改
    4.列表元素的排序
    5.列表推导式
列表的特点：
    1.列表元素按顺序有序排序
    2.索引映射为唯一一个数据
    3.列表可以存储重复数据
    4.任意数据类型混存
    5.根据需要动态分配和回收内存
"""
# 1.列表的创建与删除
# 创建方式：使用中括号、调用内置函数list（），元素之间使用英文的逗号分隔。
lst = ['hello', 'world', 98]
#索引：  0         1       2
#索引：  -3        -2      -1
lst2 = list(['hello', 'world', 98])  # 两种方式都可以创建列表对象
print(lst[-3])

# 2.列表的查询操作
#   获取列表中指定元素的索引：index():
#   如果列表中存在相同元素的时候，那么只会返回相同元素中第一个元素的索引；
lst3 = ['hello', 'world', 98, 'hello']
print(lst3.index('hello'))
#   可以在指定的start与stop之间进行查找
print(lst3.index('hello', 1, 4))
#   获取列表当中的单个元素：正向索引从0到n-1，负向索引从-n到-1
print(lst3[2])  # 获取索引为2的元素
#   获取列表中的多个元素：切片操作，语法格式   列表名【start：stop：step】，左闭右开，不包含stop,切出来的片段是一个单独的新列表，有单独的id。此外，当步长为负数，则切片的第一个元素是新列表的最后一个元素。
print(lst3[1:3:1])
print(lst3[2:0:-1])
#   判断指定元素在列表中是否存在 元素 in 列表名   元素 not in 列表名
print(98 in lst3)
print(98 not in lst3)
#   列表元素的遍历for 迭代变量 in 列表名
for item in lst3:
    print(item)
# 3.列表的增删改
#    增加操作（最常用append）
print(lst3, id(lst3))
lst3.append(100)  # append()是向列表末尾添加一个元素
print(lst3, id(lst3))
lst3.extend(lst)  # extend()将lst中所有元素一个个添加到lst3末尾
print(lst3, id(lst3))
lst3.insert(1, 90)  # insert()在索引为1的位置上添加90
lst4 = [1, 2, 3, 6]                    # 切片是在任意位置上替换n多个元素
lst5 = [4, 5]
lst4[1:3] = lst5     # 将lst4切出来的片全部换成lst5的内容
print(lst4)
#    删除操作
lst4.remove(6)     # remove()是将列表中指定元素删除，如果删除的元素是重复元素，只会删除第一个
print(lst4)
lst4.pop(0)     # pop()是根据索引去删除指定元素，如果不写参数，默认将列表最后一个元素删除
print(lst4)
lst4[1:] = []     # 使用切片操作。将切片用空列表替代，从而实现将其删除
print(lst4)
lst4.clear()        # 清除列表中的所有元素
print(lst4)
del lst4         # 删除列表
#    修改操作（指定索引的元素赋予一个新值或者指定切片的元素赋予一个新值）
lst5[1] = 100  # 指定索引的元素赋予一个新值
print(lst5)
lst5[1:] = [50, 100, 200]
print(lst5)


# 4.列表的排序
lst4 = [50, 40, 60, 20, 30]
lst4.sort()   # 可以使用sort（）对列表对象排序，默认是升序，不会产生新的列表对象
print(lst4)
lst4.sort(reverse=True)   # 将关键字reverse置True，可以降序排序
print(lst4)
lst4 = [50, 40, 60, 20, 30]
new_list = sorted(lst4)  # 使用sorted（）对列表进行排序，产生新的列表对象，默认升序排序，同样可以将reverse置True改成降序
print(new_list)
new_list = sorted(lst4, reverse=True)
print(new_list)


# 5.列表生成式
"""列表生成式简称生成列表的公式
                     语法格式：【i*i for i in range(1, 10)】  
                    列表元素的表达式    自定义变量    可迭代对象
    注意事项：表示列表元素的表达式中通常包含自定义变量
    """
lst = [i for i in range(1, 10)]
print(lst)
lst = [i*i for i in range(1, 10)]
print(lst)
lst = [i*j for i in range(1, 10) for j in range(1, 10)]
#lst.sort()
print(lst)