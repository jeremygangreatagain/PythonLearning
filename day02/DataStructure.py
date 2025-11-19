"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
"""
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)


# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
print(a, b, c)

# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
# 您也可以为多个对象指定多个变量。例如：
a, b, c, d, e = 1, 2, 3.14, "runoob", True

# 以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。
# 可以通过 type() 函数查看变量的类型：
print(type(a))  # 输出结果为 <class 'int'>
print(type(b))  # 输出结果为 <class 'int'>
print(type(c))  # 输出结果为 <class 'float'>
print(type(d))  # 输出结果为 <class 'str'>
print(type(e))  # 输出结果为 <class 'bool'>



"""
  标准数据类型
Python3 中常见的数据类型有：

Number（数字）
String（字符串）
bool（布尔类型）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
此外还有一些高级的数据类型，如: 字节数组类型(bytes)。
"""



"""
Number（数字）
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
像大多数语言一样，数值类型的赋值和计算都是很直观的。
内置的 type() 函数可以用来查询变量所指的对象类型。

此外还可以用 isinstance 来判断：
"""
a = 111
print(isinstance(a, int)) # 输出结果为 True

"""
isinstance 和 type 的区别在于：

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""
# 注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， 
# True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(True + 1)  # 输出结果为 2
print(False + 1) # 输出结果为 1
print(True is 1)  # 输出结果为 False
print(False is 0) # 输出结果为 False

# SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
print(1 is True)
print(0 is False)
"""
什么会出现 SyntaxWarning？
Python 检测到你在用 is 比较一个字面量整数（如 1）和 True，这通常是代码错误（因为 is 比较的是身份，而不是值）。
Python 建议你使用 == 来比较值是否相等，除非你确实想检查是否是同一个对象。
在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
"""