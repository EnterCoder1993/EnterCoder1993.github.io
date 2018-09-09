---
title: Python面向对象编程
date: 2018-09-09 22:28:59
tags: Python
categories: Note
---

# Python面向对象编程

> 面向对象编程(Object Oriented Programming，简称OOB)是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

```python
# 采用面向对象编程，将Student这种数据类型视为一个对象，这个对象拥有name和score两个属性。如果要打印学生的成绩，首先必须创建出这个学生对应的对象，然后调用对象的方法，让对象自己把对应的数据打印出来。
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

# 给对象发消息实际上是调用对象对应的关联函数，称之为对象的方法
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
```

## 类和实例

面向对象最重要的概念就是类(Class)和实例(Instance)，类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

定义类是通过`class`关键字：

```python
class Student(object)：
    pass

# 变量指向的就是类的实例，0x10b0a60b8是内存地址，每个实例的地址都不一样。
bart = Student()
bart
<__main__.Student object at 0x10b0a60b8>
Student
<class '__main__.Student'>
```

类可以起到模板的作用，因此在创建实例的时候，把一些必须绑定的数据强制填写进去。通过一个特殊的`__init__`方法。

```python
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score
```

> 特殊方法`__init__`前后分别有两个下划线，`__init__`方法的第一个参数永远是self，表示创建实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传递进去。

### 数据封装

每个实例都拥有自己的数据。可以通过函数来访问这些数据，实例本身就拥有数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法。

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
```

# 访问限制

在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。

```python
class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))
# 改吗修改完成后，对外部代码来说没有什么变化，但是 已经无法从外部访问实例变量.__name和实例变量.__score了。
```

好处：这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

外部无法获取name和score属性，就需要给类增加响应的get和set方法：

```python
class Student(object):
    ...
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
# 这样可以在方法中对传入的数据进行检查，便面传入无效参数。
```

> 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 集成和多态

当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

```python
class Animal(object):
    def run(self):
        print('Animal is running...')

# 编写Dog和Cat类
class Dog(Animal):

    def run(self):
        pass
class Cat(Animal):
    def run(self):
        print('Cat is running')

# 子类可以获得父类的全部功能
dog = Dog()
dog.run()
Animal is running...

# 当子类和父类都存在相同的run方法时，子类的方法会覆盖父类的方法，代码运行时总会调用子类的run()方法。这是继承的另一个好处：多态。
# 判断某个变量是否为某个类型时，可以用isinstance()判断
>>> isinstance(dog,Dog)
True
```

![object](https://ws3.sinaimg.cn/large/006tNbRwgy1fv3p1mim8rj30a105sjr7.jpg)

对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了,

# 获取对象信息

* 使用type()可以判断对象的类型
* 使用isinstance()可以判断类的继承关系
* 使用dir()
    * 使用dir()可以获取一个对象的所有属性和方法，它返回一个包含字符串的list

# 实例属性和类属性

如果类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归类所有