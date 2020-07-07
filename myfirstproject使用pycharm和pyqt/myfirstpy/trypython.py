import math
import numpy
import sys
import keyword

print("///////////////////////////////////////////////////////")


def add(x, y, f):
    return f(x) + f(y)


print(add(25, 9, math.sqrt))


def bar():
    print("int the bar..")


def foo(func):
    func()
    print("in the foo..")


foo(bar)

print("///////////////////////////////////////////////////////")

print("math.sqrt(100) : ", math.sqrt(100))
print("math.sqrt(7) : ", math.sqrt(7))
print("math.sqrt(math.pi) : ", math.sqrt(math.pi))

str = "the length of (%s) is %d" % ('runoob', len('runoob'))
print(str)


class Person():
    pass


xiaoming = Person()
xiaohong = Person()

xiaoming.name = "xiaoming"
xiaoming.age = 24
xiaoming.sex = "man"

xiaohong.name = "xiaohong"
xiaohong.age = 22
xiaohong.sex = "woman"

print(sys.getsizeof(xiaohong))

print("///////////////////////////////////////////////////////")


class Person1(object):
    address = "earth planet"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


xiaoming1 = Person1("xiaoming", 24, "man")
print(sys.getsizeof(xiaoming))
print(xiaoming1.age, xiaoming1.name, xiaoming1.sex)
xiaohong1 = Person1("xiaohong", 22, "women")

print(xiaoming1.address)
print(xiaohong1.address)

print("///////////////////////////////////////////////////////")


class Person2(object):
    address = "earth planet"
    count = 0

    def __init__(self, name=" ", age=0, sex=" "):
        self.name = name
        self.age = age
        self.sex = sex
        Person2.count += 1


xiaoming2 = Person2("xiaoming", 24, "man")
print(Person2.count)

xiaohong2 = Person2()
print(Person2.count)

print(xiaoming2.address)
print(xiaohong2.address)

xiaohong2.address = "mar"

print(xiaoming2.address)
print(xiaohong2.address)

print("///////////////////////////////////////////////////////")


class Person3(object):
    def __init__(self, name=" "):
        self.__name = name

    def get_name(self):
        return self.__name


xiaoming3 = Person3("xiaoming")
print(xiaoming3.get_name())

print("///////////////////////////////////////////////////////")


class Person4(object):
    count = 0

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name=" "):
        self.__name = name
        Person4.count = Person4.count + 1

    def get_name(self):
        return self.__name


# 通过标记一个@classmethod,将相应的方法绑定到Person4类上，而非类的实列上
# 这时类方法无法获得任何实例变量，只能获得类的引用
print(Person4.how_many())
xiaoming3 = Person3("xiaoming")
print(Person4.how_many())

print("///////////////////////////////////////////////////////")


# 类方法时通过类来直接调用的，或者通过实例直接来调用
class ClassA(object):
    @classmethod
    def func_a(cls):
        print(type(cls), cls)


if __name__ == '__main__':
    ClassA.func_a()
    ca = ClassA()  # 类实列
    ca.func_a()

print("///////////////////////////////////////////////////////")
# python 关键字
# import keyword
print(keyword.kwlist)  # 输出当前版本的所有关键字

# python 多行语句，用\链接
total = "my teacher" + \
        "is you"
print(total)

# python 多行字符,用三引号描述，可以是""",也可以是"'
sentence = """这是一个多行语句，
由多行组成，
你可以观察下它的特点"""
print(sentence)

# python 运算符,**=,幂赋值运算符，//=，取整除赋值运算符
c = 10
a = 4
c **= a
print("c的a次方，c的值为：", c)

c = 10
a = 4
c //= a
print("c的a次方，c的值为：", c)

# python 成员运算符，in 和 not in
# python中is is not,身份运算符，in not in， 成员运算符， not or and， 逻辑运算符
# python中complex(x, y),将x，y转换成一个复数，complex(x)，将x转换成一个复数
x = 6
y = 7
print(complex(x, y))

# python 基本运算符
x = 10
y = 3
print(divmod(x, y))  # x 除以 y 的除数和余数
print(pow(x, y))
print(x ** y)

