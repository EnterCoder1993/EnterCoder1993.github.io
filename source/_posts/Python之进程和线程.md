---
title: Python之进程和线程
date: 2018-09-13 21:38:38
tags: Python
categories: Note
---

# Python之进程和线程

> 对于操作系统来说，一个任务就是一个进程(Process)，比如打开浏览器就是启动一个浏览器进程，打开记事本，就启动了记事本进程。而且有些进程还能同时做几件事情，要同时做几件事，就需要同步运行多个“子任务”，进程内的这些“子任务”称为线程(Thread)。

Python执行多进程有以下两种解决方案：

1. 多进程模式；
2. 多线程模式；
3. 多进程+多线程模式

## 多进程

Unix/Linux提供了一个fork()系统调用。fork()调用一次返回两次，因为操作系统自动把当前进程(父进程)复制了一份(称为子进程)，然后分别在父进程和紫禁城内返回。

子进程永远返回`0`，父进程返回子进程的ID。因为一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。

```python
import os

print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('i am process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```

运行结果

```python
Process (2291) start...
I (2291) just created a child process (2294).
i am process (2294) and my parent is 2291.
```

有了fork调用，一个进程在接到新的任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

缺点：因为Windows没有fork调用，所以上述代码在Windows上无法运行。

### multiprocessing

multiprocessing提供了一个Process类来代表一个进程对象

```python
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
if __name__ == '__main__':
    print('Parent process %s. ' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')
```

结果如下：

```python
Parent process 2357.
Child process will start.
Run child process test (2360)...
Child process end
```

创建子进程时，只需要传入一个执行函数和函数参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()简单多了。

### Pool

Pool可以启动大量的子进程，可以用进程池的方式批量创建子进程。

```python
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 调用close后就不能添加新的Process了
    p.close()
    # Pool对象调用join方法会等待所有进程执行完毕
    p.join()
    print('All subprocesses done.')
```

### 子进程

subprocess模块可以非常方便地启动一个子进程，然后控制其输入和输出。

```python
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)

# 输入可以通过communicate()
import subprocess
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```

### 进程间通信

Python的multiprocessing模块包装了底层的机制，通过了Queue、Pipes等多种方式交换数据。

```Python
# 以Queue为例
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from eue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```