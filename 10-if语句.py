"""
if语句分支
    1. 单分支
    格式：
        if 条件:
            语句体

    2. 双分支
    格式：
        if 条件:
            语句体1
        else:
            语句体2

    3. 多分支
    格式：
        if 条件:
            语句体1
        elif 条件：
            语句体2
        else:
            语句体3
"""
age = int(input("请输入年龄："))

if 18 <= age < 70:
    print('已成年，可以上网吧')
elif age >= 70:
    print('上了年纪眼睛看不清东西')
else:
    print('未成年，不能进入网吧')

print('-' * 20)

"""
if嵌套语句
    格式：
        if 条件1:
            条件1的语句体
            
            if 条件2:
                条件2的语句体
"""

# 示例：坐公交车，有座位时可以做下
# 要求：输入公交卡当前余额，够2元就可以坐车；如果有空位才可以坐下
price = int(input('请输入公交卡余额：'))
if price >= 2:
    print('滴，刷卡成功')
    seat = int(input('请输入可乘座位数：'))

    if seat > 0:
        print('可以坐下')
    else:
        print('没有座位了，站一会吧')
else:
    print('余额不足，请先充值公交卡')

print('-' * 20)

"""
猜拳游戏
    需求：录入玩家手势，且和 机器人手势（随机）比较，打印结果
    1：剪刀，2：石头，3：布
"""
import random

# 机器人手势
robot = random.randint(1, 3)

player = int(input('请输入你要出的手势数字：'))
if player in (1, 2, 3):
    print('机器人手势是%d' % robot)
    if (player == 1 and robot == 2) or (player == 2 and robot == 3) or (player == 3 and robot == 1):
        print('玩家获得胜利✌️')
    elif player == robot:
        print('打成平局✊')
    else:
        print('机器人胜利✋')
else:
    print('输入的手势数字超出范围')
