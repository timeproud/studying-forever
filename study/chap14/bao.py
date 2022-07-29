# 创建人：gw
# 开发时间：2022/7/24 10:10


"""
包：：包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
     作用：代码规范、避免模块名称冲突
包和目录的区别：包含__init__.py文件的目录称为包
             目录里通常不包含__init__.py文件
包的导入：import   包名、模块名
"""


# 导入moduleA模块（package在同一目录下）
import package1.moduleA
print(package1.moduleA.a)


"""
导入带有包的模块时的注意事项：
  使用import导入时，只能跟包名或者模块名，不能跟函数、变量
  使用from...import...可以导入包、模块、函数、变量如：from package.moduleA import a
"""


"""
python中常用的内置模块：
            sys：与python解释器及其环境操作相关的标准库
            time: 时间模块
            datetime模块: datetime模块是对time模块的一个高级封装(time包基于C语言的库函数)
            random模块: Python中的random模块用于生成随机数
            re: 正则模块
            sys模块: sys模块提供了一系列有关Python运行环境的变量和函数
            os模块: os模块包含普遍的操作系统功能，如文件操作、目录等，与具体的平台无关，提供了访问操作系统服务功能的标准库
            calender:提供与日期相关的各种函数的标准库
            urllib：用于读取来自网上（服务器）的数据标准库
            subprocess: 子进程管理模块，常用call()、run()、Popen()等方法。官方文档
            shutil: 对文件(夹)、压缩包进行处理的模块（移动/复制/打包/解压/修改权限）。
            hashlib/hmac/uuid: 消息摘要/加密/全局唯一标识符
            pickle: 序列化处理模块，常用dump()、load()方法。
            configparser: ini配置文件解析模块。
            itertools: 一个创建快速、高效迭代器的模块。官方文档
            logging: 内置模块，日志相关。
            optparse: 命令行解析模块。
            docopt: 命令行解析模块。
            json: json文件处理模块。
            csv: CSV文件处理模块。
            xml.etree.ElementTree: 内置模块，解析xml等文件。
            tempfile: 内置模块，临时文件操作
            timeit: 测量小代码片段的执行时间。 
"""


import sys
print(sys.getsizeof(24))   # 获取对象的内存大小
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.time())
print(time.localtime(time.time()))


"""
第三方模块的安装与使用
   安装：pip install 模块名
   使用：import 模块名
"""


import schedule


def job():
    print("hhh")


schedule.every(3).seconds.do(job)    # 每隔3s执行一次
while True:
    schedule.run_pending()   # 启动
    time.sleep(3)
