"""
Python os 模块完整指南 - 面向Java开发者

==========================================
os 模块：Python 与操作系统交互的核心模块
==========================================

Java vs Python 对照:
Java:      java.io.File, java.nio.file.Files, java.lang.System
Python:    os 模块, pathlib 模块

os 模块主要功能:
├── 文件/目录操作 (创建、删除、重命名)
├── 路径操作 (拼接、分解、获取信息)
├── 环境变量和系统信息
├── 进程管理
└── 系统命令执行
"""

import os
import sys
import platform
from pathlib import Path
import time
import shutil


# ============================================================================
# 一、系统信息 (System Information)
# ============================================================================

def demo_system_info():
    """
    获取系统信息
    对应 Java: System.getProperty(), System.getenv()
    """
    print("=" * 60)
    print("【系统信息】")
    print("=" * 60)

    # 操作系统类型 [Java: System.getProperty("os.name")]
    print(f"操作系统: {os.name}")  # 'nt' (Windows), 'posix' (Linux/Mac)
    print(f"平台: {platform.system()}")  # 'Windows', 'Linux', 'Darwin'
    print(f"平台详情: {platform.platform()}")

    # 当前工作目录 [Java: Paths.get("").toAbsolutePath()]
    print(f"当前工作目录: {os.getcwd()}")

    # 登录用户名 [Windows]
    print(f"当前用户: {os.getlogin()}")

    # Python 解释器路径
    print(f"Python 路径: {sys.executable}")

    # 环境变量 [Java: System.getenv()]
    print(f"\n--- 环境变量 ---")
    print(f"PATH: {os.environ.get('PATH', '未定义')}")
    print(f"HOME: {os.environ.get('HOME', os.environ.get('USERPROFILE', '未定义'))}")
    print(f"所有环境变量数量: {len(os.environ)}")


# ============================================================================
# 二、路径操作 (Path Operations)
# ============================================================================

def demo_path_operations():
    """
    路径操作
    对应 Java: java.nio.file.Paths, java.io.File
    """
    print("\n" + "=" * 60)
    print("【路径操作】")
    print("=" * 60)

    # 路径拼接 [Java: path.resolve(child) / Paths.get()]
    path1 = "folder"
    path2 = "subfolder"
    file_name = "test.txt"

    # os.path.join - 跨平台路径拼接 (推荐)
    full_path = os.path.join(path1, path2, file_name)
    print(f"拼接路径: {full_path}")

    # 绝对路径 [Java: toAbsolutePath()]
    abs_path = os.path.abspath("test.txt")
    print(f"绝对路径: {abs_path}")

    # 路径分解
    print(f"\n--- 路径分解 ---")
    test_path = r"E:\jast\pythonTutorial\pythonProject\test.txt"
    print(f"目录名: {os.path.dirname(test_path)}")    # [Java: getParent()]
    print(f"文件名: {os.path.basename(test_path)}")   # [Java: getFileName()]
    print(f"扩展名: {os.path.splitext(test_path)[1]}") # [Java: 获取后缀需自定义]

    # 判断路径类型 [Java: Files.isDirectory() / isRegularFile()]
    print(f"\n--- 路径类型判断 ---")
    print(f"是否为绝对路径: {os.path.isabs(test_path)}")
    print(f"当前目录是否存在: {os.path.exists('.')}")
    print(f"是否为目录: {os.path.isdir('.')}")
    print(f"是否为文件: {os.path.isfile('_7_os_module.py')}")

    # 规范化路径 [Java: normalize()]
    messy_path = "./folder/../folder/./test.txt"
    normalized = os.path.normpath(messy_path)
    print(f"规范化前: {messy_path}")
    print(f"规范化后: {normalized}")


# ============================================================================
# 三、目录操作 (Directory Operations)
# ============================================================================

