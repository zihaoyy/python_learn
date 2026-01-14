"""
容器类型-公共运算符
    容器类型：
        字符串 str
        列表 list
        元组 tuple
        字典 dict
        集合 set

    运算符       描述          支持的容器类型
    +           合并          字符串、列表、元组
    *           复制          字符串、列表、元组
    in          是否存在       字符串、列表、元组、字典
    not in      是否不存在     字符串、列表、元组、字典
"""

# 1. +
print('aa' + 'bb')
print([1, 2, 3] + [4, 5, 6] + ['a', 'b'])
print((1, 2, 3) + (4, 5, 6))

# 集合元素具有唯一性，+不支持集合，合并可能存在重复元素，然后会自动删除重复的，无意义
# print({1, 2, 3} + {4, 5, 6})

# 键具有唯一性，+不支持字典
# print({'name': '张三'} + {'age': 23})

# 2. *
print('-' * 28)
print([1, 2, 3] * 2)
print((1, 2, 3) * 2)

# 集合具有唯一性，*不能作用于集合
# print({1, 2, 3} * 2)

# 键具有唯一性，*不支持字典
# print({'name': '张三'} * 2)

print('-' * 28)

# 3. in
print('a' in 'abc')
print(10 in [10, 20, 30])
print(10 in (10, 20, 30))
# 字典只能判断是否包含该键，不能判断是否包含值
print('name' in {'name': '张三', 'age': 23})
print(23 in {'name': '张三', 'age': 23})

print('-' * 28)

# 4. not in
print('a' not in 'abc')
print(10 not in [10, 20, 30])
print(10 not in (10, 20, 30))
# 字典只能判断是否包含该键，不能判断是否包含值
print('name' not in {'name': '张三', 'age': 23})
print(23 not in {'name': '张三', 'age': 23})
