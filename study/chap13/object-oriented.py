# 创建人：gw
# 开发时间：2022/7/21 13:03


# 面向对象的三大特征：封装（提高程序的安全性）、继承（提高代码的复用性）、多态（提高代码的可拓展性和可维护性）
"""
封装：将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。
     在python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个”_“。
"""


class Car:
    def __init__(self, brand, jiage):
        self.brand = brand
        self.__jiage = jiage   # jiage不希望在类的外部被直接使用（但可以使用，见30行），所以在前面加__    但是可以在类的内部被使用，如方法show()


    def start(self):
        print('汽车已启动')


    def show(self):
        print(self.brand,self.__jiage)


car1 = Car('宝马X5', '50万')
car1.start()
print(car1.brand)
car1.show()
print(car1._Car__jiage)    # 对jiage的访问


"""
继承：  语法格式：calss 子类类名（父类1，父类2...）：pass
    如果一个类没有继承任何类，则默认继承object
    python支持多继承
    定义子类时，必须在其构造函数中调用父类的构造函数
"""

"""
方法重写：如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其进行重新编写，子类重写后的方法可以通过调用super().xxx()调用父类中被重写的方法
"""


class Person:    # 定义父类
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print('姓名：{0}, 年龄：{1}'.format(self.name, self.age))


class Student(Person):    # 定义子类
    def __init__(self, name, age, GPA):
        super().__init__(name, age)     # 定义子类时，在其构造函数中调用父类的构造函数
        self.GPA = GPA

    def info(self):    # 重写info()
        super().info()   # 调用父类中的info（），也可以不调用，直接重写
        print(self.GPA)    # 重写的部分

    def __str__(self):  # 重写了object内置方法__str__()
        return 'my name is {0}, I am {1} years old.'.format(self.name, self.age)


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary


class Woman(Person):
    def __init__(self, name, age, kids):
        super().__init__(name, age)
        self.kids = kids


# class Woman_tercher(Woman, Teacher):
#     pass
#     def __init__(self, name, age, kids, salary):
        # super().__init__(name, age, kids)
        # Teacher().__init__(self, name, age, salary)
        # Teacher.__init__(self, salary)
        # self.workingyears = workingyears



stu1 = Student('Jack', 20, 3.12)
stu1.info()   # 从父类继承的方法
tea1 = Teacher('Bob', 45, 8000)
tea1.info()
# sb1 = Woman_tercher('Jany', 35, 2, 4000)
# sb1.info()


"""
object类：object类默认时所有类的父类，因此所有类都有object类的属性和方法
         内置函数dir（）可以查看指定对象所有属性
         Object有一个__str__()方法，用于返回一个对于”对象的描述“，对应于内置函数str（）经常用于print方法，帮我们查看对象的信息，所以我们经常会对__str__()进行重写
"""

print(dir(stu1))
print(stu1.__str__())


"""
多态：多态就是”具有多种形态“，指的是即便不知道一个变量所引用的对象是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法。
静态语言和动态语言关于多态不同（Python是动态语言）
   静态语言实现多态的必要条件：继承、方法重写、父类引用指向子类对象
   动态语言只关行对象的行为
"""


class Animal(object):
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃屎')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃五谷杂粮')


# 定义一个函数


def fun(obj):
    obj.eat()


fun(Dog())
fun(Cat())
fun(Person())
fun(Animal())   # 尽管Person和Animal不是一种类，但是只要有eat（）方法，就可以调用







