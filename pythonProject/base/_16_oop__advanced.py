"""
Python oop 进阶
类属性的可见性和属性装饰器
__属性名称 表示一个私有的属性
_属性名称 表示一个受保护的属性
属性 表示公有属性
"""


class Student:
    """
    学生类
    """

    def __init__(self, name: str, age: int):
        """
        初始化方法
        :param name: 姓名
        :param age: 年龄
        """
        self.__name = name
        self.__age = age

    def study(self, course_name: str):
        """
        学习方法
        :param course_name: 课程名
        :return:
        """
        print(f"{self.__name}正在学习{course_name}")


student = Student("张三", 18)
student.study("Python")
# print(student.__name)  # AttributeError: 'Student' object has no attribute '__name'

"""
动态属性
Python 是动态语言， 在运行时可以改变其结构语言，
例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化
"""


class Programmer:
    """
    程序员类
    """

    def __init__(self, name: str, age: int):
        """
        初始化方法
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def work(self):
        """
        工作方法
        :return:
        """
        print(f"{self.name}正在工作")


programmer = Programmer("张三", 18)
programmer.work()
programmer.gender = "男"
print(programmer.gender)
print(f"姓名: {programmer.name}, 年龄: {programmer.age},性别:{programmer.gender}")

"""
禁止需要有动态属性
使用 __slots__=("name","age")
这样类的对象只能有name和age属性
"""


class Student1:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student1('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
# stu.sex = '男'

"""
静态方法和类方法
对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，
区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。
可以直接使用类名.方法名的方式来调用静态方法和类方法
"""


class Triangle:
    """
    三角形类
    """

    def __init__(self, a: float, b: float, c: float):
        """

        :param a:
        :param b:
        :param c:
        """
        self.a = a
        self.b = b
        self.c = c

    # 使用staticmethod  装饰器声明 is_valid 方法是一个静态防范
    @staticmethod
    def is_valid(a: float, b: float, c: float) -> bool:
        """
        判断三角形的边长是否合法 静态方法
        :param a:
        :param b:
        :param c:
        :return:
        """
        return a + b > c and a + c > b and b + c > a

    # @classmethod装饰器声明 is_valid 方法是一个类方法
    # @classmethod
    # def is_valid(a: float, b: float, c: float) -> bool:
    #     return a + b > c and a + c > b and b + c > a

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    # 使用 @property 装饰器将 perimeter 和 area 方法转换为属性
    @property
    def area(self):
        """计算面积"""
        # p = self.perimeter() / 2
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(3, 4, 5)
print(f"周长{t.perimeter}")
print(f"面积{t.area}")

"""
继承与多态
"""


class Person:
    """
    人类
    """

    def __init__(self, name: str, age: int):
        """
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃东西")

    def sleep(self):
        print(f"{self.name}正在睡觉")


class Student(Person):
    """
    学生类
    """

    def __init__(self, name: str, age: int, grade: str):
        """
        初始化方法
        :param name: 姓名
        :param age: 年龄
        :param grade: 年级
        """
        super().__init__(name, age)
        self.grade = grade

    def study(self, course_name: str):
        """
        学习方法
        :param course_name: 课程名
        :return:
        """
        print(f"{self.name}正在学习{course_name}")


class Programmer(Person):
    """
    程序员类
    """

    def __init__(self, name: str, age: int, language: str):
        """
        初始化方法
        :param name: 姓名
        :param age: 年龄
        :param language: 编程语言
        """
        super().__init__(name, age)
        self.language = language

    def job(self, address: str):
        """
        学习方法
        :param address: 课程名
        :return:
        """
        print(f"{self.name}正在{address}上班")


stu6: Student = Student("张三", 18,"大一")
stu1: Student = Student("李四", 20,"大三")
programmer: Programmer = Programmer("王五", 18, "Python")
programmer.job("北京")
stu6.eat()
stu1.sleep()
stu6.study("Python")
