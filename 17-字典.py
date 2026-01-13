"""
字典
    定义：
    1. 括号为大括号（花括号）
    2. 数据为键值对形式出现
    3. 各个键值对之间用逗号隔开
    4. 属于可变类型

    语法：
    有数据字典：
        dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
    空字典：
        dict2 = {}
        dict3 = dict()

    操作：
        增：
            字典序列[key] = value 如果存在就修改该值，否则新增
        删：
            del 字典名
            .del()
            .clear()
        查：
            字典名['key'] key存在，返回值，不存在则报错
            .get(key, 默认值) 根据字典的key获取对应的value，不存在就返回第二个参数（默认值），如果省略第二个参数，则返回None
            .keys() 以列表返回一个字典所有的键
            .values() 以列表返回字典中的所有值
            .items() 以列表返回可遍历的（键, 值）元组数组
"""
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}
print(dict1)
print(type(dict1))

print('-' * 28)

# 增
dict1['school'] = 'Tinghua'
print(dict1)

# 删
del dict1['name']
print(dict1)

# 清空
# dict1.clear()
# print(dict1)

# 改
dict1['name'] = 'Alex'
print(dict1)

# 查
print(dict1['age'])
print(dict1.get('name'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print('-' * 28)

"""
字典遍历
    1. 根据 键 获取其对应的值
    2. 根据 键值对 获取其对应的 键 和 值
"""
dict1 = {'乔峰': '阿朱', '虚竹': '梦姑', '杨过': '小龙女', '郭靖': '黄蓉'}

# 1.根据 键 获取其对应的值
for key in dict1.keys():
    print(f'{key} <=> {dict1.get(key)}')

print('-' * 28)

# 2. 根据 键值对 获取其对应的 键 和 值
for item in dict1.items():
    print(f'{item[0]} <=> {item[1]}')

print('-' * 28)

# 3. 拆包
for k, v in dict1.items():
    print(f'{k} <=> {v}')
