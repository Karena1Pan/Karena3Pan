# Filename: test.py

# 导入模块
import trypython_support

# 现在可以调用模块里包含的函数了
trypython_support.print_func("this is my python module!")

'''
import trypython_fibonacci

trypython_fibonacci.fib(1000)
print(trypython_fibonacci.fib2(100))

'''
# //////////////////////////////
'''
# from...import语句
from trypython_fibonacci import fib
fib(1000)
'''

'''
# from...import*语句
# 把一个模块的所有内容全部导入到当前的命名空间中
# 格式为 from modname import*
'''

# //////////////////////////////
# from...import...as语句
from trypython_fibonacci import fib as fibfunc
fibfunc(1000)

'''
import trypython_fibonacci
print(dir(trypython_fibonacci))  # dir（）可以找到模块定义的所有名称。以一个字符串列表的形式返回
'''
print(dir())  # dir()没有给参数的时候，会罗列出当前定义的所有名称

#模块其它的用法可以查看:1、包 2、从一个包中导入*

