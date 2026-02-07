"""
“序列化（serialization）在计算机科学的数据处理中，
是指将数据结构或对象状态转换为可以存储或传输的形式，
这样在需要的时候能够恢复到原先的状态，
而且通过序列化的数据重新获取字节时，
可以利用这些字节来产生原始对象的副本（拷贝）
“反序列化（deserialization）”
与序列化相反的动作，即从一系列字节中提取数据结构的操作
"""

import json

# my_dict: dict = {
#     "name": "张三",
#     "age": 18,
#     "gender": "男",
#     "hobby": ["football", "swimming", "programming"],
#     "address": {
#         "province": "北京",
#         "city": "北京",
#         "street": "朝阳区"
#     }
# }
#
# with open('data.json','w') as file:
#     json.dump(my_dict, file)


with open("data.json", 'r', encoding="utf-8") as file:
    data = json.load(file)
    print(type(data))
    print(data)

import requests

resp = requests.get('http://v.juhe.cn/todayOnhistory/queryEvent?key=7d9ca00e392bc42527ccb527ae56a827&date=10/17')
if resp.status_code == 200:
    resp.json()
    for item in resp.json()['result']:
        print(item['title'])
        print(item['date'])
        print("--------------")