def demo_directory_operations():
    """
    目录操作
    对应 Java: Files.createDirectory(), Files.delete(), etc.
    """
    print("\n" + "=" * 60)
    print("【目录操作】")
    print("=" * 60)

    # 创建测试目录
    test_dir = "test_os_dir"
    sub_dir = os.path.join(test_dir, "sub_dir")

    # 创建单个目录 [Java: Files.createDirectory()]
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
        print(f"创建目录: {test_dir}")

    # 创建多级目录 [Java: Files.createDirectories()]
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir, exist_ok=True)
        print(f"创建多级目录: {sub_dir}")

    # 列出目录内容
    print(f"\n--- 列出当前目录内容 ---")
    # os.listdir() - 返回文件名列表 [Java: File.list()]
    items = os.listdir('.')
    print(f"listdir() 结果数量: {len(items)}")

    # os.scandir() - 返回迭代器，性能更好 (Python 3.5+)
    print("\n使用 scandir() (更高效):")
    with os.scandir('.') as entries:
        for entry in entries:
            if entry.is_file():
                print(f"  [FILE] {entry.name}")
            elif entry.is_dir():
                print(f"  [DIR]  {entry.name}/")

    # os.walk() - 递归遍历目录树 [Java: Files.walk()]
    print("\n--- 递归遍历目录树 (walk) ---")
    for root, dirs, files in os.walk('.'):
        level = root.count(os.sep) - 1
        indent = ' ' * 2 * level
        print(f"{indent}[DIR] {os.path.basename(root)}/")
        sub_indent = ' ' * 2 * (level + 1)
        for file in files[:5]:  # 只显示前5个
            print(f"{sub_indent}[FILE] {file}")
        if level > 1:  # 限制深度
            break

    # 删除目录
    try:
        os.rmdir(test_dir)  # 只能删除空目录 [Java: Files.delete()]
        print(f"\n删除空目录: {test_dir}")
    except OSError:
        # 删除非空目录需要用 shutil.rmtree()
        shutil.rmtree(test_dir)
        print(f"\n删除非空目录: {test_dir}")


# ============================================================================
# 四、文件操作 (File Operations)
# ============================================================================

def demo_file_operations():
    """
    文件操作
    对应 Java: java.nio.file.Files
    """
    print("\n" + "=" * 60)
    print("【文件操作】")
    print("=" * 60)

    test_file = "test_os_file.txt"

    # 创建/重命名/删除文件
    if os.path.exists(test_file):
        os.remove(test_file)  # [Java: Files.delete()]

    # 创建空文件 [Java: Files.createFile()]
    with open(test_file, 'w') as f:
        f.write("测试内容")

    # 获取文件信息 [Java: Files.getAttribute()]
    print(f"--- 文件信息: {test_file} ---")
    print(f"文件大小: {os.path.getsize(test_file)} 字节")    # [Java: Files.size()]
    print(f"修改时间: {os.path.getmtime(test_file)}")        # [Java: Files.getLastModifiedTime()]
    print(f"访问时间: {os.path.getatime(test_file)}")
    print(f"创建时间: {os.path.getctime(test_file)}")        # Windows: 创建时间

    # 格式化时间
    mtime = os.path.getmtime(test_file)
    print(f"修改时间(可读): {time.ctime(mtime)}")

    # 重命名文件 [Java: Files.move()]
    new_name = "test_os_file_renamed.txt"
    if os.path.exists(test_file):
        os.rename(test_file, new_name)
        print(f"\n重命名: {test_file} -> {new_name}")

    # 删除文件
    if os.path.exists(new_name):
        os.remove(new_name)
        print(f"删除文件: {new_name}")


# ============================================================================
# 五、文件权限操作 (File Permissions)
# ============================================================================

def demo_permissions():
    """
    文件权限操作 (主要在 Unix/Linux 系统)
    对应 Java: Files.setPosixFilePermissions()
    """
    print("\n" + "=" * 60)
    print("【文件权限】")
    print("=" * 60)

    test_file = "permission_test.txt"
    with open(test_file, 'w') as f:
        f.write("test")

    # 检查文件权限 [Java: Files.isReadable()]
    print(f"可读: {os.access(test_file, os.R_OK)}")
    print(f"可写: {os.access(test_file, os.W_OK)}")
    print(f"可执行: {os.access(test_file, os.X_OK)}")
    print(f"文件存在: {os.access(test_file, os.F_OK)}")

    # 更改权限 (Unix/Linux)
    if os.name == 'posix':
        # os.chmod() - 更改权限 [Java: Files.setPosixFilePermissions()]
        # 0o755 = rwxr-xr-x
        os.chmod(test_file, 0o755)
        print(f"已设置权限为 755")

    # 清理
    os.remove(test_file)


