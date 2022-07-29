# 创建人：gw
# 开发时间：2022/7/22 14:53


"""
模块：
    在python中一个拓展名为.py的文件就是一个模块
    一个模块可以包含多个函数和类
    使用模块的好处：
                 方便其他程序和脚本的导入并使用
                 避免函数名和变量名冲突
                 提高代码的可维护性
                 提高代码的可重用性
"""


# 导入模块        语法：import 模块名称 [as 别名]    或者   from 模块名称 import 函数、变量、类
# import math  # 关于数学计算的模块
# print(id(math))
# print(type(math))
# print(math)
# print(math.pi)
# print(dir(math))
# print(math.pow(2, 3))  # 计算2的3次方
# print(math.ceil(9.001))  # 向上取整
# print(math.floor(9.999))  # 向下取整


from math import pi # 从math中导入pi
print(pi)
print(pow(2, 3))   # 这个pow不是math中的pow


# 导入自定义模块   在同一目录下，最好将该目录设置为Sources Root，如果不在同一目录下，一定要将欲导入模块的目录设置为Sources Root
import demo   # 导入同一目录之下的模块
demo.test()
# 导入不同目录之下的模块，需要设置Sources Root
#  from function import calc
#  print('\n')
#  print(calc(1, 9))


# 以主程序方式运行
"""
在每个模块的定义中都包括一个记录模块名称的变量__name__，程序可以检查到该变量，以确定他们在哪个模块中被执行。如果一个模块不是被导入到其他程序中执行，顶级模块的__name__变量的值为__main__
语法：if __name__ == 'main':
          pass
"""


import demo2
print(demo2.calc(10, 20))
"""
该段输出结果：
           3
           30
将引用模块输出的内容也输出了（只希望输出30，不希望输出3），则需要在引用的模块中，在不希望这边1输出前加入if __name__ == '__main__':   （见demo2中程序）
"""
