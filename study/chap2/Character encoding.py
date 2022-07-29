# coding:gbk
# 上面那行叫中文编码声明注释
# 创建人：gw
# 开发时间：2022/6/24 21:35


print(chr(0b100111001011000))  # 0b代表是二进制
print(chr(20056))  # 没有0b默认十进制
print(ord('乘'))  # 乘在UTF-8中的编码是20056


"""
标识符与保留字

保留字：有一些单词被赋予了特定的意义，在给任何对象起名字时都不能使用。
怎么看有哪些保留字：
import keyword
print(keyword.kwlist)

标识符：变量、函数、类、模块、其他对象取的名字
     规则：1.可以使用字母数字下划线
          2.不能以数字开头
          3.不能是保留字
          4.严格区分大小写
 """



"""
变量的三部分：
          1.标识：表示对象所存储的内存地址，可以用内置函数id（obj）获取
          2.类型：表示对象的数据类型，可以使用type(obj)获取
          3.值：表示对象所存储的具体数据，使用print(obj)可以将值打印输出
"""
name = 'gw'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)


"""
python中常用的数据类型：
                    1.整数类型int:十进制（默认）、二进制（0b）、八进制（0o）、十六进制（0x）、将整数转换为二进制，使用bin（）函数、将整数转换为八进制，使用oct（）函数、将整数转换为十六进制，使用hex（）函数
                    2.浮点数类型float:可能会出现小数位数不确定的情况，解决方案，导入模块decimal：form decimal import Decimal
                    3.布尔类型bool:可以转成整数计算
                    4.字符串类型str：可以使用单引号、双引号、三引号来定义，单引号和双引号定义的字符串必须在同一行，而三引号定义的字符串可以发布在连续的多行

"""
#int部分示例
print('十进制', 118)
print('二进制', 0b1011110)
print('八进制', 0o77)
print('十六进制', 0x2EA)

#float部分示例
# from decimal import Decimal
# print(Decimal('1.1')+Decimal('2.2'))

# bool部分示例
f1 = True    # True表示数字1
f2 = False   # False表示数字0
print(f1, type(f1))
print(f2, type(f2))
print(f1+1)
print(f2+1)

# str部分示例
str1 = 'world is word'
str2 = "need has word"
str3 = """world is word
need has word
"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))


"""数据类型转换的意义：将不同类型的数据拼接在一起"""
name = 'gw'
age = 21
print('my name is '+name+',now I am '+str(age)+' years old. ')  # +号是连接符，将字符串和变量进行连接。str（）是将其他类型的数据转换成字符串类型
