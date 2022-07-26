# 创建人：gw
# 开发时间：2022/7/24 12:16


"""
编码格式：
    常见字符的编码格式：python的解释器使用的是Unicode(外存).   .py文件在磁盘上使用UTF-8存储(外存)

文件读写原理：文件的读写俗称IO操作
           文件读写操作流程：python操作文件、打开或新建文件、读写文件、关闭资源
           操作原理
           内置函数open（）创建文件对象   通过IO流将磁盘中的内容与程序中的对象中的内容进行同步
"""
file = open('a.txt', 'r')
print(file.readline())
file.close()


"""
常用的文件打开模式：
r	以只读的模式打开文件，文件的指针会放在文件的开头
w	以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
a	以追加的模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾
b	以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb,或者 wb
+	以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+
————————————————
文件的类型：
        按文件的数据的组织形式，可以分为两大类：文本文件：储存的是普通“字符”文本，默认为unicode字符集，可以使用记事本程序打开
                                     二进制文件：把数据内容用字节进行存储，无法用记事本打开必须使用专用的软件打开
"""


file = open('b.txt', 'a')
file.write('helloworld')
file.close()


"""
read([size])	        从文件中读取size个字节或字符的内容放回。若省略[size]，则读取到文件的末尾，即一次读取文件所有内容
readline()	            从文本文件中读取一行内容
readlines()	            把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
write(str)	            将字符串str内容写入文件
writelines(s_list)	    将字符串列表s_list写入文本文件，不添加换行符
seek(offset[，whence])	把文件指针移动到新的位置，__offect__表示相对于whence的位置：offect：为正往结束方向移动，为负往开始方向移动 __whence__不同的值代表不同的含义： 0：从文件头开始计算(默认值) 1 ：从当前位置开始计算 2：从文件尾开始计算
tell()	                返回文件指针的当前位置
flush()	                把缓冲区的内容写入文件，但不关闭文件
close()	                把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关的资源
————————————————
"""



"""
with语句：with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确地关闭，以此来达到释放资源的目的。（即不用再写close）
"""

with open('a.txt', 'r') as file:   # 此处使用with语句，不用手动写close关闭资源
    print(file.read())