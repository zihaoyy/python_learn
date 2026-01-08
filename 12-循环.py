"""
循环
    while循环
    for循环
"""

# 打印5次 HelloWorld
i = 1
while i <= 5:
    print(f'HelloWorld: {i}')
    i += 1

# 计算1-100的累加和（包含1、100）
i = 0
sums = 0
while i <= 100:
    sums += i
    i += 1

print(sums)

# 计算1-100的偶数和
i = 0
sums = 0
while i <= 100:
    if i % 2 == 0:  # 奇数和改为 == 1
        sums += i
    i += 1
print(sums)

print('-' * 20)

"""
水仙花数：
    1. 是一个三位数
    2. 每位数的立方和相加 = 本身
    如： 153 = 1+1+1 * 5+5+5 * 3+3+3
"""
# 打印所有的水仙花数
# 定义初始值100
i = 100
# while循环，获取到100 - 1000之间所有的值
while i < 1000:
    # 获取该数字的各个位数数字
    ge = i // 1 % 10
    shi = i // 10 % 10
    bai = i // 100 % 10

    # 判断是否是水仙花数，打印
    if ge * ge * ge + shi * shi * shi + bai * bai * bai == i:
        print(i)
    i += 1

# 统计水仙花数的个数并打印结果
i = 100
count = 0
# while循环，获取到100 - 1000之间所有的值
while i < 1000:
    # 获取该数字的各个位数数字
    ge = i // 1 % 10
    shi = i // 10 % 10
    bai = i // 100 % 10

    # 判断是否是水仙花数，打印
    if ge * ge * ge + shi * shi * shi + bai * bai * bai == i:
        count += 1
    i += 1
print(f'水仙花的个数是{count}')

print('-' * 20)

"""
循环嵌套
    格式：
    while 条件:
        执行体
        while 条件:
            执行体
"""

# 打印5行5列的矩形
x, y = 0, 0
while x < 5:
    while y < 5:
        print('*', end='')
        y += 1
    print()
    x += 1
    y = 0

print('-' * 20)

# 打印正三角形
x = 1
while x <= 5:
    y = 1
    while y <= x:
        print('*', end='')
        y += 1
    print()
    x += 1

print('-' * 20)

# 打印倒三角形
x = 5
while x >= 1:
    y = 1
    while y <= x:
        print('*', end='')
        y += 1
    print()
    x -= 1

print('-' * 20)

# 打印99乘法表
x = 1
while x < 10:
    y = 1
    while y <= x:
        print(f'{y} * {x} = {x * y}', end='\t')
        y += 1
    print()
    x += 1
