"""
使用Python内置的open函数来打开文件，在使用open函数时，
我们可以通过函数的参数指定文件名、操作模式和字符编码等信息，接下来就可以对文件进行读写操作了

| 操作模式 | 具体含义                           |
|---------|----------------------------------|
| 'r'     | 读取（默认）                      |
| 'w'     | 写入（会先截断之前的内容）        |
| 'x'     | 写入，如果文件已经存在会产生异常  |
| 'a'     | 追加，将内容写入到已有文件的末尾  |
| 'b'     | 二进制模式                        |
| 't'     | 文本模式（默认）                  |
| '+'     | 更新（既可以读又可以写）          |
"""
from typing import TextIO
#
# file: TextIO = open("E:\\jast\\pythonTutorial\\pythonProject\\《凡人修仙传》(精校版)_qinkan.net.txt",
#                     encoding="GB2312", errors="ignore")
# print(file.read())
# file.close()

# for line in file:
#     print(line.strip())
# file.close()
# file: TextIO = open("E:\\jast\\pythonTutorial\\pythonProject\\《凡人修仙传》(精校版)_qinkan.net.txt",'a',
#                    encoding="GB2312", errors="ignore")
# file.write("\n书名：凡人修仙传")
# file.write("\n作者：忘语")
# file.write("\n时间：2025年10月16日22:39:34")
# file.close()

# file: TextIO = None
#
# try:
#     file = open("E:\\jast\\pythonTutorial\\pythonProject\\《凡人修仙传》(精校版)_qinkan.net.txt", 'r')
#     print(file.read())
# except FileNotFoundError:
#     print("无法找到执行的文件")
# except LookupError:
#     print("未知的字符编码")
# except UnicodeDecodeError:
#     print("解码错误")
# finally:
#     if file:
#         file.close()

# try:
#     with open("E:\\jast\\pythonTutorial\\pythonProject\\《凡人修仙传》(精校版)_qinkan.net.txt",'r',
#               encoding="GB2312") as file:
#         print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError as e:
#     print('读取文件时解码错误!',e)


# 自定义异常类型，继承Exception
class MyInputException(Exception):
    """
    自定义异常类型
    """

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return self.args[0]


def get_input():
    """
    获取用户输入
    :return:
    """
    while True:
        try:
            num = int(input("请输入一个数字："))
            if num < 0:
                raise MyInputException("输入的数字必须大于0")
            return num
        except ValueError:
            print("输入的数字必须为整数")
        except MyInputException as e:
            print(e)

get_input()