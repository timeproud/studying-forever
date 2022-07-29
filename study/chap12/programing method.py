# 创建人：gw
# 开发时间：2022/7/21 9:58


"""
编程思想：                  面向过程                                       面向对象
               事物比较简单，可以用线性的思维去解决                事物比较复杂，使用简单的线性思维无法解决
        共同点：                      两者都是解决实际问题的一种思维方式
        两者相辅相成，并不是对立的。解决复杂问题，通过面向对象的方式方便我们从宏观上把握事物之间复杂的关系，方便我们分析整个系统；具体到微观操作，仍然使用面向过程来处理
"""


"""
类与对象
    类：多个类似事物组成的群体的统称，能够帮助我们快速理解和判断事物的性质。
    数据类型：不同的数据属于不同的类，可以使用内置函数type查看数据类型
    对象：100、99、520都是int类下包含的相似的个例，这个个例专业术语就叫实例或者对象
    python当中一切皆对象
"""


# 类的创建      语法：class sth:  类的内容                类的组成：类属性、实例方法、静态方法、类方法
'''class Student:    # Student 为类名，由应该或者多个单词组成，每个单词首字母大写其余小写
    pass


print(id(Student))
print(type(Student))
print(Student)'''
class Student:
    native_place = 'jiangxi'   # 在类当中，方法外的变量，称为类属性，被该类的所有对象所共享


    def  __init__(self, name, age):       # 初始化方法
        self.name = name   # slef.name称为实体属性，进行了赋值操作，将局部变量name的值赋给实体属性
        self.age = age


    def eat(self):   # 实例方法            在类之外定义的叫函数，在类之内定义的叫方法
        print(self.name + 'is eating.')


    @staticmethod
    def method():     # 静态方法中，不写self，使用类名直接访问的方法
        print('我使用了staticmethod进行修饰，所以我是静态方法')


    @classmethod
    def cmd(cls):    # 类方法，使用类名直接访问的方法
        print('因为我使用了classmethod进行修饰，所以我是类方法')


# 对象的创建：又叫类的实例化   语法：实例名 = 类名（）    意义：有了实例，就可以调用类的内容


# 创建Student类的对象
stu1 = Student('zhangsan', 20)
print(type(stu1))
print(stu1)  # 输出了16进制的内存

stu1.eat()   # 等价于Student.eat(stu1)
print(stu1.name)


# 类属性的使用方式
print(Student.native_place)
Student.native_place = '抚州'
stu2 = Student('lisi', 21)
print(stu1.native_place)
print(stu2.native_place)


# 类方法的使用方式
Student.cmd()  # 使用类名直接访问


# 静态方法的使用方式
Student.method()  # 使用类名直接访问


# 动态绑定属性和方法：python是动态语言，在创建对象后可以动态地绑定属性和方法
stu1.gender = '女'   # 单独为stu1动态绑定一个属性


def show():  # 定义在类之外，叫函数
    print('动态绑定方法')


stu1.show = show  # 将函数show，绑定为stu1的方法
stu1.show()    # 绑定后可以直接动态调用


