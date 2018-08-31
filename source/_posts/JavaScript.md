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

使用`<script>`元素的两种方式：嵌入式和外本文件，在使用`<script>`元素嵌入JavaScript代码时，只须魏`<script>`指定type属性。

```javascript
<script type="text/javascript">
    function sayHi(){
        alert("Hi!");
    }
</script>
```

包含在`<script>`元素的代码将从上至下依次解释。

通过`<script>`元素来包含外部JavaScript文件，必须包含src属性。这个属性的值指向外部JavaScript文件的链接。

```javascript
<script type="text/javascript" src="example.js"></script>
```

> 一般外部的JavaScript文件带有.js扩展名。但不是必须的，李兰器不会检查包含JavaScript文件的扩展名。因此，也可以使用JSP、PHP或其他服务器端语言动态生成JavaScript代码。

外部文件example.js将被加载到当前页面中。与解析嵌入式JavaScript代码一样，在解析外部JavaScript文件(包括下载该文件)时，页面的处理会暂时停止。如果是在XHTML文档中，可以省略`</script>`标签。

**带有src属性的`<script>`元素会忽略`<script>`和`</script>`标签内的代码，scr属性也可以包含外部域的JavaScript文件。**

```javascript
<script type="text/javascript" src="http://www.somewhere.com/afile.js"></script>
```

#### 标签的位置

`<script>`元素应该放在页面的`<head>`元素中

```html
<!DOCTYPE html>
<html>
<head>
    <title>Example HTML Page</title>
    <script type="text/javascript" src="example1.js"></script>
    <script type="text/javascript" src="example2.js"></script>
</head>
<body>
    <!-- content -->
</body>
</html>
```

这样意味着必须等到全部的JavaScript代码都被下载、解析和执行完成后才开始呈现页面的内容。若JavaScript代码很多，这将会导致浏览器在呈现页面时出现明显的延迟，因此现代的Web应用程序一般把全部JavaScript引用放在`<body>`元素中页面内容的后面。

```html
<!DOCTYPE html>
<html>
<head>
    <title>Example HTML Page</title>
</head>
<body>
    <!-- content -->
    <script type="text/javascript" src="example1.js"></script>
    <script type="text/javascript" src="example2.js"></script>
</body>
</html>
```

#### 延迟脚本

HTML4.01为`<script>`标签定义了defer属性。这个属性表明脚本在执行时不会影响页面的构造。即脚本会被延迟到整个页面都解析完毕后再运行。浏览器会立即下载，但延迟执行。

```html
    <script type="text/javascript" defer="defer" src="example2.js"></script>
```

延迟脚本并不一定按照顺序执行，因此最好只包含一个延迟脚本。且defer属性只适用于外部脚本文件。HTML5的实现会默认忽略嵌入脚本设置的defer属性。

> 在XHTML文档中，要把defer属性设置为defer="defer"。

#### 异步脚本

HTML5为`<script>`元素定义了async属性。async只适用于外部脚本文件，浏览器会立即下载文件，但标记为async的脚本并不保证按照指定它们的先后顺序执行。

```html
<script type="text/javascript" async src="example1.js"></script>
<script type="text/javascript" async src="example2.js"></script>
```

在以上代码中，第二个脚本可能会在第一个脚本执行前执行。因此要确保两者之间互不依赖。指定async属性目的是不让页面等待两个脚本下载和执行，从而异步加载页面其他内容。异步脚本不要再加载期间修改DOM。

> 在XHTML文档中，要把async属性设置为async="async"。

#### 在XHTML中的用法

XHTML(Extensible HyperText Markup Language，可扩展超文本标记语言)是将HTML作为XML的应用重新定义的一个标准。XHTML代码的规则必HTML要严格得多，而且直接影响嵌入的JavaScript代码是否有效。

### 嵌入代码与外部文件

使用外部文件引入JavaScript代码的优点：

* 可维护性：遍及不同HTML页面的JavaScript会造成维护问题。
* 可缓存：浏览器可以根据具体的设置换轮链接的所有外部JavaScript文件。
* 适应未来：HTML和XHTML包含外部文件的语法是相同的。

### `<noscript>`元素

若浏览器不支持JavaScript时，可以使用`<noscript>`元素显示替代的内容。这个元素可以出现在任何HTML元素(`<script>`元素除外)。包含在`<noscript>`元素的内容只在浏览器不支持脚本或脚本被禁用的情况下再回显示出来。

```html
<!DOCTYPE html>
<html>
<head>
    <title>Example HTML Page</title>
    <script type="text/javascript" src="example1.js"></script>
    <script type="text/javascript" src="example2.js"></script>
</head>
<body>
    <!-- content -->
    <noscript>
        <p>本页面需要浏览器支持(启用)JavaScript。
    </noscript>
</body>
</html>
```
