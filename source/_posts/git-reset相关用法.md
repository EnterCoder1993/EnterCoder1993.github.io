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

## Rest

git reset本质是重置HEAD(当前分支的版本顶端)到另一个commit。假设有有个分支如下：

![branch](https://ws4.sinaimg.cn/large/006tNbRwgy1fv09uav0axj306g0cma9w.jpg)

此时执行`git reset HEAD`任何事情都不会发生，GIT会重置当前分支到HEAD，而这个正是它现在所在的位置。

若执行`git reset HEAD~1`，HEAD将指向上一个commit。若执行`git reset HEAD~2`则HEAD将指向后两个commit如图：

![commit](https://ws1.sinaimg.cn/large/006tNbRwgy1fv09xjd2kvj305s0d1dfo.jpg)

## 参数

### --soft

--soft参数告诉Git重置HEAD到另外一个commit，但此时Index和working copy不会有任何变化。

![soft](https://ws3.sinaimg.cn/large/006tNbRwgy1fv0a2pw4rsj30g103fdfr.jpg)

### --hard

--hard参数将会重置HEAD返回到另一个commit，且index和working copy也将重置。数据因此可能会丢失，若丢失只能只用git reflog。

如果我们希望彻底丢掉本地修改但是又不希望更改branch所指向的commit，则执行git reset --hard = git reset --hard HEAD。

![hard](https://ws2.sinaimg.cn/large/006tNbRwgy1fv0a7whniuj30ly04emwz.jpg)

### --mixed(default)

--mixed是reset的默认参数，它将重置HEAD到另一个commit，并且重置index保持和HEAD相同，但work copy不会改变。

![mixed](https://ws3.sinaimg.cn/large/006tNbRwgy1fv0a7goyh6j30g103a3yf.jpg)

## 总结

--soft 、--mixed以及--hard是三个恢复等级。使用--soft就仅仅将头指针恢复，已经add的缓存以及工作空间的所有东西都不变。如果使用--mixed，就将头恢复掉，已经add的缓存也会丢失掉，工作空间的代码什么的是不变的。如果使用--hard，那么一切就全都恢复了，头变，aad的缓存消失，代码什么的也恢复到以前状态。

## 参考

> 参考：[https://www.cnblogs.com/kidsitcn/p/4513297.html](https://www.cnblogs.com/kidsitcn/p/4513297.html)