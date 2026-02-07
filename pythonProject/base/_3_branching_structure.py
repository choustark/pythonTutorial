# python 条件判断

'''
BMI 计算器
Version 1.0
Author Chou
'''
height = float(input('请输入身高（m）:'))
weight = float(input('请输入体重（kg）:'))
bmi = weight / (height * height)
if bmi <= 18.5:
    print('偏瘦')
elif 18.5 < bmi <= 23.9:
    print('正常')
elif 24.0 <= bmi <=27.9:
    print('偏重')
elif bmi >= 28.0:
    print('肥胖')
else:
    print('没有救了');


'''
match case
Version 1.0
Author Chou
'''
status_code = input('请输入状态：')
match status_code:
    case '200':
        description = 'OK'
    case '400':
        description = 'BAD REQUEST'
    case '401':
        description = 'UNAUTHORIZED'
    case '403':
        description = 'FORBIDDEN'
    case '404':
        description = 'NOT FOUND'
    case '500':
        description = 'INTERNAL SERVER ERROR'
    case _:
        description = 'UNKNOWN STAUT CODE'
print(f'状态码：{status_code},状态码描述：{description}')

'''
分段函数求值
Version 1.0
Author Chou
'''

x = float(input('请输入x值：'))
if x > 0:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }')

'''
分段函数求值 - nest 条件嵌套
Version 1.0
Author Chou
'''
x = float(input('请输入x值：'))
if x > 0:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(f'{y= }')

'''
计算三角形的周长和面积
Version 1.0
Author Chou
'''

a = float(input('请输入三角形的边长a：'))
b = float(input('请输入三角形的边长b：'))
c = float(input('请输入三角形的边长c：'))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'三角形的周长为：{perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'三角形面积为：{area}')
else:
    print('不构成三角形')
