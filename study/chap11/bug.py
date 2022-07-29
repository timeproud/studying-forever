# 创建人：gw
# 开发时间：2022/7/20 10:29


# bug常见类型
"""
粗心导致的语法错误：SyntaxError
知识点不熟练导致的错误
思路不清导致的错误
"""
# python的异常处理机制： python提供了异常处理机制，可以在异常出现的时候进行即时捕获，然后“内部消化”，让程序继续运行。
# try...except...  结构
'''
try:
    n1 = int(input('input a number:'))
    n2 = int(input('input another number:'))
    result = n1 / n2
    print(''+str(n1)+'除以'+str(n2)+'等于：'+str(result)+'')
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('only number allowed')
except BaseException as e:
    print(e)  
    '''
# try...except...else...  结构:如果try中没有异常，则执行else，否则，执行except
'''
try:
    n1 = int(input('input a number:'))
    n2 = int(input('input another number:'))
    result = n1 / n2
except BaseException as e:
    print(e)
else:
    print(''+str(n1)+'除以'+str(n2)+'等于：'+str(result)+'')
'''
# try...except...else...finally...  结构：无论try中是否有异常，finally都会被执行,常用于释放try块中被申请的资源
'''try:
    n1 = int(input('input a number:'))
    n2 = int(input('input another number:'))
    result = n1 / n2
except BaseException as e:
    print(e)
else:
    print(result)
finally:
    print('无论是否产生异常都会被执行的代码')
print('over')'''
# traceback模块
'''
import traceback
try:
    print('...')
    num = 10/0
    # print('1')
except:
    traceback.print_exc()
print(111)
'''
# python中常见的异常类型
'''
ZeroDivisionError:除或取模0
IndexError:数据中没有此索引
KeyError:映射中没有这个键
NameError:未声明、初始化对象
SyntaxError:语法错误
ValueError:传入无效的参数
'''
