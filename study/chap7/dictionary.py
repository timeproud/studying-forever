# 创建人：gw
# 开发时间：2022/7/16 15:37


"""
字典：
    什么是字典：python内置的数据结构之一，与列表一样是一个可变序列，以键值对的方式存储数据，字典是一个无序的序列
    scores = { ‘张三’ ： 100， ‘李四’ ： 200 }
    字典名  （key）键  冒号  值
"""
# 1.字典的创建：使用花括号直接创建或者使用内置函数dict（）
scores = {'张三': 100, '李四': 200}  # 使用{}创建字典（最常用）
print(scores)
print(type(scores))


student = dict(name='jack', age=20)  # 使用内置函数创建字典
print(student)


d = {}   # 空字典的创建
print(d)


# 2.字典中元素的获取：使用【】或者get（）    两者区别：如果字典中不存在指定的key，使用【】会得到 keyerror ，而使用get（）则会得到None，可以通过设置参数指定key不存在时的返回值
print(scores['张三'])  # 使用【】获取元素
print(scores.get('张三'))   # 使用get（）获取元素
print(scores.get('麻瓜', 93))   # 如果元素不存在，可以指定返回值


# 3.字典的常用操作：key的判断（in 与 not in）、字典元素的删除（del操作,clear操作）、字典元素的新增与修改（直接【】）
print('张三' in scores)
print('张三' not in scores)   # key的判断
del scores['张三']   # 字典的删除，删除指定的键值对
print(scores)
scores.clear()    # 字典元素的清空操作
scores['王五'] = 500   # 字典元素的增加操作
print(scores)
scores['王五'] = 100   # 字典元素的修改操作
print(scores)
scores['张三'] = 200
scores['李四'] = 400


# 4.获取字典视图的三个方法：key（）是获取字典中所有key、values（）是获取字典中所有value、items（）是获取字典中所有key、value对
# 获取所有key
keys = scores.keys()   # 将字典中所有key存为一个变量keys
print(keys)
print(type(keys))
lst = list(keys)   # 将所有key组成的视图转成列表
print(lst)
# 获取所有value
values = scores.values()  # 将字典中所有value存为一个变量values
print(values)
print(type(values))
lst2 = list(values)    # 将所有value组成的视图转成列表
print(lst2)
# 获取所有键值对
items = scores.items()  # 将字典中所有键值对存为一个变量items
print(items)
print(type(items))
lst3 = list(items)    # 该列表中的元素由（）元组组成
print(lst3)


# 5.字典元素的遍历(得到键，如果要输出值要另外用其他方法)   语法：for items in scores: print(items)
for item in scores:
    print(item)
    print(item, scores[item], scores.get(item))    # scores[item], scores.get(item)两种方式都可以完成遍历时输出value


# 6.字典的特点
"""
  字典中所有元素都是一个键值对，key不允许重复，value可以重复
  字典中的元素是无序的
  字典中的key必须是不可变对象
  字典也可以根据需要动态伸缩
  字典会浪费较大的内存，是一种使用空间换时间的数据结构
  """


# 7.字典生成式 ：使用内置函数zip（），用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
items1 = ['xiaomi', 'huawei', 'ipad']
prices1 = [3500, 5000, 8000]

d = {item: price for item, price in zip(items1, prices1)}  # 通过两个列表生成一个字典
print(d)
d1 = {item.upper(): price for item, price in zip(items1, prices1)}  # 通过upper()将item大写
print(d1)
