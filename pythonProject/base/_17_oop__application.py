"""
python  oop 应用
"""

# 1. 银行卡
# **目标**：写 `Account` 类，支持 `deposit` / `withdraw` / 交易历史打印；
# 再写 `CreditAccount` 继承它，加上透支额度和手续费。

import time
from datetime import datetime, date, time


class Account:
    __slots__ = 'balance'
    # 交易历史
    transaction_history: list = []

    def __init__(self, balance: float):
        self.balance = balance
        self.transaction_history.clear()

    def deposit(self, amount: float,
                transaction_history: list | None = None) -> str:
        """
        存款方法
        :param transaction_history:
        :param amount: 金额
        :return: 提示信息
        """
        self.balance += amount
        transaction_history.append(f"操作时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}，存款{amount}")
        return f"存款成功，余额为{self.balance}"

    def withDraw(self, amount: float,
                 transaction_history: list | None = None) -> str:
        """
        取款操作
        :param amount 需要撤回的金额
        :return: 撤回是否成功
        """
        if amount > self.balance:
            return f"取款失败,余额不足！"
        self.balance -= amount
        transaction_history.append(f"操作时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}，取款{amount}")
        return f"取款成功，当前余额为{self.balance}"

    def print_transaction_history(self):
        """
        打印交易历史
        :return:
        """
        print("交易历史如下：")
        for item in self.transaction_history:
            print(item)


class CreditAccount(Account):
    """
    透支账户
    """

    def __init__(self, balance: float, credit_limit: float, fee: float):
        """
        构造方法
        :param balance:  余额
        :param credit_limit: 信用额度
        :param fee: 手续费
        """
        super().__init__(balance)
        self.credit_limit = credit_limit
        self.fee = fee

    def withDraw(self, amount: float,
                 transaction_history: list | None = None) -> str:
        """
        提取
        :param amount:
        :param transaction_history:
        :return:
        """
        if amount > self.balance + self.credit_limit:
            return f"取款失败,余额不足！"
        self.balance -= amount
        transaction_history.append(f"操作时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}，取款{amount}")
        return f"取款成功，当前余额为{self.balance}"


account = Account(1000)
account.deposit(500, account.transaction_history)
account.withDraw(200, account.transaction_history)
account.print_transaction_history()
print(account.balance)

account = Account(1000)
account.deposit(800, account.transaction_history)
account.withDraw(100, account.transaction_history)
account.print_transaction_history()
print(account.balance)


# 2. 可迭代购物车
# 目标**：`Cart` 内部用 `list` 存商品，实现 `__len__` / `__getitem__` / `__iter__`，
# 支持 `for` 循环、切片、`sum(cart)` 算总价。

class Cart:
    """
    购物车
    """

    def __init__(self, name: str):
        self.name = name
        self.goods: list[dict] = []

    def add(self, **goods: str):
        """
        添加商品
        :param goods: 商品
        :return:
        """
        self.goods.append(goods)
        print(f"{goods}已添加")

    def __len__(self):
        """
        获取购物车商品数量
        :return:
        """
        return len(self.goods)

    def __getitem__(self, item):
        """
        获取购物车商品
        :param item:
        :return:
        """
        return self.goods[item]

    def __iter__(self):
        """
        获取购物车商品迭代器
        :return:
        """
        for item in self.goods:
            yield item

    def __sum__(self):
        """
        获取购物车商品总价
        :return:
        """
        total = 0
        for item in self.goods:
            total += item["price"]
        return total


myCart = Cart("Zhou的购物车")
myCart.add(name="电脑", price=10000)
myCart.add(name="鼠标", price=100)
print(myCart.__dict__)
print(len(myCart))
print(myCart[0])
print(myCart.__sum__())
