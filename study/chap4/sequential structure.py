# 创建人：gw
# 开发时间：2022/6/26 20:49



# 任何简单或复杂的算法都可以由顺序结构、选择结构和循环结构这三种基本结构组合而成。

# 顺序结构：程序从上到下顺序地执行代码，中间没有任何的判断和跳转，直到程序结束。
print('程序开始')
print('1.把冰箱门打开')
print('2.把大象放冰箱里')
print('3.把冰箱门关上')
print('程序结束')
"""
debug方式：在需要debug的程序段的开始以及结束处打断点（左键行数），然后在run的下拉菜单中点击debug
"""

"""
对象的布尔值：python的一切皆对象，所有对象都有一个布尔值，要获取对象的布尔值，使用内置函数bool（）。
  以下对象的布尔值为False：False,数值0,None,空字符串,空列表,空元组,空字典,空集合
  其他对象的布尔值为True
"""
print(bool(False))
print(bool(''))
print(bool(None))
print(bool(tuple()))  # 空元组
print(bool(list()))   # 空列表
print(bool(dict()))   # 空字典
print(bool(set()))    # 空集合