# ============================================================================
# 六、进程管理 (Process Management)
# ============================================================================

def demo_process_management():
    """
    进程管理
    对应 Java: ProcessBuilder, Runtime.exec()
    """
    print("\n" + "=" * 60)
    print("【进程管理】")
    print("=" * 60)

    # 获取当前进程ID [Java: ProcessHandle.current().pid()]
    print(f"当前进程ID: {os.getpid()}")
    print(f"父进程ID: {os.getppid()}")

    # 执行系统命令
    print("\n--- 执行系统命令 ---")

    # os.system() - 简单执行，返回退出码 [Java: Runtime.exec()]
    return_code = os.system("echo 'Hello from os.system'")  # Windows
    print(f"命令返回码: {return_code}")

    # os.popen() - 获取命令输出
    print("\n使用 popen() 获取输出:")
    with os.popen("dir") as stream:  # Windows: dir, Linux: ls
        output = stream.read()
        print(f"输出前100字符: {output[:100]}...")


# ============================================================================
# 七、环境变量操作 (Environment Variables)
# ============================================================================

def demo_environment_variables():
    """
    环境变量操作
    对应 Java: System.getenv(), System.setProperty()
    """
    print("\n" + "=" * 60)
    print("【环境变量】")
    print("=" * 60)

    # 获取环境变量 [Java: System.getenv()]
    print(f"PATH: {os.environ.get('PATH', '未定义')[:80]}...")
    print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', '未定义')}")

    # 设置环境变量 (只在当前进程有效)
    os.environ['MY_VAR'] = 'test_value'
    print(f"\n设置 MY_VAR = {os.environ['MY_VAR']}")

    # 删除环境变量
    if 'MY_VAR' in os.environ:
        del os.environ['MY_VAR']
        print("已删除 MY_VAR")


# ============================================================================
# 八、os.path 模块详解 (os.path Module)
# ============================================================================

def demo_os_path_detailed():
    """
    os.path 模块详细方法
    """
    print("\n" + "=" * 60)
    print("【os.path 模块详解】")
    print("=" * 60)

    test_path = r"E:\jast\pythonTutorial\pythonProject\test.txt"

    print(f"测试路径: {test_path}\n")

    # 路径信息
    print("--- 路径信息 ---")
    print(f"exists():      {os.path.exists(test_path)}")
    print(f"isfile():      {os.path.isfile(test_path)}")
    print(f"isdir():       {os.path.isdir(test_path)}")
    print(f"isabs():       {os.path.isabs(test_path)}")
    print(f"islink():      {os.path.islink(test_path)}")
    mount_path = 'C:\\' if os.name == 'nt' else '/'
    print(f"ismount():     {os.path.ismount(mount_path) if os.name == 'nt' else 'N/A'}")

    # 路径分解
    print("\n--- 路径分解 ---")
    print(f"dirname():     {os.path.dirname(test_path)}")
    print(f"basename():    {os.path.basename(test_path)}")
    print(f"split():       {os.path.split(test_path)}")
    print(f"splitext():    {os.path.splitext(test_path)}")

    # 路径转换
    print("\n--- 路径转换 ---")
    print(f"abspath('.'):  {os.path.abspath('.')}")
    print(f"normpath():    {os.path.normpath('./folder/../test.txt')}")
    print(f"realpath():    {os.path.realpath('.')}")

    # 路径比较
    print("\n--- 路径比较 ---")
    path1 = r"E:\jast\test"
    path2 = r"E:\jast\..\jast\test"
    print(f"samefile():    {os.path.samefile(path1, path2) if os.path.exists(path1) else '文件不存在'}")

    # 路径拼接
    print("\n--- 路径拼接 ---")
    print(f"join('a', 'b', 'c'):  {os.path.join('a', 'b', 'c')}")
    print(f"splitdrive():         {os.path.splitdrive(test_path)}")


