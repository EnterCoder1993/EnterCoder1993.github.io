---
title: Python的系统编程工具
date: 2018-09-17 21:50:26
tags: Python
categories: Note
---

# Python的系统编程工具

<!--more-->

## 介绍sys模块

```python
import os,sys
# 分别有287和84个属性
len(dir(os))
287
len(dir(sys))
84
>>> sys.platform,sys.version,sys.maxsize
('darwin', '3.6.6 (v3.6.6:4cf1f54eb7, Jun 26 2018, 19:50:54) \n[GCC 4.2.1 Compatible Apple LLVM6.0 (clang-600.0.57)]', 9223372036854775807)
```

* 模块搜索路径

    sys模块使得我们可以在Python程序内部或者交互地常看模块搜索路径。sys.path是一个由目录名称字符串组成的列表，每个目录名称字符串代表正在运行的Python解释器的真正的搜索路径。

    sys.path可以用程序进程更改，比如append、extend、insert、pop、remove和del。

    `sys.path.append(r'C:\mydir')`

* sys模块导出的其他工具

    * 显示为由字符串组成的列表的命令行参数，称为sys.argv
    * 标准流，包括sys.stdin、sys.stdout和sys.stderr
    * 程序可以通过调用sys.exit强制退出

## 介绍os模块

* 常用的os模块

  | 任务               | 工具                                                         |
  | ------------------ | ------------------------------------------------------------ |
  | Shell变量          | os.environ                                                   |
  | 运行程序           | os.system,os.popen,os.execv,os.spawnv                        |
  | 派生进程           | os.fork,os.pipe,os.waitpid,os.kill                           |
  | 文件描述符，文件锁 | os.open,os.read,os.write                                     |
  | 文件处理           | os.remove,os.rename,os.mkdir,os.rmdir                        |
  | 管理工具           | os.getcwd,os.chdir,os.chmod,os.getpid,os.listdir,os.access   |
  | 移植工具           | os.sep,os.pathsep,os.curdir,os.path.split,os.path.join       |
  | 路径名工具         | os.path.exists('path'),os.path.isdir('path'),os.path.getsize('path') |

  ```python
  import os
  dir(os)
  len(dir(os))
  ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 
   ...
   'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'walk', 'write', 'writev']
  287
  dir(os.path)
  len(dir(os.path))
  ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_sep', '_joinrealpath', '_varprog', 
   ...
   'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
  55
  ```

* 管理工具

  ```python
  >>> os.getpid() # 给出调用函数的进程IDI
  1210
  >>> os.getcwd() # 返回当前的工作目录
  '/Users/entercoder'
  >>> os.chdir('/Users/entercoder/Documents') # 更改当前工作目录
  >>> os.getcwd()
  '/Users/entercoder/Documents'
  ```

* 可移植的常量

  os模块同时导出了一组用于简化跨平台编程的名称，包括具体平台相关的路径和目录分隔符、父目录和当前目录的指示器，以及底层计算机所采用的换行符。

  ```python
  >>> os.sep # 运行平台所采用的目录分隔符
  '/'
  >>> os.pathsep # 在目录列表中分隔目录的字符
  ':'
  >>> os.pardir # 上一级目录
  '..'
  >>> os.curdir # 当前目录
  '.'
  >>> os.linesep # 换行符
  '\n'
  ```

  ### 常见的os.path工具

  ```python
  # 判断文件类型
  os.path.isdir('/Users/entercoder/Documents/entercoder1993.github.io_back')
  True
  os.path.isfile('/Users/entercoder/Documents/entercoder1993.github.io_back')
  False
  # 判断文件是否存在
  os.path.exists('/Users/entercoder/Documents/entercoder1993.github.io_back')
  True
  # 获取文件的大小
  os.path.getsize('/Users/entercoder/Documents/entercoder1993.github.io_back')
  512
  # 分离目录和文件名
  os.path.split('/Users/entercoder/Documents/entercoder1993.github.io_back') 
  ('/Users/entercoder/Documents', 'entercoder1993.github.io_back')
  # 合并目录和文件名
  os.path.join('/Users/entercoder/Documents', 'entercoder1993.github.io_back')
  '/Users/entercoder/Documents/entercoder1993.github.io_back'
  # 返回目录名
  os.path.dirname('/Users/entercoder/Documents/Note-Book/README.md')
  '/Users/entercoder/Documents/Note-Book/'
  # 返回文件名
  os.path.basename('/Users/entercoder/Documents/Note-Book/README.md')
  'README.md'
  # 分离文件的扩展名
  os.path.splitext('/Users/entercoder/Documents/Note-Book/README.md')
  ('/Users/entercoder/Documents/Note-Book/README'，'.md')
  ```


