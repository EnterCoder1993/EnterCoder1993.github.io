---
title: Python文件处理
date: 2018-09-11 11:54:14
tags: Python
categories: Note
---

# Python文件处理

## Python文件基础操作

文件：Python中文件是对象；
linux文件：一切设备都可以看成文件，例如：磁盘文件，管道，网络Socket，外设等；
文件属性：用户，读，写，执行权限

### Python文件打开方式

文件打开方法：open(name[,mode[buf]])

* name：文件路径
* mode：打开方式
* buf：缓冲buffering大小

| mode      | 说明               | 注意               |
| --------- | ------------------ | ------------------ |
| 'r'       | 只读方式打开(默认)    | 文件必须存在       |
| 'w'       | 只写方式打开       | 文件不存在创建文件,文件存在则清空文件内容 |
| 'a'       | 追加方式打开       | 文件不存在创建文件 |
| 'r+'/'w+' | 读写方式打开       |                    |
| 'a+'      | 追加和读写方式打开 |                    |

```python
# 默认为只读
f = open('push.py')
x = f.read()
```

```python
# 以只写方式打开文件，若文件文件不存在创建文件,文件存在则清空文件内容
f = open('1.txt','w')
f.write("test write")
f.close()
# 以追加方式打开文件
f = open('hello.py','a')
f.write('print('write test')')
f.close()
# 以读写方式r+打开，会覆盖文件内容
f = open('hello.py','r+')
f.write('test r+')
f.close()
# 以读写方式w+打开，会先清空文件内容
f = open('hello.py','w+')
f.write('test r+')
f.close()
```

#### Python读取方式

* read([size])：读取文件(读取size个字节，默认读取全部)
* readline([size])：读取一行
    * len(line) > size return size
    * len(line) < size return len(line)
* readlines([size])：读取缓冲buff左右的文件，返回每一行所组成的列表

```python
f = open('hello.py')
list_c = f.readlines(1)
# 仍返回hello.py中的所有内容，这是因为readlines([size])里的size默认大小为8192字节
import io
>>> io.DEFAULT_BUFFER_SIZE
8192
# 此hello.py大小大于8192字节
f = open('hello.py')
list_c = f.readlines(1)
# readlines每次只读取与buff缓冲相接近的数字
# 使用迭代器可完成整个文件的读取
iter_f = iter(f)
lines = 0
for line in iter_f:
    lines += 1
```

#### Python写入方式

* write(str)：将字符串写入文件
* writelines(sequence_of_strings)：写入多行到文件，参数为可迭代的对象

```python
f = open('hello.py','w')
f.write('test write)
f.close()

# 以writelines写入文件
f.open('hello.py','w')
f.writelines(('1','2','3'))
f.writelines(['1','2','3'])
f.close()
f = open('hello.py','w')
f.write('1111111')
cat hello.py
# 结果仍未空，因未执行文件操作，写入操作还未写入磁盘
```

写入文件过程

![writefile](https://ws2.sinaimg.cn/large/0069RVTdgy1fv5xd6cyoij31kw0dxwgk.jpg)

> 1. 主动调用close()或者flush()方法，写缓存同步到磁盘
> 2. 写入数据量大于或者等于写缓存，写缓存同步到磁盘

#### Python文件关闭

1. 缓存同步到磁盘
2. linux系统中每个进程打开文件的个数是有限的
3. 如果打开文件数到了系统限制，再打开文件就会失败

linux系统限制

```bash
ps #查看进程ID
cat /proc/进程ID/limits
# 可查看软件限制和硬件限制文件打开个数
```

fileno属性指当前打开文件数，每打开一个文件，fileno返回的整数+1

```python
list_f = []
for i in range(1025):
    list_f.append(open('hello.py','w'))
    print("%d:%d" % (i,list_f[i].fileno()))
# 当超如软件限制时，就会出现打开失败的错误
```

#### Python文件指针

文件读取写入文件指针移动的过程：
![filecur](https://ws1.sinaimg.cn/large/0069RVTdgy1fv5xr3xrmaj30mk0dkgmu.jpg)

Python操作文件指针

* seek(offset[,whence])：移动文件指针
    * offset：偏移量，可以为负数
    * whence：偏移相对位置
        * os.SEEK_SET：相对文件起始位置 0
        * os.SEEK_CUO：相对文件当前位置 1
        * os.SEEK_END：相对文件结尾位置 2

```python
f = open('hello.py','r+')
import os
# 返回当前文件的偏移
f.tell()
f.read(3)
# 指针回到起始位置
f.seek(0,os.SEEK_SET)
f.tell()
# 指针回到结尾位置
f.seek(0,os.SEEK_END)
f.tell()
# 指针相对当前位置向左偏移5
f.seek(-5,os.SEEK_CUR)
f.tell()
```

# 文件属性及OS模块使用

## Python文件属性编码格式

### Python文件对象属性

file.fileno()：文件描述符
file.mode：文件打开权限
file.encoding：文件编码格式
file.closed：文件是否关闭

### Python标准文件

文件标准输入：sys.stdin
文件标准输出：sys.stdout
文件标准错误：sys.stderr

### 文件命令行参数

```python
import sys
if __name__ == "__mian__":
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)
```

## OS模块对文件和目录操作

`os.open(filename,flag[,mode])`：打开文件

* flag：打开文件方式
    * os.O_CREAT：创建文件
    * os.O_RDONLY：只读方式打开
    * os.O_WRONLY：只写方式打开
    * os.O_RDWR：读写方式打开

`os.read(fd,buffersize)`：读取文件

`os.write(fd,string)`：写入文件

`os.lseek(fd,pos,how)`：文件指针操作

`os.close(fd)`：关闭文件