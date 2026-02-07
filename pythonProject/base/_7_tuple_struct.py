'''
元组
元组是不可变类型
元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能修改。如果试图修改元组中的元素，将引发TypeError错误。
'''
from typing import Tuple


# 定义一个三元组
t1: Tuple[int,int,int] =  (1,2,31)

print(type(t1))
print(t1)

# 定义一个四元组
t2: Tuple[int, str, float, bool] = (1, 'hello', 3.14, True)
# 查看元素的个数
print(len(t2))
# 索引获取元素
print(t2[1])
print(t2[2])
print(t2[0])


print('-'*60 + '切片运算' + '-'*60)
# 切片运算 [start:end(不包含):stride]
print(t2[1:3])
print(t2[1:])
print(t2[:3])
print(t2[:])
print(t2[::2])

# 拼接元组

print('-'*60 + '拼接元组' + '-'*60)
t3: Tuple[int, str, float, bool] = t1 + t2
print(t3)

print('-'*60 + '循环遍历元组' + '-'*60)
# 循环遍历元组
for i in t3:
    print(i)


print('-'*60 + '比较运算' + '-'*60)
# 比较运算
t4: Tuple[int] =  (1,2,31)
print(t1 == t3)            # False
print(t1 == t4)            # True
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False

print('-' * 60 + '打包和解包操作' + '-' * 60)
# 1、把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型 （打包）
# 2、一个元组赋值给多个变量时，元组会解包成多个值 （解包）
a: int = 1,10,90
print(type(a))
print(a)
b,c,d = a
print(b,c,d)

'''
如果解包时元素个数不对应则会报错，可以使用 * 来解决，别标注的*的变量可以接受多个值，并且信号有且只能出现一次
'''
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)
i, *j, k = a
print(i, j, k)
*i, j, k = a
print(i, j, k)

# 解包对所有的序列都成立，例如解包一个列表
a, b, *c = range(1, 10)
print(a, b, c)

a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

print('-' * 60 + '交换变量的值' + '-' * 60)
a: int = 1
b: int = 10
a, b = b, a
print(a, b)

a: int = 1
b: int = 10
b: int = 20
a,b,c = b,c,a
print(a, b, c)

# 如果有多于三个变量的值要依次互换，这个时候是没有直接可用的字节码指令的，需要通过打包解包的方式来完成变量之间值的交换。


print('-' * 60 + '元组和列表的比较' + '-' * 60)
infos = ('Chou', 43, True, '广东深圳')
# 将元组转换成列表
print(list(infos))  # ['Chou', 43, True, '广东深圳']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')

