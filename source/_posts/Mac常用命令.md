---
title: Mac常用命令
date: 2017-09-15 14:55:03
tags: Mac技巧
categories: macOS
---

macOS常用命令整理,此文记录了平常使用终端的一些基本命令，使用命令行进行操作还是很有成就感的，建议使用Mac的用户可以学习一下一些基本的命令。

<!--more-->

1.man
```
man command-name
eg:
man ls
man -k #search all command
```

2.pwd cd ls
```
ls -la
pwd
cd
```

3.cat less which file
```
cat #check test file
cat a.txt >> b.txt
less #high grade than cat
     #spacekey->paging
     #/ search
     #Q quit
     #v go to vi editor
whicch command-name
file filename #check file
```
4.find & mdfind

5.edit file and directory
```
mkdir -p a/b/c/d/e
cp -R <file> a/b/   file --> b/
mv -R <file> a/b/   file --> b/
rm -R directory/file
```

6.vi and nano

7.su and sudo

8.* open .
  * control + c
  * history
  * control + l == clear
