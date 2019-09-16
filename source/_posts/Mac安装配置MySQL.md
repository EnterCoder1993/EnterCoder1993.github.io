---
title: Mac安装配置MySQL
date: 2017-09-05 13:06:24
tags: [MySQL,Mac,Setting]
categories: 
  - [macOS]
  - [数据库]
---

# Mac下安装配置MySQL

Mac下MySQL的安装其实是很简单，用brew一行代码就解决了，但是安装完成后并不能直接开始用，会出现一些错误，此文可以解决安装后无法使用的问题。

<!--more-->

## 安装

使用命令行执行

```bash
$brew install MySQL
```

即可安装完成

<!--more-->

## 配置

1. 命令行输入

    ```bash
    $sudo chown -R 'Mac用户名' /usr/local
    ```

2. 连接

    ```bash
    $brew link --overwrite mysql
    ```

3. 命令行输入

    ```bash
    unset TMPDIR

    $bash mysql_install_db --verbose --user=root
    --basedir="$(brew --prefix mysql)"--datadir=/usr/local/var/mysql --tmpdir=/tmp
    ```

4. 启动mysql

    ```bash
    $mysql.server start
    ```

5. 关闭mysql

    ```bash
    $mysql.server stop
    ```

## 常用Mysql用法

>待补充
