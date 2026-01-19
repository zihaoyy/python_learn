"""
推导式
    comprehensions（解析式），是Python的一种独有特性。
    可以从一个数据序列构建另一个新的数据序列（一个有规律的列表或控制一个有规律列表）的结构体
    共有3种推导：
        列表推导式
        集合推导式
        字典推导式
    格式：
        变量名 = [变量名 for ... in ... if 判断条件]
        变量名 = {变量名 for ... in ... if 判断条件}
        变量名 = (变量名1:变量名2 for ... in ... if 判断条件)
"""

"""
列表推导式
"""
# 创建1个0~9的列表
# 方式1 不使用推导式
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# 方式2 列表推导式
list2 = [i for i in range(10)]
print(list2)

# 方式3
list3 = list(range(10))
print(list3)

print('-' * 28)

# 创建1个0~9的偶数列表
# 方式1 不使用推导式
list1 = []
for i in range(10):
    if i % 2 == 0:
        list1.append(i)
print(list1)

# 方式2 列表推导式
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)

# 方式3
list3 = list(range(0, 10, 2))
print(list3)

print('-' * 28)

# 创建列表：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]，循环嵌套，i的值1,2 j的值0,1,2
# 方式1 循环嵌套
list1 = []
for i in range(1, 3):
    for j in range(3):
        # print((i, j))
        list1.append((i, j))
print(list1)

# 方式2 列表推导式
list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

print('-' * 28)

"""
集合推导式
"""
# 生成0～9的偶数列表
set1 = {i for i in range(10) if i % 2 == 0}
print(set1)

# 创建一个集合，数据为下方列表的2次方
list1 = [1, 1, 2]
set2 = {i ** 2 for i in list1}
print(set2)

print('-' * 28)

"""
字典推导式
"""
# 创建1个字典，key是1～5的数字，value是该数字的2次方，如{1:2, 2:4, 3:9, 4:16, 5:25}
dict1 = {i: i ** 2 for i in range(1, 6)}
print(dict1)

# 把下面两个列表拼接成1个字典，两个列表的元素长度要一致
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'male']

dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)
