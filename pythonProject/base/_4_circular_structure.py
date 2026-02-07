'''
循环语句
'''

import time

number = int(input('请输入循环次数：'))
for index in range(number):
    time.sleep(1)
    print(f'第次{index} 循环，还剩{number-index}次循环')


for index in range(number):
    print(f'i={index}')



'''
对于不需要使用变量的循环用_代替
'''
for _ in range(number):
    print('循环')
    time.sleep(1)


'''
循环求和
'''
total = 0
for index in range(1, 101):
    total += index
print(f'total={total:}')


'''
求100内偶数和
'''
total = 0
for index in range(2,101,2):
    total += index
print(f'0~100内偶数和为={total}')

'''
while 循环
'''
total = 0
i= 1
while i <= 100:
    total += i
    i += 1
print(f'while 循环 total ={total:}')


'''
乘法口诀表
'''
print("乘法口诀表")
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()


"""
输入两个正整数求它们的最大公约数

Version: 1.0
Author: Chou
"""
x = int(input('x = '))
y = int(input('y = '))
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f'最大公约数: {i}')
        break


"""
输入两个正整数求它们的最大公约数

Version: 1.1
Author: Chou
"""
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x     # 将 x 更新为 y % x，y 更新为原来的 x
    # remainder = y % x
    # y = x
    # x = remainder
print(f'最大公约数: {x}')


'''
猜数字游戏
'''
import random

number = random.randint(1, 100)
counter = 0
while True:
    counter +=1
    input_number = int(input('请输入数字：'))
    if input_number > number:
        print('数字太大了')
    elif input_number < number:
        print('数字太小了')
    else:
        print('恭喜你猜对了')
        break

print(f'运气太差了，你一共猜了{counter}次')

'''
for  in range:
else

while:
else
注意else: 循环不被中断则被执行
'''

for i in range(3):
    name = str(input("用户名："))
    password = str(input("密码："))
    if name == 'admin' and password == '12345':
        print("登录成功！")
        break
    else:
        print("登录失败!\n")
else:
    print("账号被锁定！")
