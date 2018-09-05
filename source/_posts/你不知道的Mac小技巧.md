---
title: 你不知道的Mac小技巧
date: 2017-09-05 09:33:23
tags: [常用,Mac]
categories: macOS
---

# Mac可以添加自定义功能

> 主要是利用Automator来添加快捷功能，例例如右键添加复制文件或文件夹路径等。

<!--more-->

1.在Finder中打开应用程序

2.双击打开Automator.app

3.选择服务，点击选取

4.设置服务受到选定的文件或文件夹，位于Finder

5.在资源库中找到拷贝到剪贴板，拖动到右边窗口中

6.退出保存，将名称改为拷贝到剪贴板即可。


# Mac下显示和隐藏文件

打开终端，输入以下命令：

```bash
//此命令显示隐藏文件
defaults write com.apple.finder AppleShowAllFiles -bool true

//此命令关闭显示隐藏文件
defaults write com.apple.finder AppleShowAllFiles -bool false
```

命令运行之后需要重新加载Finder：快捷键option+command+esc，选中Finder，重新启动即可

# 截屏

* 将屏幕图片存储为文件 `Shift + Command + 3`
* 将屏幕图片拷贝到剪贴板 `Ctrl + Shift + Command + 3`
* 将所选区域的图片存储为文件 `Shift + Command + 4`
* 将所选区域的图片拷贝到剪贴板 `Ctrl + Shift + Command + 4`

# Split Screen分屏功能

按住窗口的最大会绿色按钮不放，选择放置在左边或者右边，然后选择另一个应用即可进行分屏，可以拖动中间的分割线调整左右区域的大小

---
2018.09.05更新

---