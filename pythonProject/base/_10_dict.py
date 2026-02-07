'''
字典的基本语法
它以键值对（键和值的组合）的方式把数据组织到一起，我们可以通过键找到与之对应的值并进行操作
字典中的键必须是不可变类型，例如整数（int）、浮点数（float）、字符串（str）、元组（tuple）等类型，这一点跟集合类型对元素的要求是一样的
'''
from typing import Dict

person: Dict[str, str] = {
    'name': 'Chou',
    'age': '18',
    'sex': '男'
}
print(person)

# 使用dict构造函数创建字典
person1: Dict[str, str] = dict(name='Chou', age='28', sex='男')
print(person1)
# 通过内置函数zip 压缩两个序列并创建字段
person2: Dict[str, str] = dict(zip(['name', 'age', 'sex'], ['Chou', '38', '男']))
print(person2)

#遍历字段数据
student: Dict[str, str] = {
    'name': 'Chou',
    'age': '18',
    'sex': '男',
    'phone': '12345678901',
    'email': '12345678901@163.com'
}
print(len(student))  #获取字段长度
for key in student:
    print(key)
    print(student[key])

teach: Dict[str, str] = {
    'name': 'Alex',
    'age': '29',
    'sex': '男',
    'phone': '12345678901',
    'email': ['12345678901@163.com', '12345678901@qq.com'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(teach)

# 字段的运算
teachMan: Dict[str, str] = {
    'name': 'Chou',
    'age': '29',
    'gender': '男',
    'phone': '13879708754',
    'email': ['12345678901@163.com', '12345678901@qq.com'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(teachMan)
## 成员运算
print('name' in teachMan)
print('sex' in teachMan)

##索引运算
print(teachMan['name'])
print(teachMan['age'])
print(teachMan['gender'])
teachMan['phone'] = '13879708001'
teachMan['age'] = '29'
teachMan['email'][0] = '1598312@qq.com'
teachMan['car']['brand'] = 'BMW X5'
print(teachMan)

for key in teachMan:
    print(teachMan[key])

## 字段的方法
luRenJia: Dict[str, str] = {
    'name': 'LurenJia',
    'age': '18',
    'sex': '男',
    'phone': '13879708754',
    'email': ['12345678901@163.com', '12345678901@qq.com'],
    'height': '170',
    'address': '深圳市南山区科技工业园'
}
print(luRenJia.get('name'))
print(luRenJia.get('address'))

luRenYi: Dict[str, str] = {
    'name': 'LurenJia',
    'age': '18',
    'sex': '男',
    'phone': '13879708754'
}
print(luRenYi.keys())
print(luRenYi.values())
print(luRenYi.items())
for key, value in luRenYi.items():
    print(f'key:{key} value:{value}')

luRenYi1: Dict[str, str] = {
    'name': 'LurenJia',
    'age': '20',
    'sex': '男',
    'address': '深圳市南山区科技工业园'
}

## 更新元素
luRenYi.update(luRenYi1)
print(luRenYi)
luRenYi |= luRenYi1
print(luRenYi)

## 删除元素
luRenBin: Dict[str, str] = {
    'name': 'luRenBin',
    'age': '18',
    'sex': '男',
    'phone': '13879708754',
    'email': ['12345678901@163.com', '12345678901@qq.com'],
    'height': '170',
    'address': '深圳市南山区科技工业园'
}
del luRenBin['phone']
print(luRenBin)
luRenBin.pop('email')
print(luRenBin)