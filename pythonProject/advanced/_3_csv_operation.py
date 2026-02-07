"""
操作csv文件
"""

import csv, random


def write_csv(file_name: str) -> None:
    """
    写入csv文件
    :param file_name:
    :return:
    """
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'age', 'score'])
        for i in range(1, 1001):
            if i % 10 == 0:
                continue
            writer.writerow([i, f'张三{i}', random.randint(10, 30), random.randint(60, 100)])


write_csv("student.csv")


def read_csv(file_name: str) -> None:
    """
    读取csv文件
    :param file_name:
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        read_line = csv.reader(file)
        for line in read_line:
            print(line)


read_csv("student.csv")
