range()函数
如果只输出 range，会出现意想不到的结果：
range(10)
range(0, 10)
range() 返回对象的操作和列表很像，但其实这两种对象不是一回事。迭代时，该对象基于所需序列返回连续项，并没有生成真正的列表，从而节省了空间。

这种对象称为可迭代对象 iterable，函数或程序结构可通过该对象获取连续项，直到所有元素全部迭代完毕。for 语句就是这样的架构，sum() 是一种把可迭代对象作为参数的函数：
sum(range(4))  # 0 + 1 + 2 + 3

match
函数默认值def ask_ok(prompt, retries=4, reminder='Please try again!'):
关键字参数
最后一个形参为 **name 形式时，接收一个字典（详见 映射类型 --- dict），该字典包含与函数中已定义形参对应之外的所有关键字参数。**name 形参可以与 *name 形参（下一小节介绍）组合使用（*name 必须在 **name 前面）， *name 形参接收一个 元组，该元组包含形参列表之外的位置参数。例如，可以定义下面这样的函数：

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

函数示例
def standard_arg(arg):
    print(arg)

/代表位置参数，*代表keyword
def pos_only_arg(arg, /):
    print(arg)  

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

variadic 参数用于采集传递给函数的所有剩余参数，因此，它们通常在形参列表的末尾。*args 形参后的任何形式参数只能是仅限关键字参数，即只能用作关键字参数，不能用作位置参数：
def concat(*args, sep="/"):
    return sep.join(args)

4.8.5. 解包实参列表
函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 range() 函数要求独立的 start 和 stop 实参。如果这些参数不是独立的，则要在调用函数时，用 * 操作符把实参从列表或元组解包出来：
list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
同样，字典可以用 ** 操作符传递关键字参数：
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

4.8.6. Lambda 表达式
lambda 关键字用于创建小巧的匿名函数。lambda a, b: a+b 函数返回两个参数的和。Lambda 函数可用于任何需要函数对象的地方。在语法上，匿名函数只能是单个表达式。在语义上，它只是常规函数定义的语法糖。与嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量：

>>>
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
42
f(1)
43
上例用 lambda 表达式返回函数。还可以把匿名函数用作传递的实参：
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']

list列表

1. 增加元素：

Python: 使用append()方法将元素添加到列表末尾。
C++: 使用push_back()方法将元素添加到列表末尾。
Java: 使用add()方法将元素添加到列表末尾。
2. 删除元素：

Python: 使用remove()方法删除列表中的元素，或使用pop()方法删除指定索引位置的元素。
C++: 使用erase()方法删除指定迭代器位置的元素，或使用pop_back()方法删除列表末尾的元素。
Java: 使用remove()方法删除列表中的元素，或使用remove(index)方法删除指定索引位置的元素。
3. 修改元素：

Python: 直接通过索引对元素进行赋值修改。
C++: 直接通过迭代器对元素进行赋值修改。
Java: 使用set()方法将指定索引位置的元素替换为新元素。
4. 查找元素：

Python: 使用index()方法返回列表中第一个匹配元素的索引。
C++: 使用find()方法返回指向第一个匹配元素的迭代器。
Java: 使用indexOf()方法返回第一个匹配元素的索引。


#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
# classmates.pop(1)

zip(*iterables, strict=False)
在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。

示例:
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
zip() 与 * 运算符相结合可以用来拆解一个列表:

python的list真的非常奇怪，很多方法我都是第一次见到，好像java没那么烦人，java就是那堆背八股文的人类讨厌些。
我好想念c++，起码好像c++的容器的crud名字都一样.
等我那天吃饱饭没事干时，我一定会洗洗数一下，哪个语言的容器的方法最难记。我觉得人生好无聊呀。既然这些编程语言都是他们老外开发的，那为什么
他们不能统一一下命名呢？他们知道我记忆力不好，英语不好，也不爱学习吗？一边学习会一边抱怨和发牢骚吗？
list.pop([i])
删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，a.pop() 删除并返回列表的最后一个元素。（方法签名中 i 两边的方括号表示该参数是可选的，不是要求输入方括号。这种表示法常见于 Python 参考库）。
ist.clear()
删除列表里的所有元素，相当于 del a[:] 。

list.index(x[, start[, end]])
返回列表中第一个值为 x 的元素的零基索引。未找到指定元素时，触发 ValueError 异常。

可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

list.count(x)
返回列表中元素 x 出现的次数。

list.sort(*, key=None, reverse=False)
就地排序列表中的元素（要了解自定义排序参数，详见 sorted()）。

list.reverse()
翻转列表中的元素。

list.copy()
返回列表的浅拷贝。相当于 a[:] 。

用列表可以实现队列和堆栈
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
x = [1, 2, 3]
y = [4, 5, 6]
list(zip(x, y))

x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)

del()
用 del 可以删除键值对。用已存在的关键字存储值，与该关键字关联的旧值会被取代。通过不存在的键提取值，则会报错。
对字典执行 list(d) 操作，返回该字典中所有键的列表，按插入次序排列（如需排序，请使用 sorted(d)）。检查字典里是否存在某个键，使用关键字 in。
有时我真的觉得，是个人类都不热爱学习，机器人或者吃苦耐劳的人，才会喜欢编程。
那我肯定是个正常的人类，一边学习，一边说，哦，我不喜欢编程，我只是喜欢程序员。我想做个聪明点的程序员。
人生真的好无聊。

谁记得住这些破构造方法，我每次想构造什么list或者dict或者什么容器，我每次都要重新看一遍语法。
我有时真的好希望我是个机器人，这破学习这么无聊，要是机器人的话，什么都记得住。
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配：

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

逆向循环序列时，先正向定位序列，然后调用 reversed() 函数：

for i in reversed(range(1, 10, 2)):
    print(i)

按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新的序列：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
