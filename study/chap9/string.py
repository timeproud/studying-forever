# 创建人：gw
# 开发时间：2022/7/18 10:28


# 字符串：在python中字符串是基本数据类型，是一个不可变的字符序列


# 1.字符串的驻留机制：字符串驻留是一种在内存中仅保存一份相同且不可变字符串的方法。 Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量。
"""
驻留机制的几种情况（交互模式）：字符串的长度为0或者1时
                          符合标识符的字符串
                          字符串只在编译时进行驻留，而非运行时
                          [-5,256]之间的整数数字
sys中的intern方法强制2个字符串指向同一个对象
pycharm对字符串进行了优化处理
字符串驻留机制的优缺点：当需要值相同的字符串时，可以直接从字符串池中拿来使用，避免频繁的创建和销毁，提升效率和节约内存，因此拼接字符串和修改字符串是比较影响性能的。
                   所以，在需要进行字符串的拼接操作时，建议使用str类型的join方法，而非+，因为join（）是计算出所有字符的长度，然后再拷贝，只new一个对象，效率比+要高
"""


# 2.字符串的常用操作
# 查询操作：index(), rindex(), find(), rfind()
s = 'hello,hello'
print(s.index('lo'))    # 查找字串第一次出现的位置，如果字串不存在，则报error
print(s.rindex('lo'))    # 查找字串最后一次出现的位置，如果字串不存在，则报error
print(s.find('lo'))      # 查找字串第一次出现的位置，如果字串不存在，则返回-1
print(s.rfind('lo'))     # 查找字串最后一次出现的位置，如果字串不存在，则返回-1
# 大小写转换操作：upper(), lower(), swapcase(), capitalize(), title()
print(s.upper())                                   # upper()把所有字符转换为大写,产生新的字符串对象
print(s.lower())                                   # lower()把所有字符转换为小写,产生新的字符串对象
print(s.swapcase())                                # swapcase()把所有大写变小写，小写变大写
print(s.capitalize())                              # capitalize()把首字母变大写，其余变小写
print(s.title())                                   # title()把每个单词的首字母变大写，其余变小写
# 字符串内容对齐操作：center（），ljust（），rjust（），zfill（）
print(s.center(20, '$'))  # center（）是居中对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认空格），如果设置宽带小于实际宽度则返回原字符串
print(s.ljust(20, '$'))  # ljust（）是左对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认空格），如果设置宽带小于实际宽度则返回原字符串
print(s.rjust(20, '$'))  # rjust（）是右对齐，第一个参数指定宽度，第二个参数指定填充符（可选，默认空格），如果设置宽带小于实际宽度则返回原字符串
print(s.zfill(20))  # zfill（）是右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度。如果指定的宽度小于等于字符串的长度，则返回字符串本身
# 字符串劈分操作：split(),rsplit()
s1 = 'hello world python'
s2 = 'hello,world,python'
lst1 = s1.split()     # split()从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回值都是一个列表
print(lst1)
lst2 = s2.split(sep=',', maxsplit=1)  # 可以通过参数sep指定劈分字符串的劈分符。通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分次数的劈分后，剩余的子串会单独作为一部分。
print(lst2)
lst3 = s1.rsplit()   # rsplit()从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回值都是一个列表
print(lst3)
lst4 = s2.rsplit(sep=',', maxsplit=1)  # 可以通过参数sep指定劈分字符串的劈分符。通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分次数的劈分后，剩余的子串会单独作为一部分。
print(lst4)
# 判断字符串的操作：isidentifier（）,isspace(),isalpha(),isdecimal(),isnumeric(),isalnum()
print('pyhton'.isidentifier())   # isidentifier（）判断指定的字符串是不是合法的标识符
print('     \n'.isspace())  # isspace()判断指定的字符串是不是全部由空白字符组成，回车，换行，空格，水平制表符等
print('中国a'.isalpha())    # isalpha()判断指定的字符串是不是全部由字母（包括汉字）组成
print('12581'.isdecimal())    # isdecimal()判断指定的字符串是不是全部由十进制的数字组成（不包括汉字、罗马数字）
print('1223四五0'.isnumeric())    # isnumeric()判断指定的字符串是不是全部由数字组成（包括汉字、罗马数字）
print('zdan真的爱你521'.isalnum())    # isalnum()判断指定的字符串是不是全部由字母和数字组成
# 字符串的替换操作：replace（）
print(s.replace('hello', 'love'))   # 第一个参数指定被替换的子串，第二个参数指定替换字串的字符串，返回替换后得到的字符串，替换前的字符串不发生变化。
print(s.replace('hello', 'love', 1))    # 可以通过第三个参数指定替换的最大次数
# 字符串的合并操作：join（）    一般是列表或者元组
lst5 = ['hello', 'c++', 'python']   # 将列表中的元素连接成字符串
print(' '.join(lst5))
t = ('hello', 'c++', 'python')
print(' '.join(t))
print('*'.join('python'))
# 字符串的比较操作： 运算符：>,>=,<,<=,==,!=
"""字符串的比较规则：首先比较两个字符串中第一个字符，如果相等则继续比较下一个字符，依次比较下去，知道两个字符串中的字符不相等是，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
          比较原理：两字符进行比较时，比较的是其ordinal value（原始值），调用内置函数ord可以得到指定字符的ordinal value。与内置函数ord对应的是内置函数chr，调用chr时指定ordinal可以得到其对应的字符。
   == 与 is 的区别：==比较的是value是否相同，is 比较的是id是否相同
"""
print('apple' > 'app')
print(ord('a'), ord('b'))
print('a' < 'b')
print(chr(99))
# 字符串的切片操作：s[start:end:step]
"""字符串是不可变类型，不具备增删改等操作，切片操作将产生新的对象"""
s3 = s.replace('hello', 'python').replace('python', 'hello', 1)
print(s3)
s4 = s3[:5]    # 由于没有指定起始位置，所以从0开始
s5 = s3[6:]    # 由于没有指定结束位置，所以会切到字符串的最后
newstr = s4 + '!' + s5
print(newstr)
print(id(s3))
print(id(s4))
print(id(s5))
print(id(newstr))
print(s3[::2])   # 从开始裁到结束，步长为2
print(s3[::-1])  # 当步长为负数，倒序切片
# 格式化字符串操作：%作为占位符、{}作为占位符、f-string方法
name = 'somebody'
age = 20
print('my name is %s, I am %d years old.' % (name, age))   # %作为占位符
print('my name is {0}, I am {1} years old.'.format(name, age))   # {}作为占位符
print(f'my name is {name}, I am {age} years old.')   # f-string方法
print('%10d' % 99)   # 10表示的是宽度
print('%.3f' % 3.1415926)  # .3表示小数点后面的位数
print('%10.3f' % 3.1415926)  # 表示总宽度为10， 小数点后3位
print('{0: .3}'.format(3.1415926))   # .3表示一共3位数
print('{0: .3f}'.format(3.1415926))   # .3f表示3位小数
print('{0: 10.3f}'.format(3.1415926))   # 10.3f表示3位小数，宽度为10


# 3.字符串的编码转换         编码：将字符串转换为二进制数据（bytes）    解码：将bytes类型的数据转换为字符串类型
st = '中国人不骗中国人'
# 编码操作
print(st.encode(encoding='GBK'))     # 在GBK中，一个中文占两个字节
print(st.encode(encoding='UTF-8'))   # 在UTF-8中。一个中文占三个字节
# 解码操作
byte = st.encode(encoding='GBK')
print(byte.decode(encoding='gbk'))
