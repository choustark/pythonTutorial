"""
Python IO 操作完整指南 - 面向Java开发者

==========================================
一、文件操作 (File Operations)
==========================================

Java vs Python 对比:
Java:      new FileReader("file.txt")
Python:    open("file.txt", "r")

# 操作模式说明:
'r'  - 只读 (默认)     [Java: FileReader]
'w'  - 写入(覆盖)      [Java: FileWriter, new FileOutputStream()]
'a'  - 追加            [Java: FileWriter with true append flag]
'r+' - 读写模式        [Java: RandomAccessFile]
'b'  - 二进制模式      [Java: InputStream/OutputStream]
't'  - 文本模式(默认)  [Java: Reader/Writer]
"""

from pathlib import Path
import json
import pickle
import io
import os

# ============================================================================
# 1. 基础文件读写 - 使用 with 语句 (推荐)
# ============================================================================

def demo_with_statement():
    """
    with 语句 = Java 的 try-with-resources
    自动关闭资源，即使发生异常
    """
    # 写入文件
    with open('demo.txt', 'w', encoding='utf-8') as f:
        f.write('Hello Python!\n')
        f.write('第二行内容\n')

    # 读取文件 - 全部读取
    with open('demo.txt', 'r', encoding='utf-8') as f:
        content = f.read()          # 读取全部内容 [Java: readAllBytes()]
        print("全部内容:", content)

    # 读取文件 - 逐行读取 [Java: BufferedReader.readLine()]
    with open('demo.txt', 'r', encoding='utf-8') as f:
        for line in f:              # 直接迭代，更简洁
            print(f"行内容: {line.strip()}", end=' ')

    # 读取文件 - 读取所有行到列表 [Java: Files.readAllLines()]
    with open('demo.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"\n行列表: {lines}")


def demo_read_methods():
    """
    不同的读取方法对比
    """
    with open('demo.txt', 'w', encoding='utf-8') as f:
        f.write('第一行\n第二行\n第三行\n')

    with open('demo.txt', 'r', encoding='utf-8') as f:
        # read() - 读取全部内容
        all_content = f.read()
        print("read() 全部内容:", repr(all_content))

    with open('demo.txt', 'r', encoding='utf-8') as f:
        # read(n) - 读取n个字符 [Java: read(char[], off, len)]
        first_5 = f.read(5)
        print("read(5) 前5字符:", repr(first_5))

    with open('demo.txt', 'r', encoding='utf-8') as f:
        # readline() - 读取一行 [Java: BufferedReader.readLine()]
        line1 = f.readline()
        line2 = f.readline()
        print("readline() 第一行:", repr(line1))
        print("readline() 第二行:", repr(line2))

    with open('demo.txt', 'r', encoding='utf-8') as f:
        # readlines() - 读取所有行，返回列表
        all_lines = f.readlines()
        print("readlines() 所有行:", all_lines)


# ============================================================================
# 2. 二进制文件操作 (Binary Files)
# ============================================================================

def demo_binary_io():
    """
    二进制模式处理图片、音频等文件
    相当于 Java 的 InputStream/OutputStream
    """
    # 写入二进制数据
    data = b'\x00\x01\x02\x03\x04\x05'  # bytes 类型 [Java: byte[]]
    with open('binary.dat', 'wb') as f:
        f.write(data)

    # 读取二进制数据
    with open('binary.dat', 'rb') as f:
        content = f.read()
        print(f"二进制内容: {content}")
        print(f"十六进制: {content.hex()}")


# ============================================================================
# 3. 内存 IO (StringIO / BytesIO)
# ============================================================================

def demo_memory_io():
    """
    内存中的流操作
    相当于 Java 的 CharArrayReader / StringWriter / ByteArrayOutputStream
    """
    # StringIO - 文本内存流 [Java: StringWriter / CharArrayWriter]
    text_io = io.StringIO()
    text_io.write("第一行\n")
    text_io.write("第二行\n")
    # 获取内容 [Java: toString()]
    content = text_io.getvalue()
    print("StringIO 内容:", content)

    # BytesIO - 二进制内存流 [Java: ByteArrayOutputStream]
    binary_io = io.BytesIO()
    binary_io.write(b'\x00\x01\x02')
    binary_data = binary_io.getvalue()
    print("BytesIO 内容:", binary_data)


# ============================================================================
# 4. 文件路径操作 (pathlib - 推荐使用)
# ============================================================================

def demo_pathlib():
    """
    现代化的路径操作
    相当于 Java 的 Path / Paths 类
    """
    # 创建路径对象 [Java: Paths.get()]
    path = Path('demo.txt')

    print(f"文件名: {path.name}")              # [Java: getFileName()]
    print(f"父目录: {path.parent}")            # [Java: getParent()]
    print(f"扩展名: {path.suffix}")            # [Java: 获取后缀需自定义]
    print(f"绝对路径: {path.absolute()}")      # [Java: toAbsolutePath()]
    print(f"文件存在: {path.exists()}")        # [Java: Files.exists()]
    print(f"文件大小: {path.stat().st_size}")  # [Java: Files.size()]

    # 创建目录 [Java: Files.createDirectories()]
    dir_path = Path('test_dir/sub_dir')
    dir_path.mkdir(parents=True, exist_ok=True)

    # 遍历目录 [Java: Files.walk()]
    current_dir = Path('.')
    for item in current_dir.iterdir():
        if item.is_file():
            print(f"文件: {item.name}")
        elif item.is_dir():
            print(f"目录: {item.name}/")


# ============================================================================
# 5. JSON 操作
# ============================================================================

def demo_json_io():
    """
    JSON 序列化和反序列化
    相当于 Java 的 Jackson / Gson
    """
    data = {
        "name": "张三",
        "age": 25,
        "skills": ["Python", "Java", "JavaScript"]
    }

    # 写入 JSON 文件 [Java: objectMapper.writeValue()]
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 读取 JSON 文件 [Java: objectMapper.readValue()]
    with open('data.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        print(f"读取的JSON: {loaded_data}")

    # JSON 字符串转换 [Java: objectMapper.writeValueAsString()]
    json_str = json.dumps(data, ensure_ascii=False)
    print(f"JSON字符串: {json_str}")

    parsed = json.loads(json_str)
    print(f"解析后的对象: {parsed}")


# ============================================================================
# 6. 序列化 (Pickle)
# ============================================================================

def demo_pickle():
    """
    Python 对象序列化
    相当于 Java 的 Serializable / ObjectOutputStream
    注意: Pickle 是 Python 特有的，不安全用于不可信数据
    """
    # 序列化对象 [Java: ObjectOutputStream.writeObject()]
    data = {
        'name': '李四',
        'scores': [95, 87, 92],
        'nested': {'a': 1, 'b': 2}
    }

    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)

    # 反序列化 [Java: ObjectInputStream.readObject()]
    with open('data.pkl', 'rb') as f:
        loaded = pickle.load(f)
        print(f"反序列化数据: {loaded}")


# ============================================================================
# 7. 文件和目录操作 (os / shutil)
# ============================================================================

def demo_file_operations():
    """
    文件和目录操作
    """
    import shutil

    # 创建测试文件
    Path('test_file.txt').write_text('测试内容', encoding='utf-8')

    # 重命名 [Java: Files.move()]
    if Path('test_file.txt').exists():
        Path('test_file.txt').rename('renamed_file.txt')

    # 复制文件 [Java: Files.copy()]
    if Path('renamed_file.txt').exists():
        shutil.copy('renamed_file.txt', 'copied_file.txt')

    # 获取文件信息 [Java: Files.readAttributes()]
    if Path('renamed_file.txt').exists():
        stat = Path('renamed_file.txt').stat()
        print(f"文件大小: {stat.st_size} 字节")
        print(f"修改时间: {stat.st_mtime}")

    # 删除文件 [Java: Files.delete()]
    for f in ['renamed_file.txt', 'copied_file.txt']:
        if Path(f).exists():
            Path(f).unlink()


# ============================================================================
# 8. 实用技巧
# ============================================================================

def demo_tips():
    """实用 IO 技巧"""

    # 1. 读取大文件 - 使用生成器避免内存问题
    def read_large_file(file_path):
        """逐行读取大文件，内存友好"""
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()

    # 2. 同时打开多个文件
    with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
        f1.write('内容1')
        f2.write('内容2')

    # 3. 检查文件是否存在后再操作
    file_path = Path('maybe_exists.txt')
    if file_path.exists():
        print(f"文件大小: {file_path.stat().st_size}")
    else:
        print("文件不存在")

    # 4. 使用 contextlib 管理资源
    from contextlib import ExitStack

    files = ['file1.txt', 'file2.txt']
    with ExitStack() as stack:
        handles = [stack.enter_context(open(f, 'r')) for f in files if Path(f).exists()]
        for handle in handles:
            print(handle.read())


# ============================================================================
# 9. 编码处理
# ============================================================================

def demo_encoding():
    """
    字符编码处理
    Python 3 默认使用 UTF-8
    """
    text = "你好，世界！Hello World!"

    # 写入不同编码的文件
    encodings = ['utf-8', 'gbk', 'utf-16']

    for enc in encodings:
        filename = f'text_{enc}.txt'
        with open(filename, 'w', encoding=enc) as f:
            f.write(text)

    # 读取时指定正确编码
    for enc in encodings:
        filename = f'text_{enc}.txt'
        try:
            with open(filename, 'r', encoding=enc) as f:
                content = f.read()
                print(f"{enc}: {content}")
            # 清理
            Path(filename).unlink()
        except UnicodeDecodeError as e:
            print(f"{enc} 解码失败: {e}")


# ============================================================================
# Java vs Python 快速对照表
# ============================================================================

def print_comparison_table():
    """
    Java IO -> Python IO 对照
    """
    comparison = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                    Java vs Python IO 对照                      ║
    ╠════════════════════════════════════════════════════════════════╣
    ║  Java                          │  Python                       ║
    ╠════════════════════════════════════════════════════════════════╣
    ║  FileReader                    │  open(file, 'r')              ║
    ║  FileWriter                    │  open(file, 'w')              ║
    ║  BufferedReader                │  for line in open(file)       ║
    ║  FileInputStream               │  open(file, 'rb')             ║
    ║  ByteArrayOutputStream         │  io.BytesIO()                 ║
    ║  StringWriter                  │  io.StringIO()                ║
    ║  Files.readAllLines()          │  f.readlines()                ║
    ║  Files.writeString()           │  f.write()                    ║
    ║  try-with-resources            │  with open() as f:            ║
    ║  Paths.get()                   │  Path()                       ║
    ║  Files.exists()                │  Path.exists()                ║
    ║  Jackson/Gson                  │  json module                  ║
    ║  Serializable                  │  pickle module                ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(comparison)


# ============================================================================
# 主函数 - 运行所有演示
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Python IO 操作演示 - 面向Java开发者")
    print("=" * 60)

    print("\n【1. with 语句演示】")
    demo_with_statement()

    print("\n【2. 读取方法对比】")
    demo_read_methods()

    print("\n【3. 二进制IO】")
    demo_binary_io()

    print("\n【4. 内存IO】")
    demo_memory_io()

    print("\n【5. Pathlib 路径操作】")
    demo_pathlib()

    print("\n【6. JSON 操作】")
    demo_json_io()

    print("\n【7. Pickle 序列化】")
    demo_pickle()

    print("\n【8. 文件操作】")
    demo_file_operations()

    print("\n【9. 编码处理】")
    demo_encoding()

    print("\n【Java vs Python 对照表】")
    print_comparison_table()
