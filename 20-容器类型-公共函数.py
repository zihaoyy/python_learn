"""
容器类型-公共函数
    len()  计算容器中元素个数
    del / del()    删除
    max()  返回容器中元素的最大值
    min()  返回容器中元素的最小值
    range(start, end, step)    生成从start到end的数字，步长是step，供for循环使用
    enumerate()    讲一个可遍历的数据对象（列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环中
"""
list1 = [10, 50, 20, 30, 66, 22]

# len()
print(len(list1))

# del、del()
del list1[1]
del (list1[1])
print(f'删除后的list1: {list1}')

# max()
print(f'最大值：{max(list1)}')

# min()
print(f'最小值：{min(list1)}')

# range()
print(f'range生成数据：{range(1, 5, 2)}')
print(f'range生成数据（类型转换）：{list(range(1, 5, 2))}')

# enumerate()
print(f'list1: {enumerate(list1)}')  # <enumerate object at 0x105d20180>， 0x指地址值（16进制）
for i in enumerate(list1):
    print(i)  # 格式：(下标, 元素值)，且下标从0开始

print('-' * 28)

for i in enumerate(list1, 5):
    print(i) # 下标从5开始
