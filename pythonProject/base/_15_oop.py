"""
Python 中的oop 编程
面向对象编程：把一组数据和处理数据的方法组成对象，把行为相同的对象归纳为类，
通过封装隐藏对象的内部细节，通过继承实现类的特化和泛化，通过多态实现基于对象类型的动态分派。
"""


# 定义类
class Person:

    def study(self, course: str):
        print(f"这个人正在学习{course}")

    def play(self):
        print("玩耍")


person1 = Person()

person2 = Person()

print(person1)

print(person2)

# 对象方法调用
# 方式1
Person.study(person1, "java开发")
# 方式2
person1.study("做饭")

person2.play()


#类的初始发方法

class Student:
    def __init__(self, name: str, age: int):
        """
        初始化方法
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def study(self, course_name: str):
        print(f"{self.name}正在学习{course_name}")

    def play(self):
        print(f"{self.name}正在玩耍")


stu1 = Student("张三", 18)
stu1.study("java 开发课程")
stu1.play()

"""
面向对象的三大特点
封装，继承，多态
"""

"""
定义一个描述数字时钟，提供走秒和显示时间的功能
"""
import time


class Clock:
    """
    数字时钟
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        """
        构造方法
        :param hour: 小时
        :param minute: 分钟
        :param second: 秒
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        """
        走秒
        :return:
        """
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """
        显示时间
        :return:
        """
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


# 创建时间对象
clock = Clock(23, 59, 59)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()

"""

定义一个类用来体现平面上的点，提供计算到另外一个点的距离
"""


class Point:
    """平面上的点"""

    def __init__(self, x: float = 0, y: float = 0):
        """
        构造方法
        :param x:
        :param y:
        :return:
        """
        self.x, self.y = x, y

    def distance_to(self, other: 'Point'):
        """
        计算到另一个点的距离
        :param other:
        :return:
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        """
        返回对象的字符串表示
        :return:
        """
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
print(p1)
p2 = Point(4, 6)
print(p2)
print(p1.distance_to(p2))
