# Python OOP 练习清单

## Level 1: 语法热身（封装、继承、多态初体验）

### 1. 银行卡
**目标**：写 `Account` 类，支持 `deposit` / `withdraw` / 交易历史打印；再写 `CreditAccount` 继承它，加上透支额度和手续费。

### 2. 彩色向量
**目标**：写 `Vector2D`，支持加减、模、`__repr__`；再写 `ColorVector` 继承它，多一个 `rgb` 字段，重写 `__add__` 保证颜色也按分量加。

### 3. 动物多态
**目标**：写 `Animal` 基类 + `talk()` 抽象方法；`Dog`/`Cat`/`Cow` 子类各自实现 `talk()`；写函数 `animal_sound(animal: Animal)` 体现多态。

## Level 2: 魔法方法 & 协议

### 4. 可迭代购物车
**目标**：`Cart` 内部用 `list` 存商品，实现 `__len__` / `__getitem__` / `__iter__`，支持 `for` 循环、切片、`sum(cart)` 算总价。

### 5. 上下文管理计时器
**目标**：写 `Timer` 类，`with Timer('task1'):` 离开块时自动打印耗时；用 `__enter__` / `__exit__` 实现。

### 6. 可调用缓存
**目标**：写 `Memoize` 类，把任意函数包装成类实例，内部用 `dict` 缓存，`__call__` 实现缓存命中判断。

## Level 3: 组合 + 设计模式

### 7. 组合图形
**目标**：写 `Circle` / `Rectangle`，再写 `CompoundShape`（组合模式），能统一计算总面积并支持添加/删除子图形。

### 8. 观察者天气站
**目标**：写 `WeatherData`（被观察者）和 `Observer` 基类，实现 `attach` / `detach` / `notify`；两个观察者：`CurrentDisplay` 和 `StatDisplay`，一旦温度更新自动打印。

### 9. 策略折扣
**目标**：写 `Order` 类，把折扣算法做成策略（Strategy 模式）：`NormalDiscount`、`VipDiscount`、`CouponDiscount`，运行时可切换。

## Level 4: 元编程 & 高级技巧

### 10. 自注册工厂
**目标**：写一个基类 `Pet`，用元类自动把子类注册到字典；`get_pet_class('Dog')` 返回 `Dog` 类，体现开放封闭原则。

### 11. 描述符校验
**目标**：写 `Typed` 描述符，保证属性类型；再写 `PositiveInt` 继承它；用它们装饰 `Person` 的 `age`、`salary` 字段，赋错类型直接抛 `TypeError`。

### 12. 数据类 + 可空字段
**目标**：用 `@dataclass` 写 `Employee`，字段：`name`、`salary`、`dept`；`salary` 允许 `None`，写 `post_init` 保证如果 `salary` 为 `None` 时自动从 `dept` 的默认薪资格表里查。

## Level 5: 综合小项目（1~2 小时能写完）

### A. 控制台塔防游戏（回合制）
**需求**：
- 地图类 `GameMap`（二维网格）
- 敌人基类 `Enemy`，子类：`BasicEnemy` / `FastEnemy`
- 塔基类 `Tower`，子类：`GunTower` / `IceTower`（策略模式换攻击算法）
- 主循环：每回合敌人移动、塔攻击、掉血、给钱，直到敌人到达终点或全灭。

### B. 迷你 ORM
**需求**：
- 基类 `Model`，支持字段类 `CharField`、`IntField`
- 元类扫描字段并生成建表 SQL（SQLite）
- 提供 `save()`、`filter()`、`get()` 类方法，能真正读写数据库。
