'''
字符串
字符串讲解
'''

'''
字符串的声明
'''
s1: str = 'zhangsan'
s2: str = "zhangsan"
s3: str = '''
Chou,
wonderful,
world!
'''
print(s1)
print(s2)
print(s3)


'''
转义字符
\ 
'''
s4:  str = '\'hello, world!\''
s5:  str = '\\hello, world!\\'
print(s4)
print(s5)

'''
原始字符创
r''
'''
s6: str = '\it \is \time \to \fuck \now'
print(s6)
s7: str = r'\it \is \time \to \fuck \now'
print(s7)

'''
字符的特殊表示
'''
s8: str = '\141\142\143\x61\x62\x63'
print(s8)
s9: str = '\u4e2a\u4eba'
print(s9)

'''
字符串的运算
'''

s10: str = 'hello, world!'
print(s10)
s11:  str = s10 * 3
print(s11)
s10 += s11
print(s10)
s10 *= 10
print(s10)

'''
比较运算
'''
s12: str = 'hello, world!'
s13: str = 'hello, world.'
print(f's12 == s13:{s12 == s13}')

s14: str = '今天是周四，2025年6月25日21:26:31'
print('周四'in s14)
print('周四'not in s14)
print(len(s14))

# 索引与切片
s15: str = ('abcdefg')
n: int = len(s15)
print(s15[0])
print(s15[n-1])
print(s15[-1])
print(s15[1:5:2])
print(s15[1:5])

# 字符串的遍历
s16: str = "hello"
for i in range(len(s16)):
    print(s16[i])

name: str = 'zhangsan,张三'


'''
字符串的方法
'''
# 大小写操作
print(name.upper())
s17: str = 'HELLO, WORLD!'
print(s17.lower())
s18: str = 'hello, world!'
print(s18.capitalize()) #首字母大写
print(s18.title()) # 每个单词首字母大写

# 查找操作
print(s18.find('o'))






