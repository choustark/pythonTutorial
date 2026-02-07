import math

"""
算术运算符

Version: 1.0
Author: Chou
"""

print(321+12) #加
print(321-12) #减
print(321*12) #乘
print(321/12) # 除
print(321//12) # 整除运算
print(321%12) #求模运算
print(3218812) #求幂运算

"""
算术运算的优先级

Version: 1.0
Author: Chou
"""
print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625

"""
赋值运算符和复合赋值运算符

Version: 1.0
Author: Chou
"""
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)

"""
海象运算符

Version: 1.0
Author: Chou
"""
print((a:=10))
print(a)

"""
比较运算符和逻辑运算符的使用

Version: 1.0
Author: Chou
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False


'''
温度单位转换
Version: 1.0
Author: Chou
'''
f: float = float(input('请输入华氏温度：'))
c: float  = (f-32)/1.8
print('%.1f华氏度 = %.1f摄氏度'%(f,c))
#第二种格式化方式
print(f'{f:.1f}华氏度={c:.1f}摄氏度')

'''
计算圆的半径
Version: 1.0
Author: Chou
'''
radius = float(input('请输入圆的半径：'))
# 周长
circumference = 2 * math.pi * radius
# 面积
area = math.pi * radius * radius
print('%.2f的圆的周长是%.2f，面积是%.2f'%(radius,circumference,area))
print(f'{radius:.2f}的半径的周长是{circumference:.2f},面积是{area:.2f}')


'''
闰年计算
Version: 1.0
Author: Chou
'''
year: int = int(input('请输入年份：'))
is_leap= year % 4 == 0 and year % 100 !=0 or year % 400 == 0
print(f'{is_leap}')



