"""
元组
    格式：
        t1 = (值1, 值2, 值3...)
        t2 = tuple()
        t3 = (值1, )
    操作：
        元组[索引] 通过下标查找元素
        .index() 查找某个数据
        .count() 统计某个数据在当前元组出现的次数
        .len() 统计元组中数据的个数
    定义：
    1. 元组可以存储多个数据但元组内的数据不可更改
    2. 元组和列表一致，也有索引概念
    3. 定义元组时，如果只有1个值，也需要在末尾添加"," 否则就是在定义一个普通的变量（非元组）
"""

t1 = (10, 20.3, False, 'test')
t2 = tuple()
t3 = (10,)

t4 = (10)

print(t1)
print(t2)
print(t3)
print(t4)
print(type(t3), type(t4))

t5 = ('a', 'b', 'c', 'd', 'e', 'f', 'c', 'e')
print(t5[1])
print(t5.index('e'))
print(t5.count('e'))
print(len(t5))
# t5[1] = 'bbc'
print(t5)

print('-' * 28)