类初始化
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

class DerivedClassName(modname.BaseClassName):
多重继承class DerivedClassName(Base1, Base2, Base3):


from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

在幕后，for 语句会在容器对象上调用 iter()。 该函数返回一个定义了 __next__() 方法的迭代器对象，此方法将逐一访问容器中的元素。 当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环。 你可以使用 next() 内置函数来调用 __next__() 方法
s = 'abc'
it = iter(s)
it

next(it)
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
学编程真无聊，我都不知道我猴年马月学到图论，因为他跟我说了一堆图啥的，不过，好像是数学里的。我可能今年底或者明年初，就可以过完数学了。
我最近很喜欢数学，但是我不喜欢看那个recommender system.
我昨晚睡觉前，还在想一个问题，就是，嗯，允许我应该找一些设计模式和架构设计的知识学习，不然，
我一辈子会很多编程语言，每个都不深，猴年马月我都成为不了算法工程师或者架构师。
但是我非常怀疑，别人都能学，理论上，我学了几年，也能搞定。
听说那个造出python的人穿过一件衬衫，人生苦短，我爱python。想起我喜欢的男生，他说他要写出一门语言，然后啥都包了，嗯嗯，我本来还想看他五六十岁时会会不会秃头。
我要是跟他们一样，吃饱饭学编程十年，我也能踩完人工智能，迟早我都能看懂他们写的人工智能的论文，反正我有一辈子的时间。我觉得对我来说，两年就够了，我肯定能自学得还行。

看到那个破生成器表达式时，我总感觉我像个格格不入的老人，努力适应这个时代的变化和要求。
sum(x*y for x,y in zip(xvec, yvec)) 总感觉这个除了少打字和看着好看，没半毛钱用处

要不是日常使用python编程，我吃了好多亏，我才不会看这个无聊的破文档，我都不明白，为什么有些人类天生吃饱饭热爱学习，编写那个文档的人，一定有坚强的意志力，毕竟我看都觉得难受，能写出文档，一定很不容易。
而我恰好不幸在不爱学习的人类中间。我最爱的编程语言是c++和rust,因为我听说它们不好学，感觉学习了就能变得更加聪明。
我在看这些标准库时，越发觉得编程很容易学，因为感觉他们不过都服务于features。每每这时，我就好嫌弃那些笨蛋吃饱饭忽悠我，学习编程很难。
sys 模块还具有 stdin ， stdout 和 stderr 的属性。后者对于发出警告和错误消息非常有用
doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。
timeit 模块可以快速演示在运行效率方面一定的优势
中两个最简单的 urllib.request 用于从URL检索数据，以及 smtplib 用于发送邮件:
质量控制 doctest,unittest
xmlrpc.client 和 xmlrpc.server 模块使得实现远程过程调用变成了小菜一碟
我想，比起破语文，还是数学比较舒坦，起码昨天学了t分布的t值和p值后，我发现还蛮好用的，比如我拿到个一个popilation mean,standard deviation时，
ebm，我感觉可好玩了，反正一堆英文数学多的话，也没几个人看得懂。感觉数学比较有逻辑性，但是语文很无聊，尤其是破小说，每次看了都不开心。

如果人生可以重来的，我就应该大二时不恋爱，吃饱饭把c语言给学了。我现在做的事情就是，嗯，我要自学人工智能，因为我不希望，我三十几岁时数学一问三不知。快八年过去了。
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)

template批量重命名
列表操作的工具
array 模块提供了一种 array() 对象，它类似于列表，但只能存储类型一致的数据且存储密集更高
collections 模块提供了一种 deque() 对象，它类似于列表，但从左端添加和弹出的速度较快，而在中间查找的速度较慢。 此种对象适用于实现队列和广度优先树搜索:
例如 bisect 模块具有用于操作有序列表的函数:
heapq 模块提供了基于常规列表来实现堆的函数。 最小值的条目总是保持在位置零。 我都不记得堆的特性了，堆好像基于树弄的？最小堆？最大堆？

虚拟环境
用于创建和管理虚拟环境的模块称为 venv。venv 通常会安装你可用的最新版本的 Python。
python -m venv tutorial-env  这将创建 tutorial-env 目录，如果它不存在的话，并在其中创建包含 Python 解释器副本和各种支持文件的目录。
 source ~/envs/tutorial-env/bin/activate  deactivate
python -m pip install requests==2.6.0
python -m pip show requests
python -m pip list
python -m pip freeze > requirements.txt

python -m pip install -r requirements.txt
https://code.activestate.com/recipes/580787-implementing-function-based-callbacks-in-python/?in=lang-python
