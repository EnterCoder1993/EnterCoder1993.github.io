---
title: JavaScript
date: 2018-04-05 23:50:05
tags: JavaScript
categories: 前端
---

> JavaScript，通常缩写为JS，是一种高级的，解释执行的编程语言。 JavaScript是一门基于原型、函数先行的语言，是一门多范式的语言，它支持面向对象编程，命令式编程，以及函数式编程。 它提供语法来操控文本、数组、日期以及正则表达式等，不支持I/O，比如网络、存储和图形等，但这些都可以由它的宿主环境提供支持。

<!--more-->

# JavaScript笔记(一)

## JavaScript简介

> JavaScript和ECMAScript通常都被人们用来表达相同的含义，但JavaScript的含义却比ECMA-262中规定的要多的多。

完整的JavaScript实现由三个不同的部分组成

* 核心(ECMAScript)
* 文档对象模型(DOM)
* 浏览器对象模型(BOM)

![javascript](https://ws4.sinaimg.cn/large/0069RVTdgy1fuqvork5jhj308303bmwy.jpg)

### ECMAScript

> ECMAScript是一种由Ecma国际（前身为欧洲计算机制造商协会）通过ECMA-262标准化的脚本程序设计语言。 这种语言在万维网上应用广泛，它往往被称为JavaScript或JScript，但实际上后两者是ECMA-262标准的实现和扩展。

ECMA-262规定了ECMAScript语言的组成部分:

* 语法
* 类型
* 语句
* 关键字
* 保留字
* 操作符
* 对象

ECMAScript就是对实现该标准的各个方面内容的描述。JavaScript实现了ECMAScript，Adobe ActionScript同样也实现了ECMAScript。

#### 什么是ECMAScript兼容

### 文档对象模型(DOM)

文档对象模型(DOM，Document Object Model)是针对XML但经过扩展用于HTML的应用程序编程接口(API,Application Progrmaming Interface)。DOM把整个页面映射为一个多层节点结构。HTML或XML页面中的每个组成部分都是某种类型的节点，这些节点又包含着不同类型的数据。

```html
<html>
    <head>
        <title>Sample Page</title>
    </head>
    <body>
        <p>Hello World</p>
    </body>
</html>
```

![dom](https://ws1.sinaimg.cn/large/0069RVTdgy1fuqw7plym9j309f09idfo.jpg)

通过DOM创建的这个表示文档的树形图，开发人员可以控制页面的内容和结构。借助DOM提供的API，可以对节点进行删除、添加、替换或修改。

### 浏览器对象模型

浏览器对象模型(BOM，Browser Object Model)可以访问和操作浏览器窗口。开发人员使用BOM可以控制浏览器显示的页面的一部分。从根本上讲，BOM只处理浏览器窗口和框架；但习惯上吧所有针对浏览器的扩展算作是BOM的一部分。比如以下扩展：

* 弹出新浏览器窗口的功能；
* 移动、缩放和关闭浏览器的功能；
* 提供浏览器详细信息的navigator对象；
* 提供浏览器所加载页面的详细信息的location对象；
* 提供用户显示器分辨率详细信息的screen对象；
* 对cookies的支持
* 项XMLHttpRequest和IE的ActiveXObject这样的自定义对象。

## 在HTML中使用JavaScript

### `<script>`元素

使用`<script>`元素可以向HTML页面中插入JavaScript。HTML4.01为`<script>`定义了6个属性：

* async：可选。表示应该立即下载脚本，但不妨碍页面中的其他操作。只对外部脚本文件有效。
* charset：可选。通过src属性指定代码的字符集，大多数浏览器会忽略它的值。
* defer：可选。表示脚本可以延迟到文档完全被解析和显示之后再执行。只对外部脚本文件有效。
* language：已废弃。
* src：可选。表示包含要执行代码的外部文件。
* type：可选。可以看成是language的替代属性；表示编写代码使用的脚本语言的内容类型(也称为MIME类型。))