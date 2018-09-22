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
* b 向上移动到单词词首(包含标点符号)
* B 空白字符分割的上词词首
* O 开始新的一行
* ^ 当前行的第一个非空字符
* $ 到 行尾
* gg 第一行
* gd 
* [N]G 第N行行首
* fx 
* ;
* tx
* Fx
* ) 到句首
* ( 到句尾
* } 到段首
* { 到段尾
* \*
* `.
* 智能移动
* 书签

# 插入模式

* i 在光标之前插入
* I 行尾插入
* a 在光标之后插入
* A 行首插入
* o 当前行下插入一空行
* O 当前行上插入一空行
* Esc 返回模式选择
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
* u 撤销改动
* ctrl - r 重做
* . 重复上一命令
* ~
* g~iw
* gUiw
* guiw
* \>\>
* <<
* == 

# 剪切和复制

* dd 删除一行
* dw 删除一个单词
* x 删除当前光标下的字符
* X 删除当前光标左边的字符
* D 删除到行尾的内容
* yy 复制一行
* nyy 复制n行
* yw
* y$
* p 粘贴到光标之前
* P 粘贴到光标之后
* ]p
* "a
* d 剪切

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
