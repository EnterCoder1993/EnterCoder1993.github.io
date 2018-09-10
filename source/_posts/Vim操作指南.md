---
title: Vim操作指南
date: 2018-09-10 23:54:00
tags: Vim
categories: Tools
---

# 移动

* hjkl
* ctrl - f 上翻页
* ctrl - b 下翻页
* %
* w 移动到单词前端(包含标点符号)
* W 单词间移动
* e 移动到单词末端(包含标点符号)
* E 移动到单词末端
* b 向上移动到单词前端(包含标点符号)
* B 
* O 开始新的一行
* ^
* $ 到 行尾
* gg
* gd
* [N]G
* fx
* ;
* tx
* Fx
* ) 到句首
* (
* }
* {
* \*
* `.
* 智能移动
* 书签

# 插入模式

* i
* I
* a
* A
* o
* O
* Esc
* 提示
    * ctrl - n
    * ctrl - p

# 编辑

* r
* J
* cc
* cw
* c$
* s
* S
* xp
* u
* ctrl - r
* .
* ~
* g~iw
* gUiw
* guiw
* \>\>
* <<
* == 

# 剪切和复制

* dd
* dw
* x
* X
* D
* yy
* 2yy
* yw
* y$
* p
* P
* ]p
* "a

# 多文件

* :e
* :bn
* :bd
* :sp fn
* ctrl - w
    * ctrl - w s
    * ctrl - w w
    * ctrl - w q
    * ctrl - w v
* :table fn
* gt
* gT
* :tabr
* :tabl
* :tabm [N]

# 搜索/替换

* /pattern
* ?pattern
* n
* N
* :s/old/new/g
* :s/old/new/gc

# 选中模式

* 文本标记
    * v
    * V
    * ctrl - v
    * o
    * U
    * O
    * aw
    * ab
    * aB
    * ib
    * iB
* 命令
    * >
    * <
    * y
    * d
    * ~

# 离开

* :w
* :wq
* :x
* :q
* :q!

# 宏命令

* qa
* q
* @a
