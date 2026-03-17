"""
函数
    格式：
        def 函数名(形参1, 形参2...):
            函数体
            return 返回值
"""


# 模拟基站工作流程， 给 Tim 打电话
def call(name):
    print("----- 拨号 -----")
    print("拨号方手机 发送信号包 到就近的基站")
    print(f"拨号方就近基站 解析信号包，找到 {name}就近的基站")
    print(f"两个基站之间通过 底下电缆的形式 传输信号包")
    print(f"{name}就近的基站 发送信号包到 {name}手机")
    print("----- 忙音等待，嘟嘟嘟 -----")
    return


call("Tim")

print("-" * 28)

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


print_info("Tim")

print("-" * 28)


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
print("-" * 28)


# 返回多个参数
def calculate(int1, int2):
    sum = int1 + int2
    sub = int1 - int2
    mul = int1 * int2
    div = int1 / int2
    return [sum, sub, mul, div]


print(calculate(1, 2))
print("-" * 28)


# 关键字参数
def user_info(name, age, gender):
    print(f"name: {name}, age: {age}, gender: {gender}")


user_info(name="Tim", age=20, gender="male")
user_info(gender="male", name="Tim", age=20)
user_info(age=20, gender="male", name="Tim")
print("-" * 28)


# 缺省参数
def user_info(name, age, gender="male"):
    print(f"name: {name}, age: {age}, gender: {gender}")
    return


user_info("Tim", 20)
user_info("Tim", 20, "female")
print("-" * 28)


# 不定长参数，*args 接收的是一个元组，**kwargs 接收的是一个字典
def user_info(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    return


user_info("Tim", 20, "male", name="Tim", age=20, gender="male")
print("-" * 28)


# 案例：get_sum，分别计算求 任意个整数和，如2个整数和、3个整数和、4个...
def get_sum2(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


get_sum2(1, 2)
get_sum2(1, 2, 3)
get_sum2(1, 2, 3, 4)
print("-" * 28)

"""
组包
"""
list1 = [1, 2, 3, 4, 5]
tuple1 = ("aa", "bb", "cc")
dict1 = {"name": "Tim", "age": 20, "gender": "male"}

"""
拆包
"""
# 列表拆包
a, b, c, d, e = list1
print(a, b, c, d, e)
print("-" * 28)

# 元组拆包
str1, str2, str3 = tuple1
print(str1, str2, str3)
print("-" * 28)

# 字典拆包，只能获取'键'的值
name, age, gender = dict1
print(name, age, gender)
print("-" * 28)
