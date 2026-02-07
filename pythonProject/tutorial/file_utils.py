import os

"""
输入目录路径，统计出文件总数以及文件后缀名称总数
将结果结构化输出
"""


def file_type_count(path: str) -> dict[str, int]:
    """
    统计文件类型
    :param path: 文件路径
    :return: 文件类型统计结果
    """
    fileType: dict[str, int] = {}
    for root, dirs, files in os.walk(path):
        for fileName in files:
            '''file_type = os.path.splitext(fileName)[1]'''
            ext: str = os.path.splitext(fileName)[1].lstrip(".")
            '''fileType.update({file_type: fileType.get(file_type, 0) + 1})'''
            fileType[ext] = fileType.get(ext, 0) + 1
            '''print(file_type)'''
    return fileType


def create_temp_file(content: str) -> None:
    """
    在当前目录创建临时文件
    :param content: 文本你同
    :return:
    """




if __name__ == '__main__':
    print(f'\n文件类型统计结果为：')
    print(file_type_count("F:\\学习视频\\20250810"))
