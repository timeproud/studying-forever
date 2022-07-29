# 创建人：gw
# 开发时间：2022/7/24 14:34


# 目录操作
"""
os模块是python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关， 在不同的操作系统上运行，得到的结果可能不一样
os模块与os.path模块用于对目录或文件进行操作
"""

import os
# os.system('notepad.exe')  # 启动系统内软件
'''
OS模块操作目录相关函数
getcwd()                        返回当前的工作目录
listdir(path)                   返回指定目录下的文件和目录信息
mkdir(path[,mode])              创建目录
makedirs(path1/path2...[,mode]) 创建多级目录
rmdir(path)                     删除目录
removedirs(path1/path2...)      删除多级目录
chdir(path)                     将path设置为当前工作目录
'''


print(os.getcwd())
print(os.listdir('../chap15'))


'''
os.path                模块操作目录相关函数
abspath(path)          用于获取文件或目录的绝对路径
exists(path)           用于判断文件或目录是否存在，如果存在返回True，否则返回False
join(path,name)        将路径与目录或文件名拼接起来
splitext()             分离文件名和扩展名
basename(path)         从一个路径中提取文件名
dirname(path)          从一个路径中提取文件路径，不包括文件名
isdir(path)            用于判断是否为路径
'''


# 列出指定目录下的所有文件
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)





'''
os.walk() 方法:os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
              os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。在Unix，Windows中有效。
walk()方法语法格式如下：
             os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
参数
    top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
    onerror -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
    followlinks -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。
返回值:返回生成器。
'''


lst_files = os.walk(path)
print(lst_files)
for dirpath, dirname, filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    for dir in dirname:
        print(os.path.join(dirpath, dir))

    for file in filename:
        print(os.path.join(dirpath, file))
    print('----------------------------')