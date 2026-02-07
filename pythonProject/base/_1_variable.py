print('---------------------------')
"""整型"""
print(0b100)
print(0o100)
print(100)
print(0x100)
print('---------------------------')
'''浮点型'''
print(123.456)  # 数学写法
print(1.23456e2)  # 科学计数法

print('---------------------------')
'''字符串型字符串型'''
print('这是字符串！')

print('---------------------------')
'''布尔'''
print(True)

# 惯例部分：
# 惯例1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
# 惯例2：受保护的变量用单个下划线开头。
# 惯例3：私有的变量用两个下划线开头。

#类型转换操作


print('--------------------类型转换操作-----------------')

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello world'
g = True

print(float(a))
print(int(b))
print(int(c))
print(int(c,base=16))
print(int(d,base=2))
print(float(e))
print(bool(f))
print(int(g))
print(chr(a))
print(ord('d'))