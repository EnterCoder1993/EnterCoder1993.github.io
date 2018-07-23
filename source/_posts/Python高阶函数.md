---
title: Python高阶函数
date: 2017-11-23 09:52:17
tags: Note
categories: Python
---


函数式Python内建支持的一种封装，通过吧大段代码拆成函数，通过一层层调用，就可以把复杂的任务分解成简单的任务，这种分解称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

<!--more-->

## 高阶函数

### 变量可以指向函数

函数本身可以赋给变量，即：变量可以指向函数。

```
f = abs
f
<built-in function abs>
f(-10)
10
```

### 函数名也是变量

当把abs指向10后，就无法调用abs函数了，因为abs这个变量已经不再指向求绝对值的函数而是指向一个整数。如果要恢复abs函数，只能重启Python交互环境。

```
abs = 10
abs(-10)
Error
```

### 传入函数

一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。

```
def add(x,y,f):
	return f(x) + f(y)
	
add(-5,6,abs)
11
```

### map()、reduce()、filter()和sorted()

#### map()

map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数一次作用到序列的每个元素，并把结果作为新的Iterator返回。

```
def f(x):
		 return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
list(r)
[1,4,9,16,25,36,49,64,81]
```

#### reduce()

reduce()把一个函数作用在一个序列[x1,x2,x3,...]上，reduce()**必须接收两个函数**，reduce把结果继续和序列的下一个元素做累积计算。

```
#把序列转化为整数
from functools import reduce
def fn(x,y):
    return x * 10 + y

reduce(fn,[1,3,5,7,9])
13579
```
把str转换为int的函数

```
from functools import reduce

def fn(x,y):
	return x * 10 + y
	
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	
reduce(fn,map(char2num,'13579'))
13579
```
整理成一个**str2int**的函数

```
from functools import reduce

def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))
```
使用lambda函数简化

```
from functools import reduce

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
	return reduce(lambda x,y:x * 10 + y,map(char2num,s))
```

#### filter()

filter()用于过滤序列，filter()接收一个函数和一个序列两个参数，filter把传入的函数依次作用于每个元素，然后根据返回值是True或False决定保留或丢弃该元素。filter函数返回的是一个Iterator，需要用list()函数获得所有的结果并放回list。

在一个list钟，删除偶数保留基数

```
def is_odd(s):
	return n % 2 == 1
	
list(filter(is_odd,[1,2,4,5,6,9,10,15]))
```
去掉序列中的空字符串

```
def not_empty(s):
	return s and s.strip()
	
list(filter(not_empty,['a',' ','c','  ']))
```

#### sorted()

sorted()函数是一个高阶函数，可以接收一个key函数来实现自定义的排序。

```
sorted([-1,36,24,5,-20])
[-20,-1.5,24,36]

sorted([-1,36,24,5,-20],key=abs,reverse=True)
[36, 24, -20, 5, -1]
```

## 返回函数

### 函数作为返回值

高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回。

```
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
```
如果不需要立刻求和，而是在后面的代码中根据需要在计算，可以不返回求和的结果，而是返回求和的函数

```
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
```

### 闭包

#### What

在函数中定义函数，并且内部函数可以引用外部函数的参数和局部变量，当外函数返回内函数时，相关参数和变量都保存在返回的函数中，这种方式是称为“闭包”。

一般情况下，函数中的局部变量仅在函数的执行期间可用，一旦函数执行过后，局部变量将不再可用。闭包可以使得局部变量在函数外被访问编程可能。

```
def print_msg():
	# print_msg是外围函数
	msg = "The Zen of Python"
	def printer():
		print(msg)
	return printer
	
another = print_msg()
# 输出The Zen of Python
another()
```

#### Why

闭包避免使用全局变量，还能降函数与所操作的某些数据（环境）关联起来。一般来说，党对象中只有一个方法时，使用闭包时更好的选择。

```
def adder(x):
	def wrapper(y):
		return x + y
	return wrapper

adder5 = adder(5)
#输出15
adder5(10)
#输出6
adder5(6)
```

## 匿名函数

### What

匿名函数，就是没有名字的函数。关键字lambda可以创建匿名函数，匿名函数有一个限制，就是只能有一个表达式，不用写return，返回追就是该表达式的结果。

```
lambda 参数: 表达式

add = lambda x,y : x + y
add(1,3)
4
```

### Why

lambda函数一般适用于创建一些临时性的，小巧的函数。

```
def func(g,arr):
	return [g(x) for x in arr]

arr = func(lambda x: x + 1,[1,2,3,4,5])
```

## 装饰器

希望增强函数的额功能，但是又不希望修改函数的定义，这种在代码运行期间动态的增加功能的方式，称之为“装饰器”，本质上，装饰器就是一个返回函数的高阶函数。

 ```
 def foo():
 	print('foo')
 	
 def bar(func):
 	func()
 	
 bar(foo)
 ```
 
### 简单装饰器
 
use_logging就是一个装饰器，它是一个普通的函数，把真正业务逻辑的函数func包裹在其中，use_logging返回的也是一个函数，这个函数的名字叫wrapper。
 
```
 def use_logging(func):
	def wrapper():
		print('%s is running' % func.__name__)
		return func()
	return wrapper()
	
def foo():
	print('i am foo')
	
foo = use_logging(foo)
foo()
```
 
### 语法糖
 
@符号就是装饰器的语法糖，它放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作。
 
```
 def use_logging(func):
	def wrapper():
		print('%s is running' % func.__name__)
		return func()
	return wrapper()
	
@use_logging
def foo():
	print('i am foo')
	
foo()
```

## 偏函数

partial函数可以固定函数参数，并返回一个新的函数，当函数的参数太多，需要固定某些参数时，可以使用functools.partial创建一个新的函数。

```
functools.partial(func[,*args][,\*\*kwargs]
```
转换二进制字符串

```
def int2(x,base=2):
	return int(x,base)
```

使用functools.partial创建一个偏函数。

```
import functools
int2 = functools.partial(int,base=2)
int2('1000000')
64
```

参考教程：
[廖雪峰的Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000)





