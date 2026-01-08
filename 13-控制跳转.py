"""
    控制跳转语句：
    break
    continue
"""

# 在如下代码中填充指定内容，使其能完成 分别打印2、7、13次hello world
for i in range(1, 11):
    if i % 3 == 0:
        # break
        # continue
        print(f'hello world! {i}')

    print(f'hello world! {i}')

print('-' * 20)

# 报数字游戏：输入的学生数量为50，游戏结束后，报数的同学数量为39
# 1、键盘录入玩游戏的人数
# 2、每个学生依次报数，遇到尾数是7或7的倍数时跳过
# 3、统计报数的学生一共有多少人
count = 0
total = int(input("请输入玩游戏的人数："))
for i in range(1, total + 1):
    if i % 7 == 0 or i % 10 == 7:
        continue
    count += 1
print(f'参与游戏总人数是 {total}，报数的总人数是 {count}')

print('-' * 20)

# 猜数字游戏：
# 1、 随机生成 1个 1-100 之间的随机数，让用户猜
# 2、 如果用户猜大了或猜小了，就提示用户并继续猜
# 3、 如果猜对了，提示猜对了
import random

randomNum = random.randint(1, 100)
while True:
    guess = int(input('请输入数字：'))
    if guess < randomNum:
        print('您猜小了，请继续猜测')
        continue
    elif guess > randomNum:
        print('您猜大了，请继续猜测')
        continue
    else:
        print('恭喜您猜对了！')
        break

print('-' * 20)

"""
循环 + else 语法
    格式：
        while/for循环:
            循环体
        else:
            语句体
    执行特点：
        1. 只要循环是正常退出的，就一定会执行 else 的内容
        2. 循环正常退出，指 非break方式 跳出
"""
# 演示 for + ele 语句
for i in range(1, 11):
    if i % 3 == 0:
        # continue
        # break
        print(f'hello world {i}!')
else:
    print('我是for循环的else')

print('-' * 20)

# 打印1～100之间所有的质数，按照3个一行的方式输出
# 质数：只能被 1 和 自身 整除的数字，称为质数，也是素数，最小质数是2
# 场景1：分解版
count = 0
for i in range(2, 101):
    # 获取2-i的一半之间所有的整数，后续会和i取余
    for j in range(2, i // 2 + 1):
        # 看是否是质数
        if i % j == 0:
            break
    else:
        count += 1
        if count % 3 == 0:
            print(i, end='\n')
        else:
            print(i, end='\t')

print('-' * 20)

# 场景2：合并版，三元简化
count = 0
for i in range(2, 101):
    # 获取2-i的一半之间所有的整数，后续会和i取余
    for j in range(2, i // 2 + 1):
        # 看是否是质数
        if i % j == 0:
            break
    else:
        count += 1
        print(i, end='\n' if count % 3 == 0 else '\t')

print('-' * 20)

# 场景3：算法实现
# 规律：2～100之间的质数，只要是2，3，5，7或 不能被其中所有的整数 整除，就是质数
count = 0
for i in range(2, 101):
    if i in (2, 3, 5, 7) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        count += 1
        print(i, end='\n' if count % 3 == 0 else '\t')
