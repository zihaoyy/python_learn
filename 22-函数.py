"""
函数
    格式：
        def 函数名(形参1, 形参2...):
            函数体
            return 返回值
"""


# 模拟基站工作流程， 给 Tim 打电话
def call(name):
    print('----- 拨号 -----')
    print('拨号方手机 发送信号包 到就近的基站')
    print(f'拨号方就近基站 解析信号包，找到 {name}就近的基站')
    print(f'两个基站之间通过 底下电缆的形式 传输信号包')
    print(f'{name}就近的基站 发送信号包到 {name}手机')
    print('----- 忙音等待，嘟嘟嘟 -----')
    return


call('Tim')

print('-' * 28)

"""
函数说明文档
"""


def print_info(name):
    """
    打印信息
    :param name: 名称
    :return: 无
    """
    print(name)
    return


print_info('Tim')

print('-' * 28)


# 定义get_sum函数，计算两个整数和，返回这个函数
def get_sum(a, b):
    """
    计算两个整数和，并返回计算结果
    :param a: 第一个整数
    :param b: 第二个整数
    :return: 两个整数的和
    """
    return a + b


print(get_sum(1, 2))
