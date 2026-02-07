'''
条件语句与分支语句
'''

'''
1~100以内的素数
'''
for num in range(1, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。
游戏结束的条件是玩家破产（输光所有的赌注）。
Version 1.0
Author Chou
'''
print('-' * 10, '花旗骰', '-' * 10)
import random

totalMoney = 1000
while totalMoney > 0:
    print(f'目前有 {totalMoney} 元')
    bet = int(input('请下注: '))
    if 0 > bet:
        print('请下注！')
        break
    # 生成两个骰子的随机数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    if first_point == 7 or first_point == 11:
        print("恭喜你，玩家赢了！")
        totalMoney += bet
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print("运气太差了，庄家赚了！")
        totalMoney -= bet
    else:
        print("对赌继续....")
        while True:
            second_point = random.randrange(1, 7) + random.randrange(1, 7)
            if second_point == 7:
                print("运气太差了，庄家赚了！")
                totalMoney -= bet
                break
            elif second_point == first_point:
                print("恭喜你，玩家赢了！")
                totalMoney += bet
                break
            else:
                print(f"还剩{totalMoney}对赌继续吗？")
print(f'游戏结束，你的资产为 {totalMoney}')

'''
游戏需求：
掷骰子
两个骰子分为： 1-6
1.掷骰子需要有金币，没有金币不能玩游戏
2.获取金币方式：玩一局游戏赠送一枚金币，可以充值金币
    最低充值10金币，且充值的金币必须是10 的倍数。充五元赠送10个金币
3. 玩一局消耗5金币
4.输赢规则：
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    猜大小：猜2~6 为小，8~12为大，猜中7 继续。猜对奖励6枚金币，猜错没有奖励
    
5.游戏结束: 1.主动退出，2.没有金币退出
'''
print('-' * 20, '开始猜大小游戏', '-' * 20)
_game_gold = 0
count_join = 0
while True:
    print('-'*20, f'你已经参与了{count_join}局游戏，当前金币余额为：{_game_gold}', '-'*20)
    if _game_gold < 5:
        print('金币不足，请充值！')
        while True:
            is_continue_charge = False
            print('请选择需要充值的金额：1:10元 2:20元 3:50元 4:100元 5:200元 6:500元\n\t')
            if not is_continue_charge:
                _charge_gold = int(input('请选择需要充值的金额序号：'))
                if _charge_gold == 1:
                    _game_gold += 10
                elif _charge_gold == 2:
                    _game_gold += 20
                elif _charge_gold == 3:
                    _game_gold += 50
                elif _charge_gold == 4:
                    _game_gold += 100
                elif _charge_gold == 5:
                    _game_gold += 200
                elif _charge_gold == 6:
                    _game_gold += 500
                else:
                    print('请选择正确的金额!')
                print(f'充值成功，当前金币为{_game_gold},是否继续充值？y/n')
            toBeContinue = input('请选择：')
            if toBeContinue == 'y':
                is_continue_charge = True
                continue
            else:
                print(f'你当前的游戏金币余额为：{_game_gold},可以愉快的玩耍啦~')
                break
    print("选择小请输入：1，选择大请输入：2，退出游戏：0")
    player_number = int(input('请输入：'))
    if player_number == 1:
        print('你选择了小')
    elif player_number == 2:
        print('你选择了大')
    else:
        print(f'游戏结束，你当前的金币余额为：{_game_gold}')
        break
    one_point = random.randrange(1, 7) + random.randrange(1, 7)
    if one_point == 2 or one_point == 3 or one_point == 4 or one_point == 5 or one_point == 6:
        print(f'掷出了{one_point}，点数为小')
        if player_number == 1:
            _game_gold += 6
            print(f'恭喜你猜对了，奖励六枚金币，当前金币余额为：{_game_gold}')
        else:
            print('很遗憾你猜错了')
            _game_gold -= 5
    elif one_point == 7:
        print(f'掷出了{one_point}，游戏机继续')
    else:
        print(f'掷出了{one_point}，点数为大')
        if player_number == 2:
            _game_gold += 6
            print(f'恭喜你猜对了，奖励六枚金币，当前金币余额为：{_game_gold}')
        else:
            print('很遗憾你猜错了')
            _game_gold -= 5
    _game_gold += 1
    print(f'参与一局游戏+1金币，你当前的金币余额为：{_game_gold}')
    count_join += 1
