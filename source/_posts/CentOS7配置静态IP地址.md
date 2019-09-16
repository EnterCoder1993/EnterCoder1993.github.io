---
title: CentOS7配置静态IP地址
date: 2018-09-12 23:43:15
tags: [Linux,Network]
categories: Note
---

# CentOS 7 配置静态IP地址

<!--more-->

1. 切换到网卡列表目录

    ```bash
    $cd /etc/sysconfig/network-scripts/
    ```

![network](https://ws4.sinaimg.cn/large/0069RVTdgy1fv76u0bmesj30nn08o3zi.jpg)

一般第一个就是你的网卡，若是服务器，可能会有多个以ifcfg-em开头的网卡，分别对应服务器的网卡接口，在这里我的网卡为`ifcfg-eth0`

2. 编辑网卡

    ```bash
    $vi ifcfg-eth0

    BOOTPROTO=none
    ONBOOT=yes
    # IP地址
    IPADDR=102.168.1.100
    # 子网掩码
    PREFIX=24
    # 网关地址
    GATEWAY=192.168.1.1
    # 设置DNS地址
    DNS1=202.96.134.133
    DNS2=8.8.8.8
    ```

![ipconfig](https://ws2.sinaimg.cn/large/0069RVTdgy1fv7739ctbgj30fn0enwf8.jpg)

退出vi，使用`:wq`命令

3. 保存退出，重启网络服务

    ```bash
    $service network restart
    ```

若成功，则出现如下提示
![success](https://ws2.sinaimg.cn/large/0069RVTdgy1fv77633a05j30of01kgll.jpg)