# ============================================================================
# 九、常用代码模式 (Common Patterns)
# ============================================================================

def demo_common_patterns():
    """
    常用代码模式
    """
    print("\n" + "=" * 60)
    print("【常用代码模式】")
    print("=" * 60)

    # 1. 安全地删除文件
    def safe_remove(filepath):
        """安全删除文件"""
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"✓ 已删除: {filepath}")
        else:
            print(f"✗ 文件不存在: {filepath}")

    # 2. 获取目录大小
    def get_dir_size(directory):
        """获取目录大小"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.isfile(filepath):
                    total_size += os.path.getsize(filepath)
        return total_size

    # 3. 查找文件
    def find_files(directory, pattern):
        """查找匹配模式的文件"""
        matches = []
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if pattern in filename:
                    matches.append(os.path.join(root, filename))
        return matches

    # 4. 创建临时文件
    def create_temp_file(content):
        """创建临时文件"""
        temp_dir = os.path.join(os.getcwd(), "temp")
        os.makedirs(temp_dir, exist_ok=True)
        temp_file = os.path.join(temp_dir, f"temp_{os.getpid()}.txt")
        with open(temp_file, 'w') as f:
            f.write(content)
        return temp_file

    # 演示
    print("\n--- 创建临时文件 ---")
    temp_file = create_temp_file("临时内容")
    print(f"临时文件: {temp_file}")

    print("\n--- 查找 .py 文件 ---")
    py_files = find_files('.', '.py')
    print(f"找到 {len(py_files)} 个 .py 文件")

    # 清理
    if os.path.exists(temp_file):
        os.remove(temp_file)
        if os.path.exists(os.path.dirname(temp_file)):
            os.rmdir(os.path.dirname(temp_file))


# ============================================================================
# 十、Java vs Python 对照表
# ============================================================================

def print_comparison_table():
    """
    Java vs Python os 模块对照表
    """
    comparison = """
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                    Java vs Python os 模块对照                            ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  Java                                      │  Python (os)              ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  文件/路径操作                              │                           ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  new File(path)                            │  无需创建                  ║
    ║  Paths.get(path)                           │  os.path                   ║
    ║  path.resolve(other)                       │  os.path.join()            ║
    ║  path.toAbsolutePath()                     │  os.path.abspath()         ║
    ║  path.normalize()                          │  os.path.normpath()        ║
    ║  path.getParent()                          │  os.path.dirname()         ║
    ║  path.getFileName()                        │  os.path.basename()        ║
    ║  path.startsWith(other)                    │  os.path.commonprefix()    ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  文件检查                                   │                           ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  Files.exists(path)                        │  os.path.exists()          ║
    ║  Files.isDirectory(path)                   │  os.path.isdir()           ║
    ║  Files.isRegularFile(path)                 │  os.path.isfile()          ║
    ║  Files.isSameFile(p1, p2)                  │  os.path.samefile()        ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  文件信息                                   │                           ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  Files.size(path)                          │  os.path.getsize()         ║
    ║  Files.getLastModifiedTime(path)           │  os.path.getmtime()        ║
    ║  Files.getOwner(path)                      │  os.stat()                 ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  文件操作                                   │                           ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  Files.createFile(path)                    │  open(path, 'w')           ║
    ║  Files.delete(path)                        │  os.remove()               ║
    ║  Files.move(src, target)                   │  os.rename()               ║
    ║  Files.copy(src, target)                   │  shutil.copy()             ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  目录操作                                   │                           ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  Files.createDirectory(path)               │  os.mkdir()                ║
    ║  Files.createDirectories(path)             │  os.makedirs()             ║
    ║  Files.list(path)                          │  os.listdir()              ║
    ║  Files.walk(path)                          │  os.walk()                 ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  系统信息                                   │                           ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  System.getProperty("user.dir")            │  os.getcwd()               ║
    ║  System.getProperty("user.home")           │  os.path.expanduser("~")   ║
    ║  System.getProperty("file.separator")      │  os.sep                    ║
    ║  System.getenv("PATH")                     │  os.environ.get("PATH")    ║
    ║  System.getenv()                           │  os.environ                ║
    ║  Runtime.exec("cmd")                       │  os.system()               ║
    ║  ProcessHandle.current().pid()             │  os.getpid()               ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    """
    print(comparison)


# ============================================================================
# os 模块常用函数速查表 (Quick Reference)
# ============================================================================

def print_quick_reference():
    """
    os 模块常用函数速查表
    """
    reference = """
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                      os 模块常用函数速查表                               ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  分类              │  函数                          │  说明              ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  系统信息          │  os.name                       │  操作系统名称      ║
    ║                    │  os.getcwd()                   │  当前工作目录      ║
    ║                    │  os.getpid()                   │  当前进程ID        ║
    ║                    │  os.getlogin()                 │  当前登录用户      ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  路径操作          │  os.path.join()                │  路径拼接          ║
    ║                    │  os.path.abspath()             │  绝对路径          ║
    ║                    │  os.path.dirname()             │  目录名            ║
    ║                    │  os.path.basename()            │  文件名            ║
    ║                    │  os.path.split()               │  分割目录和文件    ║
    ║                    │  os.path.splitext()            │  分割扩展名        ║
    ║                    │  os.path.exists()              │  路径是否存在      ║
    ║                    │  os.path.isfile()              │  是否为文件        ║
    ║                    │  os.path.isdir()               │  是否为目录        ║
    ║                    │  os.path.isabs()               │  是否绝对路径      ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  目录操作          │  os.mkdir()                    │  创建单个目录      ║
    ║                    │  os.makedirs()                 │  创建多级目录      ║
    ║                    │  os.rmdir()                    │  删除空目录        ║
    ║                    │  os.removedirs()               │  删除多级空目录    ║
    ║                    │  os.listdir()                  │  列出目录内容      ║
    ║                    │  os.scandir()                  │  列出目录(高效)    ║
    ║                    │  os.walk()                     │  递归遍历目录      ║
    ║                    │  os.chdir()                    │  改变工作目录      ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  文件操作          │  os.remove()                   │  删除文件          ║
    ║                    │  os.unlink()                   │  删除文件(remove别名)║
    ║                    │  os.rename()                   │  重命名/移动       ║
    ║                    │  os.renames()                  │  递归重命名        ║
    ║                    │  os.stat()                     │  获取文件状态      ║
    ║                    │  os.path.getsize()             │  获取文件大小      ║
    ║                    │  os.path.getmtime()            │  获取修改时间      ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  环境变量          │  os.environ                    │  环境变量字典      ║
    ║                    │  os.getenv()                   │  获取环境变量      ║
    ║                    │  os.putenv()                   │  设置环境变量      ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  进程/命令         │  os.system()                   │  执行系统命令      ║
    ║                    │  os.popen()                    │  执行命令并获取输出║
    ║                    │  os.getpid()                   │  获取进程ID        ║
    ║                    │  os.kill()                     │  终止进程          ║
    ╠══════════════════════════════════════════════════════════════════════════╣
    ║  路径常量          │  os.sep                        │  路径分隔符        ║
    ║                    │  os.pathsep                    │  PATH分隔符        ║
    ║                    │  os.linesep                    │  行分隔符          ║
    ║                    │  os.curdir                     │  当前目录 (.)      ║
    ║                    │  os.pardir                     │  上级目录 (..)     ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    """
    print(reference)


# ============================================================================
# 主函数
# ============================================================================

if __name__ == '__main__':
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "Python os 模块完整教程 - 面向Java开发者" + " " * 10 + "║")
    print("╚" + "═" * 58 + "╝")

    # 运行所有演示
    demo_system_info()
    demo_path_operations()
    demo_directory_operations()
    demo_file_operations()
    demo_permissions()
    demo_process_management()
    demo_environment_variables()
    demo_os_path_detailed()
    demo_common_patterns()

    # 打印对照表
    print("\n" + "=" * 60)
    print("【Java vs Python 对照表】")
    print("=" * 60)
    print_comparison_table()

    print("\n" + "=" * 60)
    print("【os 模块常用函数速查表】")
    print("=" * 60)
    print_quick_reference()
