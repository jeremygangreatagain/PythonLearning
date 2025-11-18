# 标识符
# 第一个字符必须以字母（a-z, A-Z）或下划线 _ 。
# 标识符的其他的部分由字母、数字和下划线组成。
# 标识符对大小写敏感，count 和 Count 是不同的标识符。
# 标识符对长度无硬性限制，但建议保持简洁（一般不超过 20 个字符）。
# 禁止使用保留关键字，如 if、for、class 等不能作为标识符。

# 合法的标识符示例
age = 25
user_name = "Alice"
_total = 100
MAX_SIZE = 1024
# calculate_area()
# StudentInfo
# __private_var



# 非法的标识符示例（注释掉以避免语法错误）
# 2nd_place = "silver"    # 错误：以数字开头
# user-name = "Bob"       # 错误：包含连字符
# class = "Math"          # 错误：使用关键字
# $price = 9.99          # 错误：包含特殊字符
# for = "loop"           # 错误：使用关键字



# Python3 支持 Unicode 标识符，这意味着可以使用非 ASCII 字符作为标识符的一部分。
姓名 = "张三"  # 合法
π = 3.14159   # 合法



# 验证标识符合法性的简单函数
def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

print(is_valid_identifier("2var"))  # False
print(is_valid_identifier("var2"))  # True

# Python中单行注释以 # 为开头，多行注释可以使用三个单引号 ''' 或三个双引号 """ 包围注释内容。
# 第一个注释
print("Hello, World!")  # 输出问候语
'''
这是一个多行注释的示例
可以包含多行文字
'''
print("多行注释示例结束1")
"""
这是另一个多行注释的示例
也可以包含多行文字
"""
print("多行注释示例结束2")


""" 
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下： 
"""
if True:
    print("True")
else:
    print("False")

# 以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#   print ("False")    # 缩进不一致，会导致运行错误
# ↑取消缩进量与以前的缩进不匹配Pylance



'''
多行语句
Python 通常是一行写完一条语句，但如果语句很长，
我们可以使用反斜杠 \ 来实现多行语句，例如：
'''
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total) # 输出为 6

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ["item_one", "item_two", "item_three", 
        "item_four", "item_five"]
print(total) # 输出为 ['item_one', 'item_two', 'item_three', 'item_four', 'item_five']



"""
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数) - 复数由实部和虚部组成，
形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j
"""



"""转义符 \。
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
"""
str='123456789'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）（包头不包尾）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# 这里的 r 指 raw，即 raw string，会自动将反斜杠转义，例如：
print('\n')       # 输出空行
print(r'\n')      # 输出 \n



# 空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。
# 类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是 Python 语法的一部分。
# 书写时不插入空行，Python 解释器运行也不会出错。
# 但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。

# 等待用户输入
# 执行下面的程序在按回车键后就会等待用户输入：
input("\n\n按下回车键结束程序...")
# 以上代码中 ，\n\n 在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。


"""
多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，
该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
如下实例：
"""
# if expression : 
#   suite
# elif expression : 
#   suite 
# else : 
#   suite



"""
print 输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
"""
print("hello world")
print("hello world", end="")



"""
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""