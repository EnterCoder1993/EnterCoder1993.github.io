---
title: Python之collections模块
date: 2018-09-06 22:27:52
tags: Python
categories:  Note
---

# collection模块

## tuple的功能

* 不可变、iterable

    ```python
    name_tuple = ('entercoder1','entercoder2')
    for name in name_tuple:
        print(name)
    ```

* 拆包

    ```python
    user_tuple = ('entercoder',26,175,'beijing')
    name,age,height = user_tuple
    print(name,age,height)
    name,*other = user_tuple
    print(name,other)
    ```

* 不可变性不是绝对的

    ```python
    name_tuple = ("entercoder",[29,175])
    name_tuple[1].append(22)
    ```

* tuple比list好的对象
    * immutable的重要性
        * 性能优化
        * 线程安全
        * **可以作为dict的key**

        ```python
        user_tuple = ('entercoder',26,175,'beijing')
        user_info_dict = {}
        user_info_dict[user_tuple] = 'entercoder'
        ```

        * 拆包特性
    * C语言类比，Tuple对应struct

## namedtuple的功能

用法：

```python
from collections import namedtuple
User = namedtuple("User",["name","age","height"])
user = User(name="entercoder",age=29,height=175)
print(user.name,user.age,name.height)
```