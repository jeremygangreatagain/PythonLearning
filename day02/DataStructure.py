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



# 数值运算
print(5 + 4)    # 加法 输出结果为 9
print(4.3 - 2)  # 减法 输出结果为 2.3
print(3 * 7)    # 乘法 输出结果为 21
print(2 / 4)    # 除法 输出结果为 0.5, 得到一个浮点数
print(2 // 4)   # 取整除法 输出结果为 0, 得到一个整数
print(5 % 4)    # 取模 运算符返回除法的余数 输出结果为 1
print(2 ** 4)   # 幂运算 输出结果为 16, 即 2 的 4 次方
"""
注意：
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。

Python 还支持复数，复数由实数部分和虚数部分构成，
可以用 a + bj，或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
"""
a = 1 + 2j
print(a.real)  # 输出结果为 1.0
print(a.imag)  # 输出结果为 2.0



"""
String（字符串）
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
字符串的截取的语法格式如下：
变量[头下标:尾下标]，表示从头下标开始到尾下标为止，但不包括尾下标。
注意头下标默认为 0，尾下标默认为字符串的长度。
"""

# 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数。实例如下：
str = "Runoob"  # 定义一个字符串变量

print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符(不包含倒数第一个字符)
print(str[0])       # 输出字符串的第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符(不包含第五个字符)
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
print(str + "TEST") # 打印字符串和"TEST"连接起来的结果

# Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，
# 可以在字符串前面添加一个 r，表示原始字符串：
print("Ru\noob")    # 使用反斜杠转义特殊字符 输出结果为 Ru(回车)oob
print(r"Ru\noob")   # 在字符串前面添加一个 r，表示原始字符串 输出结果为 Ru\noob

# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。
# 也可以使用 """...""" 或者 '''...''' 跨越多行。
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
word = 'Python'
print(word[0], word[5]) # 输出结果为 P n
print(word[-1], word[-6]) # 输出结果为 n P
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误。
"""
注意：
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
"""



"""
bool（布尔类型）
布尔类型即 True 或 False。
在 Python 中，True 和 False 都是关键字，表示布尔值。
布尔类型可以用来控制程序的流程，比如判断某个条件是否成立，或者在某个条件满足时执行某段代码。

布尔类型特点：
布尔类型只有两个值：True 和 False。
bool 是 int 的子类，因此布尔值可以被看作整数来使用，其中 True 等价于 1。
布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。
布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。
布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。
可以使用 bool() 函数将其他类型的值转换为布尔值。
以下值在转换为布尔值时为 False：None、False、零 (0、0.0、0j)、空序列（如 ''、()、[]）和空映射（如 {}）。
其他所有值转换为布尔值时均为 True。
"""
# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))   # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))         # False
print(bool(42))        # True
print(bool(''))        # False
print(bool('Python'))  # True
print(bool([]))        # False
print(bool([1, 2, 3])) # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 布尔比较运算
print(5 > 3)  # True
print(2 == 2) # True
print(7 < 4)  # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")
    
if not False:
    print("This will also always print")
    
x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
"""
注意: 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，
只有 0、空字符串、空列表、空元组等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。
"""



"""
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，
它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下：
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
"""
# 加号 + 是列表连接运算符，星号 * 是重复操作。如下实例：
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 定义一个列表
tinyList = [123, 'runoob']
print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3])          # 从第二个开始输出到第三个元素
print(list[2:])           # 输出从第三个元素开始的所有元素
print(tinyList * 2)       # 输出列表两次
print(list + tinyList)    # 连接列表

# 与Python字符串不一样的是，列表中的元素是可以改变的
a = [0, 1, 2, 3, 4, 5]
a[0] = 9
a[2:4] = [7, 8]
print(a)  # 输出结果为 [9, 1, 7, 8, 4, 5]
a[2:4] = []
print(a)  # 输出结果为 [9, 1, 4, 5]

"""
注意：
1、列表写在方括号之间，元素用逗号隔开。
2、和字符串一样，列表可以被索引和切片。
3、列表可以使用 + 操作符进行拼接。
4、列表中的元素是可以改变的。
Python 列表截取可以接收第三个参数，参数作用是截取的步长
"""



"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。
元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同：
"""
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinyTuple = (123, 'runoob')
print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出从第二个开始输出到第三个元素
print(tuple[2:])           # 输出从第三个元素开始后的所有元素
print(tinyTuple * 2)       # 输出元组两次
print(tuple + tinyTuple)   # 连接元组

"""
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。
也可以进行截取。
其实，可以把字符串看作一种特殊的元组。

虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
"""
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

"""
如果你想创建只有一个元素的元组，需要注意在元素后面添加一个逗号，
以区分它是一个元组而不是一个普通的值，这是因为在没有逗号的情况下，
Python会将括号解释为数学运算中的括号，而不是元组的表示。
如果不添加逗号，如下所示，它将被解释为一个普通的值而不是元组：
"""
not_a_tuple = (42)
"""
这样的话，not_a_tuple 将是整数类型而不是元组类型。

string、list 和 tuple 都属于 sequence（序列）。

注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用 + 操作符进行拼接。
"""



"""
Set（集合）
Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
另外，也可以使用 set() 函数创建集合。

注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
"""
sites = {'Google', 'Taobao', 'Runoob', 'Facebook' ,'Zhihu' ,'Baidu'}
print(sites)   # 输出集合，输出顺序可能不一样，重复的元素会被自动去掉
# 成员测试
if 'Runoob' in sites:
  print('Runoob 在集合中')
else:
  print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)               # 输出结果为 {'a', 'b', 'c', 'd', 'r'}
print(a - b)           # a和b的差集 输出结果为 {'r', 'd', 'b'}
print(a | b)           # a和b的并集 输出结果为 {'a', 'b', 'c', 'd', 'r', 'l', 'm', 'z'}
print(a & b)           # a和b的交集 输出结果为 {'a', 'c'}
print(a ^ b)           # a和b中不同时存在的元素 输出结果为 {'r', 'd', 'b', 'l', 'm', 'z'}



"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinyDict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])          # 输出键为 2 的值
print(tinyDict)         # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values()) # 输出所有值



"""
bytes 类型
在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）。
与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。
bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。
在网络编程中，也经常使用 bytes 类型来传输二进制数据。

创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：
此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，
第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
x = bytes("hello", encoding="utf-8")

与字符串类型类似，bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等。
同时，由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象。例如：
"""
x = b"hello"
y = x[1:3]  # 切片，得到 b"el"
z = x + b"world"  # 拼接，得到 b"helloworld"
# 需要注意的是，bytes类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值，例如：
x = b"hello"
if x[0] == ord("h"):
  print("第一个字符是 h")
# 其中 ord() 函数用于将字符转换为相应的整数值。

# Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，
# 你只需要将数据类型作为函数名即可