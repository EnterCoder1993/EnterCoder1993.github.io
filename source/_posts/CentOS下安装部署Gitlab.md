---
title: CentOS下安装部署Gitlab
date: 2019-04-17 17:00:35
tags: 
---


# Gitlab简介

> GitLab是一个开源的git仓库管理平台,方便团队协作开发和管理.在GitLab上可以实现完成的CI(持续集成)和CD(持续发布).而且还提供了免费使用的社区版本(https://gitlab.com/gitlab-org/gitlab-ce)

官网:[https://about.gitlab.com](https://about.gitlab.com)

# 搭建环境


| 工具/环境 | 版本 |
| --- | --- |
| Linux Server | CentOS 7 |
| GitLab | 11.9.8 |

# 准备工作

## 安装基础依赖

```bash
#安装技术依赖
sudo yum install -y curl policycoreutils-python openssh-server

#启动ssh服务&设置为开机启动
sudo systemctl enable sshd
sudo systemctl start sshd
```

## 安装Postfix

Postfix是一个邮件服务器,Gitlab发送邮件需要用到

```bash
#安装postfix
sudo yum install -y postfix

#启动postfix并设置为开机启动
sudo systemctl enable postfix
sudo systemctl start postfix
```

## 开放ssh以及http服务(80端口)

```bash
#开放ssh、http服务
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --add-service=http --permanent

#重载防火墙规则
sudo firewall-cmd --reload
```

# 部署安装

本次安装部署的士社区办:gitlab-ce,如果要部署商业版可以把关键字替换为:gitlab-ee

## Yum安装GitLab

* 添加GitLba社区版Package

```bash
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash

```

* 安装GitLab社区版

```bash
sudo yum install -y gitlab-ce
```

安装成功后可以看到终端输出GitLab的Logo

## 配置GitLab站点Url

* GitLab默认的配置文件路径是`/etc/gitlab/gitlab.rb`
* 默认的站点Url配置项是:`external_url 'http://gitlab.example.com'`

根据需求修改站点URL配置.

修改完成后需要在终端输入一下命令使配置生效

```bash
sudo gitlab-ctl reconfigure
```

# 启动访问

启动GitLab的终端命令为

```bash
#启动
sudo gitlab-ce start
#停止
sudo gitlab-ce stop
```

> 注:查看GitLab版本号:`cat /opt/gitlab/embedded/service/gitlab-rails/VERSION`


参考:[CentOS 7 下 GitLab安装部署教程](https://ken.io/note/centos7-gitlab-install-tutorial)
