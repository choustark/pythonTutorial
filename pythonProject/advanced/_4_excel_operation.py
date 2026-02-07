"""
操作excel文件
"""

import csv, random
from xlwt import Workbook, Worksheet, Row
import xlrd


def create_excel_file(file_name: str, sheet_name: str,
                      header: list[str], data: list[list[str]]) -> None:
    """
    创建excel文件
    :param file_name:
    :param sheet_name:
    :param header
    :param data
    :return:
    """
    if file_name is None or sheet_name is None:
        raise ValueError("参数不能为空")
    if not file_name.endswith('.xls'):
        raise ValueError("文件格式错误")
    if header is None or data is None:
        raise ValueError("表头和数据不能为空")
    # 创建文档
    wb: Workbook = Workbook()
    # 创建sheet
    ws: Worksheet = wb.add_sheet(sheet_name)
    # 定义表头
    for index, head in enumerate(header):
        # 写入数据,参数为行，列，值
        ws.write(0, index, head)
    # 写入数据
    for row_index, datum in enumerate(data):
        for col_index, value in enumerate(datum):
            ws.write(row_index + 1, col_index, value)
    #  保存文档
    wb.save(file_name)


header = ['序号', '姓名', '年龄', '性别']
data = [
    [1, '张三', 18, '男'],
    [2, '王五', 19, '女'],
    [3, '赵六', 20, '男'],
    [4, '张三', 18, '男'],
    [5, '王五', 19, '女'],
    [6, '赵六', 20, '男'],
    [7, '张三', 18, '男'],
    [8, '王五', 19, '女'],
    [9, '赵六', 20, '男'],
]

# create_excel_file('test.xls', 'Sheet1', header, data)


header1: list[str] = ['序号', '姓名', '年龄', '性别']
for item in header:
    print(item)


# 读取excel文件
def read_excel_file(file_name: str) -> list[list[str]]:
    """
    读取excel 文件
    :param file_name: 文件名称
    :return: 读取到的数据
    """
    if file_name is None:
        raise ValueError("参数不能为空")
    if not file_name.endswith('.xls'):
        raise ValueError("文件格式错误")
    #读取工作簿
    wb = xlrd.open_workbook_xls(file_name)

    sheet_name = wb.sheet_names()
    print(sheet_name)
    # 通过指定的表单名称获取Sheet对象（工作表）
    sheet = wb.sheet_by_name(sheet_name[0])
    # 获取行数和列数
    print(sheet.nrows, sheet.ncols)

    result: list[list[str]] = []
    # data: list[str] = []
    for row_index in range(sheet.nrows):
        for col_index in range(sheet.ncols):
            result.append([sheet.cell_value(row_index, col_index)])

    return result


datas: list[list[str]] = read_excel_file('test.xls')
print(datas)
