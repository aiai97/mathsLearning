循环字典，items(),enumerate(),zip()
for k, v in knights.items():
for i, v in enumerate(['tic', 'tac', 'toe']):
for q, a in zip(questions, answers):
reversed(),sorted(),set()
for f in sorted(set(basket)):
我希望我以后不要老失眠，活着就好了，每天一边犯困上班的感觉真不舒服。起码睡够了，学习效率才高。
外界的纷纷扰扰与我无关。我也不想认识任何人。
Python 与 C 不同，在表达式内部赋值必须显式使用 海象运算符 :=。 
我只是很少遇到过下面的比较
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
fibo.__name__ 是一个 Python 表达式，用于获取函数对象 fibo 的名称。
在 Python 中，函数是一种对象，它具有一些特殊属性。其中 __name__ 是一个特殊属性，用于获取函数对象的名称。
这项操作将执行模块里的代码，和导入模块一样，但会把 __name__ 赋值为 "__main__"。 也就是把下列代码添加到模块末尾：
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

sys模块
dir() 1，查看当前作用域内可用的变量、函数和类
my_list = [1, 2, 3]
print(dir(my_list))  # 输出 my_list 对象的属性和方法列表
my_list = [1, 2, 3]
if 'append' in dir(my_list):
    getattr(my_list, 'append')(4)  # 动态调用 my_list 对象的 append 方法，添加元素 4
我可能今年知道学习编程是件很容易的事情，只是我以前都被些笨蛋忽悠，我非常讨厌他们。我不想撒谎，我觉得学习编程和数学，起码对于我来说，不难。

导入子模块
还可以从包中导入单个模块，例如：
import sound.effects.echo
另一种导入子模块的方法是 ：
from sound.effects import echo
从包中导入 *，唯一的解决方案是提供包的显式索引，__all__ = ["echo", "surround", "reverse"]
包中含有多个子包时（与示例中的 sound 包一样），可以使用绝对导入引用兄弟包中的子模块。例如，要在模块 sound.filters.vocoder 中使用 sound.effects 包的 echo 模块时，可以用 from sound.effects import echo 导入。

7输入输出
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
str() 函数返回供人阅读的值，repr() 则生成适于解释器读取的值
print(f'The value of pi is approximately {math.pi:.3f}.')
在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐：

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
还有一些修饰符可以在格式化前转换值。 '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr()：

string.format()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
                  table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
格式化填充字符串
文件操作
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed

import json
x = [1, 'simple', 'list']
json.dumps(x)
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise



