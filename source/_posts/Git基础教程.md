---
title: Git基础教程
date: 2017-09-12 20:53:47
tags: Git
categories: Note
---

# Git基础教程

Git学习笔记,此文记录一些常用Git命令，熟练使用Git应该是开发者必须要掌握的一门技术。

<!--more-->

## 安装git和初始化

### 安装

```bash
$brew install git
```

### 用户名和邮箱设置

```bash
$git config --global user.name "yourname"
$git config --global user.email "email@example.com"
```

### 添加SSH到github

1. 生成本地ssh-key

    ```bash
    $ssh-keygen -t rsa -code "youremail@example"
    ```

2. 打开主目录中的id_rsa.pub文件

    ```bash
    $vim /User/用户名/.ssh/id_rsa.pub
    ```

3. 添加ssh-key到github-settings-SSH and GPG keys

### 测试

```bash
$ssh -T git@github.com
Hi entercoder1993! You've successfully authenticated, but GitHub does not provide shell access.
```

## 创建版本库

### 初始化

```bash
$git clone <url> #克隆远程版本库
$git init #初始化版本库
```

### 把文件添加到仓库，可以添加一个或多个

```bash
$git add <-A/--all>
```

### 把文件提交到仓库，可以一次提交多个文件

```
git commit -m "message"
```

### 查看仓库的状态

```
git status
```

### 查看文件修改内容

```bash
$git diff
```

### 查看提交历史记录

```bash
$git log <--pretty=oneline>
```

### 在Git中，HEAD表示当前版本，上一个版本就是HEAD^，上上个版本就是HEAD^^

### 使用`git reflog`可以记录每一次的命令

### 工作区 本地目录

* 版本库 .git中包含index、master和指针HEAD
* 暂存区(index) git add -->暂存区
* master分支 git commit -->master

### 查看工作区与版本库的区别

```
git diff HEAD -- <file> #如果修改之后没有git add到暂存区，使用git commit就不会将修改提交到master中
```

### 如果要丢弃工作区的修改，可以使用

```
git checkout -- <file> #即文件在工作区的修改全部撤销，撤销后文件会回到最后一次git commit或git add的状态
```

### `git reset HEAD <file>`可以把暂存区的修改撤销，重新放回工作区

### 删除一个文件

```bash
$git rm <file>
```

## 远程版本库

登陆后再右上角找到Create a new repo，创建一个新的远程仓库，填入对应的仓库名称

```bash
$git remote add origin git@github.com:<name>/<reponame>.git
$git push -u origin master #第一次推送master分支的所有内容
$git push origin master    #后续使用此命令极客推送
```

## 分支管理

### 创建与合并

1. 查看分支 `git branch`
2. 创建分支 `git branch <name>`
3. 切换分支 `git checkout <name>`
4. 创建+切换分支 `git checkout -b <name>`
5. 合并某分支到当前分支 `git merge <name>`
6. 删除分支 `git branch -d <name>`

### 解决冲突

在分支中的修改与master中的修改冲突时，使用`git merge`合并时会存在冲突，可以使用`git status`查看冲突，并需要到修改的文件中解决冲突，解决完成后再进行add&commit就可以解决分支中的冲突问题，解决完成后就可以使用`git branch -d <name>`删除冲突，也可以使用`git log --graph`查看分支的合并情况。

### 分支管理策略

合并分支时，Git会使用Fast forward模式，这种模式，删除分支后，会丢掉分支信息，如果禁用Fast forwar模式，Git就会在merge时生成一个新的commmit，这样就可以在分支历史中看出分支信息。

```bash
$git merge --no-ff -m "message" <baranchname>
```

### bug分支

若master分支出现bug，需要及时修改，我们可以使用`git stash`把目前修改的分支储存起来，然后将分支切换到出现bug的分支，并创建bug分支，解决完成后，使用

```bash
$git stash list   #查看分支存储信息
$git stash apply  #恢复储存信息，但stash的内容不删除
$git stash drop   #将储存信息删除
$git stash pop    #恢复的同事删除储存信息
```

### Feature分支

未被合并的分支，需要删除分支的，使用`git branch -D <branchname>`

### 多人协作

使用`git remote`查看远程仓库的信息加上-v可以查看详细信息

### 推送分支

将本地分支的所有提交提交到远程库，推送时要指定本地分支，这样git就会把该分支推送到远程库对应的分支上

```bash
$git push origin master
$git push origin dev
```

### 抓取分支

1. 查看远程库信息，使用`git remote -v`
2. 从本地推送分支，使用`git push origin branchname`
3. 若推送失败，先用`git pull`抓取远程的新提交
4. 在本地创建和远程分支对应的分支，使用`git checkout -b branchname origin/branchname`本地和远程分支的名称最好一致
5. 建立本地分支与远程分支的关联，使用`git branch --set-upstream branchnanme origin/branchname`
6. 从远程抓取分支，使用git pull，如果有冲突，要先才处理冲突

## 标签管理

虽然可以使用commit id来退回版本，但是并不好找，所以使用tag标记为容易记住的有意义的名字，跟某个commit绑定在一起

### 创建标签

`git tag <name>`用于新建一个标签，默认为HEAD，也可以指定一个commit id
`git tag -a <tagname> -m "message"`可以指定标签信息
`git tag -s <tagname> -m "message"`可以用PGP签名标签
`git tag`可以查看所有标签

### 操作标签

`git push origin <tagname>`可以推送一个本地标签
`git push origin --tags`可以推送全部未推送过的本地标签
`git tag -d <tagname>`可以删除一个本地标签
`git push origin :refs/tags/<tagname>`可以删除一个远程标签
