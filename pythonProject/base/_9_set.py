'''
集合的基本语法
'''
from typing import Set

a: Set[int] = {1, 2, 3}
b: Set[str] = {"张三","李四","王五"}
print(a)
print(b)

# 元素的遍历
for i in a:
    print(i)

# 成员运算
nums: Set[int] = {11,12,13,14,15,16}
for i in nums:
    print(i)
print(15 in nums)
print(17 not in nums)

# 二元运算
set1: Set[int] = {1,2,3,4,5}
set2: Set[int] = {1,2,4,5,6,7,8}

# 并集
print(set1 | set2)
print(set1.union(set2))
# 交集
print(set1 & set2)
print(set1.intersection(set2))
# 差集
print(set1 - set2)
print(set1.difference(set2))
# 对称差集
print(set1 ^ set2)
print(set1.symmetric_difference(set2))


# 二元运算
set3: Set[int] = {1, 3, 5, 7}
set4: Set[int] = {2, 4, 6}
# set1.update(set2)
set3 |= set4
print(set3)

set5: Set[int] = {3,6,9}
# set1.intersection_update(set3)
set3 &= set5
print(set3)

# set2.difference_update(set1)
set4 -=set3
print(set4)


#比较运算
num1: Set[int] = {1, 3, 5}
num2: Set[int] = {1, 2, 3, 4, 5}
num3: Set[int] = {5, 4, 3, 2, 1}
print(num1 < num2)
print(num1 <= num2)
print(num2 < num3)
print(num2 <= num3)
print(num2 > num1)
print(num2 == num3)

print(num1.issubset(num2))
print(num2.issuperset(num1))


# 集合的方法
# 添加元素
set6: Set[int] = {1,10,100}
set6.add(10000)
set6.add(100)
set6.add(10000)
print(set6)

# 删除元素
set6.discard(10)
if 100 in set6:
    set6.remove(100)
print(set6)

# 清空元素
set6.clear()
print(set6)


set7: Set[str] = {'Java', 'Python', 'C++', 'Kotlin'}
set8: Set[str] = {'Kotlin', 'Swift', 'Java', 'Dart'}
set9: Set[str] = {'HTML', 'CSS', 'JavaScript'}
# 是否存在相同元素，不存在则返回true，存在则返回false
print(set7.isdisjoint(set8))  # False
print(set7.isdisjoint(set9))  # True

set10 = {1,True,'java'}
for i in set10:
    print(i)

element = set10.pop()
print(element)