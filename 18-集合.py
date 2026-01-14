"""
集合
    set，是一个不重复无序的元素序列
    语法：
        1. {}
        2. set() 创建空集合只能使用该方式，因为第一种方式用来创建空字典
    场景：去重
"""
set1 = {10.2, 'test', False}
print(set1)

set2 = set()
print(set2)

set3 = {}
print(type(set3), set3)

list1 = [10, 20, 30, 20, 10, 30, 50]
set4 = set(list1)
list1 = list(set4)
print(list1)