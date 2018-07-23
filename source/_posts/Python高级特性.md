---
title: Python高级特性
date: 2017-09-02 00:28:02
tags: Note
categories: Python
---

在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好

<!--more-->

## 切片

切片就是对字符串进行各种截取操作。

```
>>> l = list(range(1,10))
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[0:3] #0-3
[1, 2, 3]
>>> l[:3] #0-3
[1, 2, 3]
>>> l[-2:] #倒数切片
[8, 9]
>>> l[::3] #每隔三个数
[1, 4, 7]
>>> l[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> (1,2,3,4,5,6)[:3] #tuple
(1, 2, 3)
>>> 'abcdefg'[:3] #字符串切片
'abc'
```

## 迭代

通过for循环来遍历list或tuple

```
>>> for ch in 'abc':
...     print(ch)
...
a
b
c
```
默认情况下迭代value，可以用for value in d.value()
同时迭代key和value，可以用for k,v in d.items
可以用Iterable判断一个对象是否为可迭代对象

```
>>> from collections import Iterable
>>> isinstance('abc',Iterable)
True
>>> isinstance([1,2,3],Iterable)
True
>>> isinstance(123,Iterable)
False
```
通过enumerate可以把一个list变成索引-元素对

```
>>> for i,value in enumerate(['a','b','c']):
...     print(i,value)
...
0 a
1 b
2 c
```
## 列表生成式


```
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> [x * x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> [x * x for x in range(1,11) if x % 2 == 0]
[4, 16, 36, 64, 100]
>>> [m + n for m in 'abc' for n in 'xyz']
['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']
>>> import os
>>> [d for d in os.listdir('.')]
['.android', '.atom', '.bash_history']
>>> d = {'x':'a','y':'b','z':'c'}
>>> [k + '=' + v for k,v in d.items()]
['x=a', 'y=b', 'z=c']
>>> l = ['Hello','Word','IBM','Apple']
>>> [s.lower() for s in l]
['hello', 'word', 'ibm', 'apple']
```

## 生成器

一边循环一边计算的列表成为列表生成器
```
>>> l = [x*x for x in range(10)]
>>> l
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x*x for x in range(10))
>>> g
<generator object <genexpr> at 0x10eecc200>
```
l和g的区别仅在于最外层的[]和()，l是一个list，而g是一个generator，需要通过next()函数才能获得generator的下一个返回值
```
>>> next(g)
0
>>> next(g)
1
```
generator保存的是算法，每次调用next(g)，直到最后一个元素时就会抛出StopIteration的错误。可以使用for循环来迭代generator

```
>>> def fib(max):
...     n,a,b=0,0,1
...     while n < max:
...          yield b
...          a,b = b,a+b
...          n = n + 1
...     return 'done'
...
>>> fib(6)
<generator object fib at 0x10eecc2b0>
>>> for n in fib(6):
...     print(n)
...
1
1
2
3
5
8
```
## 迭代器

可以直接作用于for循环的数据类型：
* 集合数据类型，如list、tuple、dict、set、str等；
* generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象称为可迭代对象：Iterable，可以使用isinstance()判断一个对象是否是Iterable对象。
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
可以使用iter()函数把Iterable变成Iterator

```
>>> from collections import Iterator
>>> isinstance(iter('abc'),Iterator)
True
```
Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
