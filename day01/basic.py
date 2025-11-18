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