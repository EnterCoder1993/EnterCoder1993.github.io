---
title: 双系统Windows时间不同步问题
date: 2018-09-07 20:59:08
tags: Time
categories: Problems
---

# 双系统Windows时间不同步问题

在电脑上安装使用双系统时，Windows常常会出现时间不同步的为题。需要重新设置时间才能解决。今天偶然在[掘金](https://juejin.im/entry/5adbd1ad51882567137dc6de)上看到这个问题，并解决了我电脑的问题，因此记录下来备忘。

1. Win + R 运行regedit打开注册表编辑器

![regedit](https://ws1.sinaimg.cn/large/006tNbRwgy1fv1a2hldkdj30nu0ghwf4.jpg)

2. 在左边的导航菜单，找到`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation`路径，然后再右边的窗口点击空白位置，选择`New >> DWORD(32 bit) Value`

![value](https://ws1.sinaimg.cn/large/006tNbRwgy1fv1a7ij71dj30a505nt8j.jpg)

3. 将这个条目重命名为`RealTimeIsUniversal`，并设置为`1`

![1](https://ws2.sinaimg.cn/large/006tNbRwgy1fv1a9e4xo4j30az087q2t.jpg)

4. 之后重启就不会出现时间不同步的问题了。

参考：    
* [https://juejin.im/entry/5adbd1ad51882567137dc6de](https://juejin.im/entry/5adbd1ad51882567137dc6de)

* [原文](https://link.juejin.im/?target=http%3A%2F%2Fwww.theitstuff.com%2Fhow-to-sync-time-between-linux-and-windows-dual-boot-2)