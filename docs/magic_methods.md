# Python 魔法方法详解

## 目录

1. [简介](#简介)
2. [对象生命周期](#对象生命周期)
3. [字符串表示](#字符串表示)
4. [比较运算](#比较运算)
5. [算术运算](#算术运算)
6. [反向算术运算](#反向算术运算)
7. [增量赋值运算](#增量赋值运算)
8. [类型转换](#类型转换)
9. [容器协议](#容器协议)
10. [迭代器协议](#迭代器协议)
11. [属性访问](#属性访问)
12. [描述符协议](#描述符协议)
13. [上下文管理器](#上下文管理器)
14. [可调用对象](#可调用对象)
15. [其他常用方法](#其他常用方法)

---

## 简介

魔法方法（Magic Methods），也叫**双下划线方法**（Dunder Methods），是 Python 中以双下划线开头和结尾的特殊方法。它们允许自定义类能够使用 Python 的内置操作（运算符、函数、语法糖）。

```python
class MyClass:
    def __init__(self):      # 魔法方法
        pass
```

---

## 对象生命周期

### `__new__(cls, [...])`

创建对象实例时首先调用，返回实例对象。通常用于实现单例模式或不可变类型。

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

### `__init__(self, [...])`

对象初始化，在 `__new__` 之后调用。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Tom", 18)
```

### `__del__(self)`

对象销毁时调用（垃圾回收）。不推荐依赖此方法进行资源清理。

```python
class TempFile:
    def __del__(self):
        print("对象被销毁")
```

---

## 字符串表示

### `__str__(self)`

`print()` 和 `str()` 调用，返回用户友好的字符串。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

print(Person("Tom"))  # Person: Tom
```

### `__repr__(self)`

交互式环境显示，`repr()` 调用。应返回无歧义、可用于重新创建对象的字符串。

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(1, 2)
print(p)  # Point(1, 2)
# eval(repr(p)) 可以重建对象
```

### `__format__(self, format_spec)`

`format()` 和 f-string 调用。

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __format__(self, format_spec):
        return f"${self.amount:{format_spec}}"

m = Money(1234.5)
print(f"{m:.2f}")  # $1234.50
```

---

## 比较运算

| 方法 | 运算符 |
|------|--------|
| `__lt__` | `<` |
| `__le__` | `<=` |
| `__eq__` | `==` |
| `__ne__` | `!=` |
| `__gt__` | `>` |
| `__ge__` | `>=` |

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person("Tom", 18)
p2 = Person("Jerry", 20)
print(p1 < p2)   # True
print(p1 == p2)  # False
```

### 使用 `@total_ordering` 简化

只需定义 `__eq__` 和一个比较方法，自动生成其他。

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person(18)
p2 = Person(20)
print(p1 <= p2)  # True（自动生成）
```

---

## 算术运算

| 方法 | 运算符 | 说明 |
|------|--------|------|
| `__add__` | `+` | 加法 |
| `__sub__` | `-` | 减法 |
| `__mul__` | `*` | 乘法 |
| `__truediv__` | `/` | 真除法 |
| `__floordiv__` | `//` | 地板除 |
| `__mod__` | `%` | 取模 |
| `__divmod__` | `divmod()` | 返回 (商, 余数) |
| `__pow__` | `**` 或 `pow()` | 幂运算 |
| `__lshift__` | `<<` | 左移 |
| `__rshift__` | `>>` | 右移 |
| `__and__` | `&` | 按位与 |
| `__xor__` | `^` | 按位异或 |
| `__or__` | `\|` | 按位或 |
| `__matmul__` | `@` | 矩阵乘法 |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # Vector(4, 6)
print(v1 * 3)     # Vector(3, 6)
```

---

## 反向算术运算

当左操作数不支持该运算时，调用右操作数的对应方法。

| 方法 | 运算符 |
|------|--------|
| `__radd__` | `+` |
| `__rsub__` | `-` |
| `__rmul__` | `*` |
| `__rtruediv__` | `/` |
| ... | ... |

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __radd__(self, other):
        return Number(other + self.value)

n = Number(10)
result = 5 + n  # 调用 n.__radd__(5)
```

---

## 增量赋值运算

| 方法 | 运算符 |
|------|--------|
| `__iadd__` | `+=` |
| `__isub__` | `-=` |
| `__imul__` | `*=` |
| `__itruediv__` | `/=` |
| ... | ... |

```python
class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

c = Counter(10)
c += 5
print(c.value)  # 15
```

---

## 类型转换

| 方法 | 内置函数 |
|------|----------|
| `__bool__` | `bool()` |
| `__int__` | `int()` |
| `__float__` | `float()` |
| `__complex__` | `complex()` |
| `__str__` | `str()` |
| `__bytes__` | `bytes()` |
| `__hash__` | `hash()` |
| `__index__` | 用于切片、hex()等 |

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return int(self.amount)

    def __float__(self):
        return float(self.amount)

    def __bool__(self):
        return self.amount > 0

m = Money(99.99)
print(int(m))    # 99
print(float(m))  # 99.99
print(bool(m))   # True
```

---

## 容器协议

### 大小相关

| 方法 | 说明 |
|------|------|
| `__len__(self)` | `len(obj)` |
| `__length_hint__(self)` | 估计长度（优化用） |

### 元素访问

| 方法 | 说明 |
|------|------|
| `__getitem__(self, key)` | `obj[key]` |
| `__setitem__(self, key, value)` | `obj[key] = value` |
| `__delitem__(self, key)` | `del obj[key]` |
| `__contains__(self, item)` | `item in obj` |

```python
class MyList:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __contains__(self, item):
        return item in self._data

    def append(self, item):
        self._data.append(item)

lst = MyList()
lst.append(1)
lst.append(2)
print(len(lst))    # 2
print(lst[0])      # 1
lst[0] = 10
print(1 in lst)    # False
print(10 in lst)   # True
```

---

## 迭代器协议

### `__iter__(self)`

返回迭代器对象。

### `__next__(self)`

返回下一个元素，没有元素时抛出 `StopIteration`。

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for i in Countdown(3):
    print(i)  # 3, 2, 1
```

---

## 属性访问

### `__getattr__(self, name)`

访问**不存在**的属性时调用。

### `__getattribute__(self, name)`

访问**任意**属性时调用（包括存在的属性，慎用）。

### `__setattr__(self, name, value)`

设置属性时调用。

### `__delattr__(self, name)`

删除属性时调用。

### `__dir__(self)`

`dir(obj)` 调用。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        return f"属性 '{attr}' 不存在"

    def __setattr__(self, name, value):
        print(f"设置属性: {name} = {value}")
        super().__setattr__(name, value)

p = Person("Tom")       # 输出: 设置属性: name = Tom
print(p.name)          # Tom
print(p.age)           # 属性 'age' 不存在
p.age = 18             # 输出: 设置属性: age = 18
```

---

## 描述符协议

描述符是包含以下任意方法的对象：

### `__get__(self, instance, owner)`

获取属性值。

### `__set__(self, instance, value)`

设置属性值。

### `__delete__(self, instance)`

删除属性。

```python
class ValidatedAttribute:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"{self.name} 必须是 {self.type}")
        instance.__dict__[self.name] = value

class Person:
    name = ValidatedAttribute("name", str)
    age = ValidatedAttribute("age", int)

p = Person()
p.name = "Tom"   # OK
p.age = 18       # OK
# p.age = "18"   # TypeError
```

---

## 上下文管理器

### `__enter__(self)`

进入 `with` 块时调用，通常返回资源对象。

### `__exit__(self, exc_type, exc_val, exc_tb)`

退出 `with` 块时调用，用于清理资源。如果返回 `True`，抑制异常。

```python
class MyFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("打开文件")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        self.file.close()
        return False  # 不抑制异常

with MyFile("test.txt", "w") as f:
    f.write("Hello")
    # 退出时自动调用 __exit__
```

---

## 可调用对象

### `__call__(self, [...])`

让对象像函数一样被调用。

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

add_5 = Adder(5)
print(add_5(10))  # 15
```

实际应用：装饰器、策略模式等。

---

## 其他常用方法

### `__hash__(self)`

`hash(obj)` 调用，对象用作字典键或集合元素时需要。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

p = Person("Tom")
print(hash(p))  # 某个整数
```

### `__bool__(self)`

`bool(obj)` 调用，用于真值测试。

### `__bytes__(self)`

`bytes(obj)` 调用。

### `__index__(self)`

用于切片、`hex()`、`oct()` 等需要整数的场景。

### `__copy__(self)` 和 `__deepcopy__(self, memo)`

控制 `copy.copy()` 和 `copy.deepcopy()` 行为。

### `__class__(self)`

对象所属类。

### `__dict__(self)`

对象属性字典。

### `__slots__`

类变量，限制实例属性，节省内存。

```python
class Point:
    __slots__ = ['x', 'y']  # 只能有 x 和 y 属性

p = Point()
p.x = 1
p.y = 2
# p.z = 3  # AttributeError
```

### `__prepare__(metaclass, name, bases, **kwds)`

元类方法，自定义类命名空间。

---

## 最佳实践

1. **成对实现**：实现 `__repr__` 时最好也实现 `__str__`
2. **比较方法**：使用 `@total_ordering` 减少代码
3. **避免过度使用**：`__getattribute__` 会影响所有属性访问，慎用
4. **异常安全**：`__exit__` 应该处理异常并清理资源
5. **不可变对象**：使用 `__slots__` 和 `frozen=True` 的 dataclass

---

## 参考资源

- [Python 官方文档 - Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [Data Model - Python](https://docs.python.org/3/reference/datamodel.html)
