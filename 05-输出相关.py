"""
输出相关
    函数：
        print()，将()中的内容输出到控制台
    分类：
        1. 输出单个值
        2. 同时输出多个值
        3. 换行输出 和 不换行输出
        4. 格式化输出 -> 占位符
        5. 格式化输出 -> 差值表达式
"""
name = '威震天'
age = 40
salary = 1000.122
flag = True

# 演示 1. 输出单个值
print('name：' + name)
print(age)

# 演示 2. 同时输出多个值
print(name, age, salary, flag)

# 演示 3. 换行输出 和 不换行输出
# 换行输出
print('hello\nworld')

# 不换行输出
print('你好')
print('世界')
print('hello', end=' ')
print('world')
# 上述代码完整写法：print('hello', end='\n')，为print函数默认添加内容

# 演示 4. 格式化输出 -> 占位符
name = '张三'
age = 20
print('我的姓名是%s，年龄是%d' % (name, age))
# 常用格式符号：%s字符串、%d整形、%f浮点型

# 练习
name = '小明'
student_no = 1
price = 9.00
weight = 5.00
money = 45.00
print('我的名字叫%s，请多多关照！' % name)
print('我的学号是%06d' % student_no)
print('苹果总价%.2f元/斤，购买了%.2f斤，需要支付%.2f元' % (price, weight, money))

# 占位符特殊写法  %05d -> 期望得到5位数的整数，不够前面补0   %.2f -> 保留两位小数，四舍五入

# 特殊写法 两个% -> 一般用于显示比例
print('xx占比%.2f%%，成绩排名全班3%%' % price)


# 演示 5. 格式化输出 -> 差值表达式
# 格式：print(f'content {var}')
print(f'我叫{name}，工号是{student_no:06d}，工资{salary:.2f}')
