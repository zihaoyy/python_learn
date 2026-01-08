"""
字符串：
    在计算机底层，Python中的字符串是一段连续的内存地址，下标从0开始
字符串索引：
    Python中有 正向 和 逆向 索引之分
"""
s1 = 'helloworld'
print(s1[2])
print(s1[-1])
# 与range相同，包左不包右
print(s1[1:5:3])

print('-' * 20)
"""
切片：
    指操作的对象截取其中一部分操作，如取字符串'123456@gmail.com'中的前缀就可以使用切片。字符串、列表、元祖都支持切片
    语法：
        [起始, 结束, 步长]
    注意：
        1. 选取的区间从“起始”位开始，到“结束”位的前一位结束，步长表示选取间隔的长度
        2. 如果不写起始位，默认是0
        3. 如果不写结束位，默认到字符串末尾
        4. 如果不写步长，默认是1
        5. 如果 索引 和 步长的方向相反，获取不到数据
        6. 特殊写法：字符串[::-1]表示反转字符串
"""
name = 'abcdefg'
#  a  b  c  d  e  f  g
#  0  1  2  3  4  5  6
# -7 -6 -5 -4 -3 -2 -1
print(name[2:5:1])  # cde
print(name[2:5])  # cde
print(name[:5])  # abcde
print(name[1:])  # bcdefg
print(name[:])  # abcdefg
print(name[::2])  # aceg
print(name[:-1])  # abcdef
print(name[-4:-1])  # def
print(name[::-1])  # gfedcba

print('-' * 20)
"""
字符串查找
    .find(子串, 起始索引, 结束索引)：找子串在字符串中第1次出现的位置，如果写开始和结束索引（包左不包右），就在指定区间查找，找不到就返回-1
    .index(子串, 起始索引, 结束索引)：效果同上，找不到就报错
    .rfind(子串, 起始索引, 结束索引)：类似于find()，子串在字符串中最后一次出现的位置
    .rindex(子串, 起始索引, 结束索引)：效果同上，找不到就报错
"""
str1 = 'hello and python and java and sql and react'
print(str1.find('and'))
print(str1.find('and', 7, 30))
print(str1.find('and', 7, 19))
print('-' * 20)
print(str1.index('and'))
print(str1.index('and', 7, 30))
print(str1.index('and', 7, 19))
print('-' * 20)
print(str1.rfind('and'))
print(str1.rfind('and', 7, 30))
print(str1.rfind('and', 7, 19))
print('-' * 20)
print(str1.rfind('and'))
print(str1.rfind('and', 7, 30))
print(str1.rfind('and', 7, 19))
print('-' * 20)
print(str1.rindex('and'))
print(str1.rindex('and', 7, 30))
print(str1.rindex('and', 7, 19))
print('-' * 20)

"""
字符串修改 字符串属于“不可变类型”
    .replace(旧子串, 新子串, 替换次数)
    .split(切割符, 切割个数)
"""
# len函数
s0 = len(s1)
print(s0)

# replace函数
s1 = 'hello world and python and vue and c#'
s2 = s1.replace('and', 'or')
print(f's1: {s1}')
print(f's2: {s2}')
s3 = s1.replace('and', 'or', 2)
print(f's3: {s3}')

# split函数
s4 = s1.split(' ')
print(type(s4))
print(f's4: {s4}')
s5 = s1.split('and')
print(f's5: {s5}')
s5 = 'hello'
s6 = ','.join(s5).split(',')
print(f's6: {s6}')

print('-' * 20)

# 输入一个字符串，打印所有偶数位上的字符（下标0, 2, 4, 6... 位上的字符）
str2 = input('请输入字符串：')
str2len = len(str2)
for i in range(0, str2len, 2):
    print(str2[i])

# 给定一个文件名，判断其尾部是否以'.png'结尾
file_name = 'test1.png'
print(file_name[-4:] == '.png' and len(file_name) > 4)
