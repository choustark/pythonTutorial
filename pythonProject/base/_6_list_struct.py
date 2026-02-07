'''
基础数据结构列表
列表是由一系元素按特定顺序构成的数据序列，可以用它来保存多个数据,不同的数据类型
'''
from typing import List
from typing import Dict
from typing import Tuple

item1: List[str] = [1, 2, 3, 4, 5, 6, 7]
print(item1)
item2 = ['java', 'python', 'c++', 'c', 'rust', 'go', 'javaScript']
print(item2)
item3 = [1, 'java', True, False, 1.0, 1.1, 1.2]
print(type(item3))

'''
list() 函数 创建列表对象构造器
'''

item4: List[int] = list(range(1, 10))
print(item4)
item5: List[int] = list('hello world')
print(item5)

'''
列表的运算
'''
item6: List[int] = [1, 2, 3, 4, 5, 6, 7]
item7: List[int] = [8, 9, 10, 11, 12, 13, 14]
print(item6 + item7)
print(item6 * 3)

print(1 in item6)
print(15 in item7)
print(15 not in item7)
print('java' in item2)

'''
索引
'''
items8: List[str] = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])
print(items8[1])
print(items8[-1])
items8[1] = 'durian'
print(items8)
items8[-4] = 'strawberry'
print(items8)

'''
切片运算
切片运算是形如[start:end:stride]的运算符
start:代表访问列表元素的起始位置
end:代表访问列表元素的终止位置（终止位置的元素无法访问）
stride:则代表了跨度，简单的说就是位置的增量
'''
print(items8[0:5:2])
print(items8[-4:-2:1])

# 切片操作修改列表中的元素
items8[1:3] = ['x', 'o']

'''
遍历列表
'''
for i in items8:
    print(i)

print('-' * 230)

'''
索引遍历
'''
for index in range(len(items8)):
    print(items8[index])

import random

counters: List[int] = [0] * 6
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')

print('-' * 230)

'''
列表的增删改查
'''
languages: List[str] = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)
languages.insert(1, 'Rust')
print(languages)
if 'go' in languages:
    languages.remove('go')
    print(languages)
if 'C++' in languages:
    languages.remove('C++')
    print(languages)

# 移除列头的元素（从左到右）
languages.pop(0)
print(languages)

# 删除列表中指定位置的元素
del languages[0]
print(languages)

languages.clear()
print(languages)

'''
列表元素的位置和元素的频次
'''
print('-' * 80 + '列表元素位置和频次' + '-' * 80)

items9: List[str] = ['Java', 'Python', 'C++', 'C', 'Rust', 'Go', 'Go', 'JavaScript']
print(items9)

print(items9.index('Java'))  # 从索引的0开始查找Java
# print(items9.index('Java',1))           # 从索引的1开始查找Java ValueError: 'Java' is not in list
print(items9.index('C', 1))

print(items9.count('Go'))

print('-' * 80 + '元素的排序和反转' + '-' * 80)
items10: List[str] = ['Java', 'Python', 'C++', 'C', 'Rust', 'Go', 'Go', 'JavaScript']
print(items10)
items10.sort()
print(items10)
items10.reverse()
print(items10)

print('-' * 80 + '列表的  生成式  ' + '-' * 80)
list1: List[int] = [];
for i in range(1, 200):
    if i % 3 == 0 or i % 5 == 0:
        list1.append(i)
print(list1)
print(f'个数{len(list1) = }')

# 简写方式
list2: List[int] = [i for i in range(1, 200) if i % 3 == 0 or i % 5 == 0]

print(list2)
print(f'个数{len(list2) = }')

print('-' * 80 + '有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方' + '-' * 80)
nums1: List[int] = [10, 20, 15, 25]
nums2: List[int] = []
for i in nums1:
    nums2.append(i ** 2)
print(nums2)

nums3 = [i ** 2 for i in nums1]
print(nums3)

print('-' * 80 + '嵌套列表' + '-' * 80)
items11: List[List[int]] = [[90, 85, 70], [99, 80, 81], [80, 86, 89]]
print(items11[0])
print(items11[0][1])

items12: List[List[int]] = []
for _ in range(5):
    temp: List[int] = []
    for _ in range(1):
        score = int(input("请输入分数："))
        temp.append(score)
    items12.append(temp)
print(items12)

print('-' * 80 + '列表的应用: 生成一组随机双色球号' + '-' * 80)

import random
from rich.console import Console
from rich.table import Table
import os

red_balls_container: List[int] = list(range(1, 34))
blue_balls_container: int = random.randrange(1, 17)
# 红球个数为6个
selected_red_balls: List[int] = []
for _ in range(6):
    index = random.randrange(len(red_balls_container))
    selected_red_balls.append(red_balls_container.pop(index))
# 红色球排血
selected_red_balls.sort()
# 输出红色球
for ball in selected_red_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 绿色球
print(f'\033[032m{blue_balls_container:0>2d}\033[0m')

print('-' * 80 + '列表的应用: 生成一组随机双色球号 优化版本' + '-' * 80)

# 随机生成红色球 34个
red_balls_container: List[int] = [i for i in range(1, 34)]
# 随机生成蓝色球 17个
blue_balls_container: List[int] = [i for i in range(1, 17)]
# 从红色球中随机抽取6个（没有返回抽样）
selected_red_balls: List[int] = random.sample(red_balls_container, 6)
# 排序
selected_red_balls.sort()
for ball in selected_red_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
random.choice(blue_balls_container)
print(f'\033[032m{random.choice(blue_balls_container):0>2d}\033[0m')

print('-' * 80 + '列表的应用: 生成n组随机双色球号' + '-' * 80)
num: int = int(input('请输入组数：'))
for _ in range(num):
    # 随机生成红色球 34个
    red_balls_container: List[int] = [i for i in range(1, 34)]
    # 随机生成蓝色球 17个
    blue_balls_container: List[int] = [i for i in range(1, 17)]
    # 从红色球中随机抽取6个（没有返回抽样）
    selected_red_balls: List[int] = random.sample(red_balls_container, 6)
    # 排序
    selected_red_balls.sort()
    for ball in selected_red_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    random.choice(blue_balls_container)
    print(f'\033[032m{random.choice(blue_balls_container):0>2d}\033[0m')

print('-' * 80 + '列表的应用: 生成n组随机双色球号 打印优化版本' + '-' * 80)
console: Console = Console()
num: int = int(input('请输入组数：'))
# 随机生成红色球 34个
red_balls_container: List[int] = [i for i in range(1, 34)]
# 随机生成蓝色球 17个
blue_balls_container: List[int] = [i for i in range(1, 17)]
# 生成表头
table: Table = Table(title='双色球', show_lines=True, show_header=True)
table.add_column('序号', justify='right', no_wrap=True)
table.add_column('红球组', style='red')
table.add_column('篮球组', justify='right', style='green')
for i in range(num):
    # 从红色球中随机抽取6个（没有返回抽样）
    selected_red_balls: List[int] = random.sample(red_balls_container, 6)
    # 排序
    selected_red_balls.sort()
    blue_ball: int = random.choice(blue_balls_container)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(str(i + 1),
                  f'{" ".join([f"{ball:0>2d}" for ball in selected_red_balls])}',
                  f'{blue_ball:0>2d}')
# 输出
console.print(table)

print('-' * 150)
from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)