print("///////////////////////////////////////////////////////")
# python 字符串
a = "Hello"
b = "Python"
print(a + b)
print(a * 2)
print(a[1])
print(a[1:4])
print('H' in a)
print('l' in a)
print('M' not in a)
print(r'\n')  # r放在字符串前，表示按照字面意思打印，而不是转义字符

print("///////////////////////////////////////////////////////")
# python 列表
# 列表
list0 = []
list1 = ['py40', True, 100]
list2 = [6, 4, 10, 3, 1, -6, 100]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# 列表元素修改
list1 = ['py40', True, 100]
list1[1] = "gengxin"
print(list1)

list1[1] = False
print(list1)

# 列表元素新增与删除

list1.append('d')
print(list1)
del list1[2]
print("delete the third element", list1)

# 遍历列表元素
print("//////////////")
for x in list1:
    print(x)

print("//////////////")
# 其它列表方法可问度娘 Python列表函数和方法

print("///////////////////////////////////////////////////////")
# python 元组

# 创建元组
tup1 = ('hello', 'py40', 0, 10000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup4 = ()  # 创建空元组
tup5 = (50,)  # 元组中只包含一个元素时，需要在元素后面添加逗号

# 访问元组
tup1 = ('hello', 'py40', 0, 10000)
print(tup1[0])

# 元组元素不允许被修改，只能通过链接元组来实现
tup2 = (1,)
tup3 = tup1 + tup2
print(tup3)

tup1 = ('hello', 'py40', 0, 10000)
tup1 = (tup1, '05')
print(tup1)

# 元组的元素不能被删除，但可以删除整个元组
tup2 = (1,)
del tup2
print("///")
# 语句print(tup2)会报错，删除的元组已经不存在了

# 判断元组是否存在
tup1 = ('hello', 'py40', 0, 10000)
print(1 in tup1)

# 元组遍历
print("///")
tup1 = ('hello', 'py40', 0, 10000)
for x in tup1:
    print(x)
print("///")

# 元组内置方法：len(tuple),计算元组个数，max(tuple),返回元组中元素最大值，min(tuple),返回元组中元素最小值，tuple(seq)，将列表转换成元组
tup1 = (6, 1, 0, 10000)
print(len(tup1))
print(max(tup1))
print(min(tup1))
list1 = ['py40', True, 100]
print(list1)
print(tuple(list1))

print("///////////////////////////////////////////////////////")
# python 集合
# 注：把不同的元素组成一起形成集合，集合无序，元素唯一
# 创建集合
s = set("beginman'")
t = frozenset("ythonman")  # 创建冻结的集合，冻结后集合不能添加或删除任何元素
print(s, "\n", t)

print(type(s), type(t))

print(len(s), len(t))

print(s == t)
s = t
print(s == t)

# 集合可通过函数实现相应的操作，可以查看集合中的方法，使用相关方法。

# 集合的遍历
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
for d in weekdays:
    print(d)

print("///////////////////////////////////////////////////////")
# python字典

# 字典是一种可变容器模型，且可存储任意类型对象
# 字典的每个键值（key => value）对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包含在花括号({})中。
# 格式为 d = { key1 : value1， key2 : value2 }

dict1 = {"name": "Zhangguoli", "city": "beijing"}
print(dict1["name"])
dict1["name"] = "cyrus"
print(dict1)
# 字典增加元素
dict1["age"] = 36
print(dict1)
# 字典删除元素
del dict1["name"]  # 删除键"name"
print(dict1)
dict1.clear()  # 清除字典数据
print(dict1)
# del dict1  # 删除字典

# 字典元素遍历
print("/////")
dict2 = {"name": "Zhangguoli", "city": "beijing"}
# 方法一
for (d, x) in dict2.items():
    print("key:" + d + ", value:" + x)
# 方法二
for d, x in dict2.items():
    print("key:" + d + ", value:" + x)

dict0 = {"Alice": 89, "Beth": 95, "Cecil": 78}
print(dict0)
for d, x in dict0.items():
    print("key:" + d + ", value:", x)
print("/////")
# 可查阅字典的内置函数和方法
print("Alice" in dict0)
print("Cyrus" in dict0)

t = dict0.items()  # 以列表返回可遍历的（键，值）元组数组
print(t)
t = dict0.keys()  # 以列表返回一个字典所有的键
print(t)

print("/////")
print(dict0)
t = dict0.update(dict2)  # 把字典dict2的键/值对更新到dict0中，此处返回none，主要因为update方法没有返回值
print(dict0)
dict3 = {"Alice": 95, "Beth": 100, "Cecil": 60}
t = dict0.update(dict3)
print(dict0)
print("/////")

print("///////////////////////////////////////////////////////")
# python条件语句

x = 3
if x > 3:
    print("x>3")
elif x == 3:
    print("x=3")
else:
    print("都不是")

# python循环语句与C++类似，此处不总结了

# range的使用
# range()为内置函数，可以生成数列，步长可是正值，也可以是负值，类似matlab语言
for i in range(6):
    print(i)
for i in range(0, 10, 3):
    print(i)
for i in range(-10, -100, -30):
    print(i)

# break和continue的使用和c++一样
print("/////")
for letter in 'py40.com':  # 第一个实例
    if letter == '0':
        break
    print('letter-> :', letter)
else:
    print("break跳出后，else语句不会继续执行")

var = 5  # 第二个实例
while var > 0:
    var -= 1
    if var == 3:
        print("#continue跳过当前循环,执行下次循环")
        continue
    print('var->:', var)
else:
    print("while条件不满足，会执行else语句...")
print("Good bye!")
print("/////")

# pass语句
# pass是空语句，使用pass仅仅是为了保持结构的完整性
for letter in 'py40.com':
    if letter == '0':
        pass
        print("执行 pass 块")
    print('当前字母 :', letter)

print("///////////////////////////////////////////////////////")


# python函数
# 函数定义的格式与其它语言类似，均以函数名和参数进行限制
# python中调用函数时可以用的参数类型有：必须参数，关键字参数，默认参数，不定长参数

# 必须参数

# "打印任何传入的字符串"
def printme(str):
    print(str)
    return

# 调用printme函数
printme("mytime")

# 关键字参数
printme(str="thi is function call")


# 默认参数
def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo
printinfo(age=50, name="cyrus")
print("————————")
printinfo(name="cyrus")

# 不定长参数
# 主要用于处理比声明时更多的参数的情况，不定长参数声明时不会命名

# 定义格式如下
'''
def functionname(formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''


# 加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
# 实列如下：

def myprintinfo(arg1, *vartuple):
    # 打印任何传入的参数
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用myprintinfo 函数
myprintinfo(10)
myprintinfo(70, 60, 50)

# 匿名函数
# python 用lambda来创建匿名函数，格式如下
'''
lambda [arg1 [,arg2,.....argn]]:expression
'''

# 实例如下
mysum = lambda arg1, arg2: arg1 + arg2
# 调用mysum函数
print("相加后的值为 : ", mysum(10, 20))
print("相加后的值为 : ", mysum(20, 20))


# return 退出函数，返回返回值
def sumreturn(arg1, arg2):
    # 返回2个参数的和."
    total1 = arg1 + arg2
    print("函数内 : ", total1)
    return total1


# 调用sum函数
total = sumreturn(10, 20)
print("函数外 : ", total)

print("///////////////////////////////////////////////////////")

# python的输入输出格式

# 格式美化：str()： 函数返回一个用户易读的表达形式，repr()： 产生一个解释器易读的表达形式
# 输出平方立方表
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')  # 1、注意这里的end, 在输出位后加空格 2、rjust表示靠右，为字符串的一个方法
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# str.format的使用
print('{}网址： "{}!"'.format('python在线学习', 'www.py40.com'))  # 括号及里面的字符被format()中的参数替换
print('{0} 和 {1}'.format('Google', 'py40'))
print('{1} 和 {0}'.format('Google', 'py40'))  # 括号中的数字，用于指定传参的位置
print('{name}网址： {site}'.format(name='python在线学习', site='www.py40.com'))  # 使用关键字参数
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'py40.com', other='Taobao'))  # 位置和参数可以任意结合

print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!a}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))  # !a表示使用ascii(), !s表示使用str(),!r表示使用repr(),用于对格式进行转化

print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))  # :和格式标识符可以跟着字段名，即允许对值进行更好的格式化，.3f表示小数点后保留三位
table = {'Google': 1, 'py40com': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))  # :后传入整数，保证该域至少有这么多的宽度，用于美化格式

table = {'Google': 1, 'py40com': 2, 'Taobao': 3}
print('Py40: {0[py40com]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))  # 传入字典，使用[]来访问键值
print('Py40: {py40com:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))  # 使用**来实现相同的功能

# 采用c语言的格式
print('常量 PI 的值近似为：%5.3f。' % math.pi)

# 输入格式
'''
str = input("请输入：")
print ("你输入的内容是: ", str)
'''

print("///////////////////////////////////////////////////////")
# python的文件操作
# 打开关闭：open(),close()

# 文件读取

# file.read(size = -1),按照字节读取 ，size为-1时，表示读取所有剩余字节
# file.readlines（size = -1），读取并返回一行，或返回最大size个字符
# file.readlines(sizhint = 0),读取文件的所有行，并作为一个列表返回，若sizehint>0，则返回总和大约sizehint字节的行（具体由缓冲区大小决定）

# 文件写入

# file.write(str)  # 向文件写入指定字符
# file.write(seq)  # 向文件写入串序列seq，seq是任何返回字符串的可迭代对象

# 文件写入的时候，不会自动加上换行符，需要手动添加
# 实例：
'''
f = file('/root/test.py','a+')
codelst = ['\n','import os\n',"os.popen('ls').read()\n"]
f.writelines(codelst)
f.close()
file('/root/test.py','r').read()
"print 'hello,world'\nimport os\nos.popen('ls').read()\n"
'''

print("///////////////////////////////////////////////////////")
# python模块
# 见文件test.py给出的实例

print("///////////////////////////////////////////////////////")
# python的异常处理机制

# 异常处理的标准语法格式如下：
'''
try:
    try_suite
except Exception1,Exception2,...,Argument as e:
    exception_suite
    
    #other exception block
else:
    no_exceptions_detected_suite
finally:
    always_execute_suite
'''

# try..except用法
# try_suite是需要捕获异常的代码，except是关键，try捕获了try_suite里的异常后，将交给except来处理

# try...except最简单的形式如下：
# 形式1
'''
try:
    try_suite
except:
    exception block
'''
# 形式2
'''
try:
    try_suite
except Exception as e:
    exception block
'''

# 实例举例
'''
try:
    lines=open(tfile,'r',encoding='utf-8').readlines()
    flen=len(lines)-1
    for i in range(flen):
        if sstr in lines[i]:
            lines[i]=lines[i].replace(sstr,rstr)
    open(tfile,'w').writelines(lines)     
    print('修改文件内容为：'+rstr)
except IOError:
    print('输入输出异常')
except AttributeError:
    print('尝试访问未定义的属性')
except Exception as e:
    print(e)
    print('打开失败了')

'''

# try..except...else用法
# 没有检测到异常的时候，则执行else语句

# 实例如下：(可参考该实例)
'''
import syslog
try:
    f = open("/root/test.py")
except IOError, e:
    syslog.syslog(syslog.LOG_ERR,"%s"%e)
else:
    syslog.syslog(syslog.LOG_INFO,"no exception caught\n")

f.close()
'''

# finally子句用法
# finally子句是无论是否检测到异常，都会执行的一段代码，可以丢掉except子句和else子句，单独使用try...finally，也可配合except等使用
# 相关方法可查阅资料

# 断言（assert）的使用方法
# 表达式为：assert expression[,reason]
# 使用规则：assert是断言的关键字。执行时，先判断表达式expression，如果值为真，什么都不做，如果表达式值为假，则抛出异常，reason类似异常类的实例
# 实例举例：
'''
assert len('love') == len('like')
print("////////")
assert 1==1
print("////////")
assert 1==2, "1 is not equal 2!"
print("////////")
'''
# 注：如上代码执行时，前两个assert什么都没做，第三个assert抛出了异常1 is not equal 2！，此时传入的字符串"1 is not equal 2!"被作为异常类的
# 实例的具体信息而存在

# assert异常也可以被try块捕获

print("///")
try:
    assert 1 == 2, "1 is not equal 2!"
except AssertionError as reason:
    print("%s:%s" % (reason.__class__.__name__, reason))
    print(type(reason))
