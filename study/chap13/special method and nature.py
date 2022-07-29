# 创建人：gw
# 开发时间：2022/7/22 0:33


"""
特殊方法和特殊属性
特殊属性：  __dict__       获得类对象或者实例对象所绑定的所有属性和方法的字典
特殊方法：  __len__()      通过重写__len__()方法，让内置函数len（）的参数可以是自定义类型
          __add__()      通过重写__add__()方法，可使用自定义对象具有“+”功能
          __new__()      用于创建对象
          __init__()     对创建的对象初始化
"""


class A(object):
    pass


class B(object):
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建C类对象
x = C('lala', 20)
print(x.__dict__)
print(C.__bases__)  # 输出C类的父类类型的元素
print(C.__mro__)    # C的继承层次结构
print(A.__subclasses__())  # A的子类的元素列表


a = 20
b = 100
c = a + b  # 两个整数相加
d = a.__add__(b)   # 与上一行一个意思


print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name


    def __add__(self, other):    # 重写add（）方法
        return self.name + other.name


    def __len__(self):         # 重写len，从而在调用时获得name的长度
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')

# s = stu1+stu2   # 如果没有重写add（），程序报错
s = stu1 + stu2   # 重写了__add__()
print(s)


# len():计算列表长度
lst = [11, 22, 33]
print(len(lst))
print(lst.__len__())   # 与上一行一个意思


print(stu1.__len__())  # 重写了len后，调用输出name的长度


class Person(object):
    def __new__(cls, *args, **kwargs):
        print('new被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj


    def __init__(self, name, age):
        print('__init__()被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

# 创建Person的实例对象
p1 = Person('qiqi', 20)
print('p1这个实例对象的id为：{0}'.format(id(p1)))
p2 = Person('liqi', 21)
print('p2这个实例对象的id为：{0}'.format(id(p2)))


"""
object这个类对象的id为：140731266588160
Person这个类对象的id为：1495079089680
new被调用执行了，cls的id值为1495079089680
创建的对象的id为：1495080276176
__init__()被调用了，self的id值为：1495080276176
p1这个实例对象的id为：1495080276176
new被调用执行了，cls的id值为1495079089680
创建的对象的id为：1495080276080
__init__()被调用了，self的id值为：1495080276080
p2这个实例对象的id为：1495080276080
"""


# 类的浅拷贝与深拷贝
"""
变量的赋值操作：只是形成两个变量，实际上还是指向同一个对象
浅拷贝：python拷贝一般是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，由此，源对象与拷贝对象会引用同一个子对象
深拷贝：使用copy的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也要重新拷贝
"""


class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# （1）变量的赋值操作
cpu1 = Cpu()    # Cpu类的一个实例对象
cpu2 = cpu1     # 类对象的赋值操作
print(cpu1)
print(cpu2)    # cpu1和cpu2的地址一样

# （2）类的浅拷贝
disk = Disk()   # 创建一个Disk类的对象
computer = Computer(cpu1, disk)    # 创建一个Computer类的对象
# 浅拷贝
import copy
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)
"""
<__main__.Computer object at 0x000001E61D4EA880> <__main__.Cpu object at 0x000001E61D4EA8E0> <__main__.Disk object at 0x000001E61D4EA8B0>
                                不同，进行了拷贝                             相同，没有拷贝                                 相同，没有拷贝
<__main__.Computer object at 0x000001E61D4E95B0> <__main__.Cpu object at 0x000001E61D4EA8E0> <__main__.Disk object at 0x000001E61D4EA8B0>
由于执行的是浅拷贝，computer2拷贝了一份computer，并且存到新地址，但是不拷贝对应的cpu1和disk，所以computer2.cpu和computer2.disk仍然指向cpu1和disk
"""

# （3）类的深拷贝
computer3 = copy.deepcopy(computer)   # 深拷贝操作
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
"""
<__main__.Computer object at 0x00000126812B9880> <__main__.Cpu object at 0x00000126812B98E0> <__main__.Disk object at 0x00000126812B98B0>
                                不同，进行了拷贝                             不同，进行了拷贝                                  不同，进行了拷贝 
<__main__.Computer object at 0x00000126812B8460> <__main__.Cpu object at 0x00000126812B8070> <__main__.Disk object at 0x00000126812B3760>
"""

