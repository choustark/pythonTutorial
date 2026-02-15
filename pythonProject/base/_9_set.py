'''
集合的基本语法
特点
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


# ============ 补充：集合的其他重要特性 ============

# 1. 构造集合 - 从其他类型转换
list_data = [1, 2, 2, 3, 3, 3]
string_data = "hello"
set_from_list = set(list_data)          # {1, 2, 3} - 去重！
set_from_string = set(string_data)      # {'h', 'e', 'l', 'o'}
empty_set = set()                       # 注意：{} 是空字典，不是空集合！
print(f"列表去重: {list_data} -> {set_from_list}")
print(f"字符串转集合: {set_from_string}")
print(f"空集合: {empty_set}, 类型: {type(empty_set)}")

# 2. 集合推导式
squares = {x ** 2 for x in range(5)}           # {0, 1, 4, 9, 16}
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}  # {0, 4, 16, 36, 64}
print(f"平方集合: {squares}")
print(f"偶数平方: {even_squares}")

# 3. 集合长度
nums = {1, 2, 3, 4, 5}
print(f"集合长度: {len(nums)}")

# 4. 浅拷贝
original = {1, 2, 3}
copied = original.copy()
original.add(99)
print(f"原集合: {original}, 拷贝: {copied}")

# 5. 就地更新方法（不返回新集合，直接修改原集合）
a = {1, 2, 3}
b = {3, 4, 5}
a.difference_update(b)      # a = a - b，就地修改
print(f"差集更新: {a}")

a = {1, 2, 3}
a.intersection_update(b)    # a = a & b
print(f"交集更新: {a}")

a = {1, 2, 3}
a.symmetric_difference_update(b)  # a = a ^ b
print(f"对称差更新: {a}")

# 6. frozenset - 不可变集合（可作字典的键）
fs = frozenset([1, 2, 3])
# fs.add(4)  # TypeError! 不可修改
print(f"frozenset: {fs}, 类型: {type(fs)}")

# frozenset 可作为字典键
dict_with_frozenset = {frozenset({1, 2}): "value1", frozenset({3, 4}): "value2"}
print(f"frozenset作字典键: {dict_with_frozenset}")

# 7. 实用场景：去重并保持顺序（Python 3.7+）
def unique_ordered(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]

duplicates = [3, 1, 2, 3, 2, 1, 4]
print(f"去重保序: {duplicates} -> {unique_ordered(duplicates)}")