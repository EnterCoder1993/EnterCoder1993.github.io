---
title: git-reset相关用法
date: 2018-09-06 23:24:38
tags: Git
categories: Note
---

# git reset相关用法

* HEAD 当前版本的别名，即当前分支最近的一个提交。
* Index 指下一次提交所包含的文件的集合。
* Working Copy 正在工作的文件集。

## 流程

1. 使用checkout切换分支，HEAD指向当前分支的最近一次commit，当前HEAD、Index和Working Copy中的文件集合是相同的。
2. 对文件执行修改，Git发现文件发生改变，此时Working Copy发生改变。
3. 执行git add，Git将改变的文件集合记录到Index，此时Index的状态与Working Copy的状态相同。
4. 最后执行git commit，Git创建了新的commit，此时HEAD指向新的commit，HEAD、Index和Working Copy一致。

