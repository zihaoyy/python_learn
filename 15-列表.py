"""
列表
    属于容器的一种，属于可变类型，可以同时存储多个元素
    语法：
        列表名 = [值1, 值2, 值3...]
        列表名 = list()
元组：()
字典：{键值对}
集合：{单值, 单值...}
"""
list1 = [10, 20.3, True, 'hello']
list2 = list()
list3 = []

print(list1)
print(list2)

print(type(list2))

print(list2 == list3)

print(list1[1], list1[-3])

print('-' * 20)

"""
列表遍历
"""
name_list = ['zhangsan', 'lisi', 'wangwu']
# for循环遍历
for name in name_list:
    print(name)

# while循环遍历
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

# for循环索引遍历
for name in range(len(name_list)):
    print(name_list[name])

print('-' * 20)

"""
列表操作
    增
        .append() 增加指定数据到列表中
        .extend() 列表末尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
        .insert(下标, 数据)
    删
        del 列表名[下标]
        .pop(下标) 默认删除最后一个，返回该数据
        .remove()
        .clear() 清空列表，返回空列表
    改
        列表名[下标] = 值
    查
        in
        not in
        index
        count
    排序
        sort
        .reverse(reverse=True) False升序 True降序
"""
list1 = []
# 增
list1.append(10)
list1.extend('hello')
list1.extend(['hello', 'world'])
list1.insert(1, 'orange')

# 删
del list1[1]
list1.pop(2)
# list1.clear()

# 改
list1[1] = 'react'

# 查
print(list1.index('world'))
# print(list1.index('world', 1, 4))
print(list1.count('l'))
print(10 in list1)
print('hello' not in list1)
print(list1)

# 排序
list1.sort(reverse=True)

# 反转
list1.reverse()

print('-' * 20)

# 统计大串中小串出现的次数
max_str = 'woaibeijing,buguannanjinghaishibeijing,laidaojiushihaodifangbeijing'
min_str = 'beijing'

# 思路一 count
result = max_str.count(min_str)
print(result)

# 思路二 split切割+统计个数
result = max_str.split(min_str)
print(len(result) - 1)

# 思路三 替换
new_str = max_str.replace(min_str, '')
result = (len(max_str) - len(new_str)) // len(min_str)
print(result)

# 思路四 find + 切片
result = max_str.find(min_str)
print(result - 1)