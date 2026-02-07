import logging

"""
包文档说明内容
"""



"""版本信息"""
__version__ = "0.1.0"


"""
作者信息
"""
__author__ = "ChenJinXin"
__license__ = "MIT"
__url__ = ""


"""包级别日志"""
logging = logging.getLogger(__name__)
logging.addHandler(logging.NullHandler())


