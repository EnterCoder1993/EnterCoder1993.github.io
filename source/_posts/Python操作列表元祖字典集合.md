---
title: Python操作列表、元祖、字典、集合
date: 2018-09-05 21:09:28
tags: Python
categories: Note
---

# 列表

* **列表**：由一系列按特定顺序排列的元素组成。可用list()函数或方括号创建，元素间用逗号分隔。

    ```python
    my_list = ['name','age']
    list1 = list((1,2))
    ```

* **访问元素**：列表是有序集合，通过元素的位置或索引即可访问列表的任何元素

    ```python
    computer = ['dell','asus','apple']
    print(computer[0])
    ```

## 修改、添加和删除元素

### 修改列表元素

```python
phone = ['xiaomi','oneplus','apple']
phone[0] = 'vivo'
```

### 添加列表元素

1. 在列表末尾添加元素

    ```python
    phone = ['xiaomi','oneplus','apple']
    phone.append('oppo')
    ```

2. 在列表中插入元素

    ```python
    phone = ['xiaomi','oneplus','apple']
    phone.insert(1,'SAMSUNG')
    ```

### 删除列表元素

1. 使用del语句删除元素

    ```python
    phone = ['xiaomi','oneplus','apple']
    del phone[2]
    ```

2. 使用pop()方法删除元素

    pop()方法可删除列表末尾的元素，并且可以接着使用它。

    ```python
    phone = ['xiaomi','oneplus','apple']
    new_phone = phone.pop()

    # 在括号中指定要删除的元素的索引可删除任何位置的元素
    my_phone = phone.pop(1)
    ```

3. 根据值删除元素

    使用remove方法可以删除元素的值，并且也可以接着使用它的值。

    ```python
    phone = ['xiaomi','oneplus','apple']
    your_phone = phone.remove('oneplus')
    ```

    > 方法remove()只删除第一个指定的值。多国药删除的值可能多次在列表中出现多次，就需要用循环来判断是否删除了所有的值。

## 组织列表

### 使用sort()方法对列表进行永久性排序

```python
cars = ['bmw','audi','toyota']
cars.sort()
# 按与字母顺序想法的顺序排列列表元素
cars.sort(reverse=True)
```

### 使用sorted()对列表进行临时排序

```python
cars = ['bmw','audi','toyota','BMW']
sorted(cars)
['BMW', 'audi', 'bmw', 'toyota']
```

### 倒着打印列表

使用reverse()方法可以反转列表元素的排列顺序，reverse()方法永久性地修改列表元素的排列顺序，但可以恢复原来的排列顺序，只需再次使用reverse()方法。

```python
cars = ['BMW', 'audi', 'bmw', 'toyota']
cars.reverse()
```

### 确定列表的长度

```python
cars = ['BMW', 'audi', 'bmw', 'toyota']
len(cars)
```

### 遍历整个列表

```python
cars = ['BMW', 'audi', 'bmw', 'toyota']
for car in cars:
    print(car)
```

### 创建数值列表

```python
for value in range(1,5):
    print(value)
1
2
3
4

numbers = list(range(1,6))

# 指定步长
even_numbers = list(range(2,11,2))
# 找出列表的最大值、最小值和总和
min(numbers)
max(numbers)
sum(numbers)
```

### 列表解析

```python
squares = [value**2 for value in range(1,11)]
```

### 使用列表的一部分

#### 切片

```python
cars = ['BMW', 'audi', 'bmw', 'toyota']
print(cars[0:2])
['BMW', 'audi']
print(cars[:3])
print(cars[2:])
print(cars[-2:])
```

#### 复制列表

复制列表可以创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引([:])

```python
my_foods = ['pizza','falafel','corrot cake']
your_foods = my_foods[:]
```

## 方法

| 操作           | 解释                             |
| -------------- | -------------------------------- |
| list.append()  | 追加元素                         |
| list.count(x)  | 计算列表中参数x出现的次数        |
| list.extend(L) | 向列表中追加另一个列表L          |
| list.index(x)  | 获得参数x在列表中的位置          |
| list.insert()  | 向列表中插入数据                 |
| list.pop()     | 删除列表中的成员（通过下标删除） |
| list.remove()  | 删除列表中的成员（直接删除）     |
| list.reverse() | 将列表中成员的顺序颠倒           |
| list.sort      | 将列表中成员排序                 |

# 元祖

不可变的列表被称为元祖。使用圆括号来标识。使用索引来访问元素。可以用tuple()函数或者括号创建，元素间用逗号分隔。

```python
dimensions = (200，50)
tuple1 = tuple([1,2])
print(dimensions[0])

## 遍历元祖中的所有值
for dimension in dimensions:
    print(demension)
```

虽然不能修改元祖的元素，但可以给存储元祖的变量赋值，重新定义整个元祖。

```python
dimensions = (100，200)
print(dimensions[0])

```

元组由于它的不可变性（第五点特点），相比列表的操作少了很多，只保留了index()，count()函数，用法同列表。当然也可以用内置函数来对他进行操作，这些内置函数对于列表也适用。

