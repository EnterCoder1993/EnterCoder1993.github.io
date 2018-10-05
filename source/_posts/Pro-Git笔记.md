---
title: Pro-Git笔记
date: 2018-09-08 21:21:02
tags: Git
categories: Note
---

# Pro Git学习笔记

## 目录

- [Git简介](#Git简介)
- [安装Git](#安装Git)
- [初次运行Git前的配置](#初次运行Git前的配置)
- [Git基础](#Git基础)
- [Git分支](#Git分支)

## Git简介

1. 直接记录快照，而非差异比较
2. 近乎所有操作都是本地执行
3. Git保证完整性
4. Git一般只添加数据
5. 三种状态
    * **以提交** -- 已提交表示数据已经安全的保存在本地数据库中
    2. **已修改** -- 修改了文件，但还没保存到数据库中
    3. **已暂存** -- 对一个已修改的文件的当前版本做了标记，使之包含在下次提交的快照中。
6. 工作区域
    * **Git仓库** -- 用来保存项目的元数据和对象数据库的地方，从其他计算基金克隆仓库时，拷贝的就是这里的数据
    2. **工作目录** -- 对项目的某个版本独立提取出来的内容。这些从 Git 仓库的压缩数据库中提取出来的文件，放在磁盘 上供你使用或修改。
    3. **暂存区域** -- 暂存区域是一个文件，保存了下次将提交的文件列表信息，一般在 Git 仓库目录中。 有时候也被称作`‘索 引’'，不过一般说法还是叫暂存区域。![](https://ws1.sinaimg.cn/large/0079wTXjgy1fsmpcjuov0j30jz0b1taa)

  
## 安装Git
* Linux上安装

```bash
$sudo yum install git
    
$sudo apt-get install git
```

* Mac上安装
安装Xcode Command Line Tools

* Windows上安装
[Git官网](git-scm.com/download/win)

* 源代码安装
从源码安装Git，需要安装Git以来的库：curl、zlib、openssl、expat和libiconv

```bash
$sudo yum install curl-devel expat-devel gettext-devel \ openssl-devel zlib-devel 
$sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext \ libz-dev libssl-dev
```
为了能够添加更多格式的文档（如 doc, html, info），你需要安装以下的依赖包：

```bash
$sudo yum install asciidoc xmlto docbook2x 
$sudo apt-get install asciidoc xmlto docbook2x
```
[下载Git的tar包](https://www.kernel.org/pub/software/scm/git)

```bash
$tar -zxf git-2.0.0.tar.gz 
$cd git-2.0.0 $ make configure $ ./configure --prefix=/usr 
$make all doc info 
$sudo make install install-doc install-html install-info
```
使用Git来获取Git的升级

```bash
$git clone git://git.kernel.org/pub/scm/git/git.git
```

## 初次运行Git前的配置
### 三个配置变量
每一个级别覆盖上一级别的配置
1. `/etc/gitconfig` 文件: 包含系统上每一个用户及他们仓库的通用配置。 如果使用带有 --system 选项的 git config 时，它会从此文件读写配置变量。
2. `~/.gitconfig` 或 ~/.config/git/config 文件：只针对当前用户。 可以传递 --global 选项让 Git 读写此文件。
3. `.git/config` 当前使用仓库的 Git 目录中的 config 文件（就是 .git/config）：针对该仓库。

> 在Windows 系统中，Git 会查找 $HOME 目录下（一般情况下是 C:\Users\$USER）的 .gitconfig 文件。 Git 同样也会寻找 /etc/gitconfig 文件，但只限于 MSys 的根目录下，即安装 Git 时所选的目标位置。

### 用户信息和文本编辑器
设置用户名称和邮件地址，因为每一个Git的提交都会使用这些信息，并且会写入到你的每一次提交中，不可更改：

```bash
$git config --gloabl user.name "username"
$git config --global user.email "user email"
$git config --global core.editor emacs
//default vim
```
> 如果使用了 --global 选项，那么该命令只需要运行一次，因为之后无论你在该系统上做任何事 情， Git 都会使用那些信息。 
> 当你想针对特定项目使用不同的用户名称与邮件地址时，可以在那个项目目录下运 行没有 --global 选项的命令来配置。

检查配置信息

```bash
$git config --list
//check someone
$git config <key>
```

### 获取帮助
Git命令使用手册

```bash
$git help <verb>
$git  <verb> --help
$man git-<verb>
```
config命令手册

```bash
$git help config
```

## Git基础

### 获取Git仓库

1. 在现有项目或目录下导入所有文件到Git中

    ```bash
    $git init
    ```

    使用该命令后将创建一个.git的子目录，子目录中含有初始化Git仓库中所有的必须文件，这些文件是Git仓库的骨干。

    .git文件夹中包含的文件信息：

    初始化仓库以后，使用`git add .`跟踪文件。可以通过`git add <file>`实现对指定文件的跟踪，然后执行`git commit`提交。

2. 从服务器克隆一个现有的Git仓库

    ```bash
    $git clone [git-url]
    ```

    git支持多种数据传输协议
    * `https://`协议
    * `git://`协议
    * `SSH`协议 `user@server:path/to/repo.git`

### 记录每次更新到仓库

![state](https://ws1.sinaimg.cn/large/0079wTXjgy1fsns4c405fj30n509rwfp)

工作目录下的每个文件都只有两种状态：已跟踪或未跟踪。

* 已跟踪的文件是指那些被纳入了版本控制的文件

* 工作目录中除了已跟踪的文件以外的所有其他文件都属于未跟踪文件

状态：
1. 新建文件`README`(未跟踪状态)
2. `git add README`跟踪README文件(暂存状态)
3. 修改已跟踪文件`CONTRIBUTING.md`(修改状态，但还未添加到暂存区，要暂存文件更新，使用`git add CONTRIBUTING.md`暂存文件更新)

* 检查当前文件状态

    ```bash
    $git status
    ```

* 跟踪新文件

    ```bash
    $git add [file]
    ```

* 暂存已修改文件

    ```bash
    $git add [file]
    ```
    
* 状态简览

    ```bash
    $git status -s/--short
    ```

    使用`git status -s`显示简短的状态信息
    * 新添加的未跟踪文件前面为`??`标记
    * 新添加到暂存文件前面有`A`标记
    * 修改过的文件前面为`M`标记

* 忽略文件

    创建一个名为`.gitignore`的文件，列出药忽略的文件模式。
    
    ```bash
    $cat .gitignore 
    # 忽略所有以.o或.a结尾的文件
    *.[oa] 
    # 忽略所有以~结尾的文件
    *~
    ```
    
    `.gitignore`的格式规范如下：
    * 所有空行或者以 `＃` 开头的行都会被 Git 忽略。
    * 可以使用标准的 `glob` 模式匹配。
    * 匹配模式可以以（`/`）开头防止递归。
    * 匹配模式可以以（`/`）结尾指定目录。
    * 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（`!`）取反。
    
    glob模式是指shell所使用的简化了的正则表达式。

    * 星号（\*）匹配零个或多个任意字符；
    
    *  [abc]匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c)；

    * 问号（? ）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配 （比如 [0-9] 表示匹配所有 0 到 9 的数字）。 

    * 使用两个星号（\*) 表示匹配任意中间目录，比如\`a/**/z\` 可以匹 配 a/z, a/b/z 或 \`a/b/c/z\`等。
    
    > [.gitignore文件列表](https://github.com/github/gitignore)
    
* 查看已暂存和未暂存的修改

    ```bash
    $git diff
    # 若要查看已暂存的将要添加到下次提交里的内容，可以使用git diff --cached(git diff --staged)命令。
    ```

    > 使用`git diff`分析文件差异，也可以通过图形化的方式或其他格式输出，可以使用`git difftool`命令来用Araix，emerge或vimdiff等软件输出diff分析结果。

* 提交更新

    运行提交命令`git commit`前，应先用`git status`查看文件是否都是暂存状态，若文件还不是暂存状态，要用`git add`将修改或新添加的文件添加到暂存区，否则提交的时候不会记录这些还没暂存起来的变化。

    ```bash
    $git commit -m "message"
    ```

    > 提交记录的是暂存区域的快照。任何还未暂存的仍然保持已修改状态，可以在下次提交时纳入版本管理。每一次运行提交操作，都是对项目做一次快照。以后可以回到这个状态或进行比较。

* 跳过使用暂存区域

    给`git commit`加上`-a`选项，Git就会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过`git add`步骤。

* 移除文件

    要从Git中移除某个文件，就必须要从已跟踪文件清单中移除(即从暂存区域移除)，然后提交。

    ```bash
    $git rm PROJECT.md
    ```

    下次提交时，该文件就不再纳入版本管理中，如果要删除之前修改并且已经放到暂存区域的话，则必须使用强制删除选项`-f`。

    若想让文件保留在目录中，但不希望Git继续跟踪。可以添加`--cached`选项。

    ```bash
    $git rm --cached README
    ```
    
    也可以使用glob模式

    ```bash
    # 该命令删除log目录下扩展名为.log的所有文件
    $git rm log/\*.log
    ```

* 移动文件

    使用`git mv`命令，也可以对文件进行重命名

    ```bash
    $git mv file_from file_to
    ```

    运行`git mv`相当于运行了下面三条命令，不过Git会意识到这是一次改名。

    ```bash
    $mv README.md README
    $git rm README.md
    $git add README
    ```

### 查看提交历史

使用`git log`命令可以查看提交历史记录。默认会按提交时间列出所有更新，最近的更新在最上面。

`-p`选项用来显示每次提交内容的差异。使用`-num`可以显示最近num次提交的记录。

```bash
$git log -p --stat -2
```

添加`-stat`选项可以返回每次提交的简略的统计信息。另一个常用的选项是`--pretty`(oneline，short，full，fuller)，这个选项可以指定使用不同于默认格式的方式展示提交历史。`format`可以定制要显示的记录格式。`--graph`可以形象地展示分支、合并历史。

```bash
$git log --pretty=format:"%h - %an, %ar : %s" --graph
586f3df - entercoder1993, 34 hours ago : update note of git
0c17bed - entercoder1993, 6 days ago : update spider of python
a0fe9fc - entercoder1993, 7 days ago : add data analysis of python
```

`format`常用选项

![format](https://ws1.sinaimg.cn/large/006tNbRwly1fvv7fct89zj30kt0d1dil.jpg)

`git log`的常用选项表格

| 选项            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| -p              | 按补丁格式显示每个更新之间的差异                             |
| --stat          | 显示每次更新的文件修改统计信息                               |
| --shortstat     | 只显示—stat中最后的行数修改添加移除统计                      |
| --name-only     | 仅在提交信息后显示已修改的文件清单                           |
| --abbrev-commit | 仅显示SHA-1的前几个字符                                      |
| --relative-date | 使用较短的相对时间显示                                       |
| --graph         | 显示ASCII图形表示的分支合并历史                              |
| --pretty        | 使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。 |
| --name-status   | 显示新增、修改、删除的文件清单                               |

### 撤销操作

运行带有`--amend`选项的提交命令会将暂存区中的文件提交。如果上次提交以来未做任何修改，则修改的只是提交信息。

* 取消暂存的文件

    使用`git reset HEAD <file>`可以用来取消暂存。

* 取消对文件的修改

### 远程仓库的使用

> 远程仓库是指托管在因特网或其他网络中的项目版本库。

* 常看远程仓库

    使用`git remote`命令可以查看已经配置的远程仓库服务器，使用`-v`选项会显示需要读写远程仓库使用的Git保存的简写与其对应的URL。

    ```bash
    $git remote -v
    origin	https://github.com/entercoder1993/entercoder1993.github.io.git (fetch)
    origin	https://github.com/entercoder1993/entercoder1993.github.io.git (push)
    ```

* 添加远程仓库

    使用`git remote add <shortname> <url>`可以添加一个新的远程仓库。

* 从远程仓库抓取与拉取

    使用`git fetch <remote-name>`可以从远程仓库中获得数据。它会访问远程仓库，从中拉取所有你还没有的信息。
    如果使用`clone`克隆一个仓库，命令会自动添加为远程仓库并默认一“origin”为简写。
    `git fetch origin`会抓取(或上一次抓取)后新推送的所有工作。但需要手动将其合并到工作中。
    `git pull`会自动的抓取然后合并远程分支到当前分支。

* 推送到远程分支

    `git push <remote-name> <branch-name>`可以将项目推送到远程仓库服务器。只有当你有所克隆服务器的写入权限，并且之前没有人推送过时才可以使用此命令。若有其他人先推送了，则必须先将他们的工作拉取下来并将其合并进你的工作后才能推送。

* 查看远程仓库

    使用`git remote show <remote-name>`可以查看某一远程仓库的更多信息。

## Git分支

### 分支简介

* 创建分支

    ```bash
    $git branch bran-name
    ```
    
* 切换分支

    ```bash
    $git checkout bran-name
    ```
    
* 查看分叉历史

    ```bash
    $git log
    $git log --oneline --decorete --graph --all
    ```
    
### 分支的新建与合并

工作流：
1. 开发某个网站
2. 为实现某个需求，创建一个分支
3. 在这个分支上展开工作

有Bug需紧急处理：
1. 切换到你的线上分支
2. 为紧急任务创建一个新的分支，并修复它
3. 测试通过后，切换回线上分支，合并这个修补分支，最后将改动推动到线上分支
4. 切换回最初工作的分支，继续工作

* 新建并切换分支

    ```bash
    $git branch bran-name
    $git checkout bran-name
    # 简写
    $git checkout -b bran-name
    ```
    > 切换分支之前，保持干净的状态(提交还未被提交的修改)。也可以保存进度(stashing)和修补提交(commit amending)

* 分支的合并

    ```bash
    $git checkout master
    Switched to branch 'master'
    $git merge bran-name
    ```
    
* 分支的删除

    ```bash
    $git branch -d bran-name
    ```
    
* 遇到冲突时的分支合并