| 操作                | 解释                   |
| ------------------- | ---------------------- |
| cmp(tuple1, tuple2) | 比较两个元组元素。     |
| len(tuple)          | 计算元组元素个数。     |
| max(tuple)          | 返回元组中元素最大值。 |
| min(tuple)          | 返回元组中元素最小值。 |
| tuple(seq)          | 将列表转换为元组。     |
| list(seq)           | 将元组转换为列表。     |

# 字典

## 使用字典

**字典**是一系列键——值对。每个键都与一个值相关联，可以使用键来访问与之相关的值。可将任何Python对象用作字典中的值。可以用dict()或花括号创建，元素之间用逗号’,‘’分隔，键与值之间用冒号”:”隔开。键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

```python
alien = {'color':'green','point':5}
dict1 = dict([('name','entercoder'),('age',10)])
```

### 访问字典中的值

获取与键相关的值，指定字典名和放在方括号内的键。

```python
alien = {'color':'green','point':5}
alien['color']
alien['point']
```

### 添加键——值对

```python
alien['x_position'] = 0
alien['y_position'] = 25
```

### 创建一个空字典

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
```

### 修改字典中的值

```python
alien_0['color'] = 'yellow'
```

### 删除键——值对

使用del语句将相应的键——值对彻底删除。

```python
del alien_0['points']
```

### 由类似对象组成的字典

```python
favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
```

## 遍历字典

```python
favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for key,value in favorite_language.items():
    print("\nname: " + key.title())
    print("\nlanguage: " + value.title())

# 遍历字典中的所有键
for name in favorite_language.keys():
    print(name.title())

# 遍历字典中的所有值
for value in favorite_language.values():
    print(value.title())

# 按顺序遍历字典中的所有键
for name in sorted(favorite_language.keys()):
    print(name.title())
```

## 方法

| 操作                                                  | 解释                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| adict.keys()                                          | 返回一个包含字典所有KEY的列表；                              |
| adict.values()                                        | 返回一个包含字典所有value的列表；                            |
| adict.items()                                         | 返回一个包含所有（键，值）元祖的列表；                       |
| adict.clear()                                         | 删除字典中的所有项或元素；                                   |
| adict.copy()                                          | 返回一个字典浅拷贝的副本；                                   |
| adict.fromkeys(seq, val=None)                         | 创建并返回一个新字典，以seq中的元素做该字典的键，val做该字典中所有键对应的初始值（默认为None）； |
| adict.get(key, default = None)                        | 返回字典中key对应的值，若key不存在字典中，则返回default的值（default默认为None）； |
| adict.has_key(key)                                    | 如果key在字典中，返回True，否则返回False。 现在用 in 、 not in； |
| adict.iteritems() adict.iterkeys() adict.itervalues() | 与它们对应的非迭代方法一样，不同的是它们返回一个迭代子，而不是一个列表； |
| adict.pop(key[,default])                              | 和get方法相似。如果字典中存在key，删除并返回key对应的vuale；如果key不存在，且没有给出default的值，则引发keyerror异常； |
| adict.setdefault(key, default=None)                   | 和set()方法相似，但如果字典中不存在Key键，由 adict[key] = default 为它赋值； |
| adict.update(bdict)                                   | 将字典bdict的键值对添加到字典adict中。                       |

# 集合

1.可以用set()函数或者方括号{}创建，元素之间用逗号”,”分隔。 
2.与字典相比少了键 
3.不可索引，不可切片 
4.不可以有重复元素

```python
set1 = set('entercoder')
set2 = {'c','java','python','java'}
```

## 方法

| 操作                            | 解释                                            |
| ------------------------------- | ----------------------------------------------- |
| s.issubset(t)，s <= t           | 测试是否 s 中的每一个元素都在 t 中              |
| s.issuperset(t)，s >= t         | 测试是否 t 中的每一个元素都在 s 中              |
| s.union(t)，s \| t              | 返回一个新的 set 包含 s 和 t 中的每一个元素     |
| s.intersection(t)，s & t        | 返回一个新的 set 包含 s 和 t 中的公共元素       |
| s.difference(t),s - t           | 返回一个新的 set 包含 s 中有但是 t 中没有的元素 |
| s.symmetric_difference(t),s ^ t | 返回一个新的 set 包含 s 和 t 中不重复的元素     |
| s.copy()                        | 返回 set “s”的一个浅复制                        |

# 差异

## 用法

列表主要用于对象长度不可知的情况下，而元组用于对象长度已知的情况下，而且元组元素一旦创建变就不可修改。字典主要应用于需要对元素进行标记的对象，这样在使用的时候便不必记住元素列表中或者元组中的位置，只需要利用键来进行访问对象中相应的值。集合中的元素不可重复的特点使它被拿来去重。

> 在海量数据中查找元素时，最好将数据创建为字典，或者是集合。这是由于字典和集合背后的查找原理是散列（哈希）表。由于散列表在查找元素时的时间复杂度基本是O(1),这使查找时间很短。