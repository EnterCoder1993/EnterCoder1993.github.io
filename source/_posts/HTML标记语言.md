---
title: HTML标记语言
date: 2018-03-28 22:38:01
tags: Note
categories: 前端

---

# HTML标记语言基础

> 超文本标记语言(HTML)是一种用于创建网页的标准标记语言

<!-- more -->

![html思维导图](https://ws1.sinaimg.cn/large/e8c3586egy1fpsyefgexxj22210p045m)

> 浏览器：Chrome
> 开发工具：IDEA

## HTML的语法

* 什么是HTML标记语言 --> 表示网页信息的符号标记语言
* 特色：
    * 可以设置文本格式
    * 可以创建列表
    * 可以插入图像和媒体
    * 可以建立表格
    * 超链接

* HTML的标记和他的属性
    * 保存格式
        * `.html`
        * `.htm`
        * `.xhtml`
    * 标记和被标记的内容构建出HTML文档
        * `<标记>内容</标记>`

    * 标记的属性 --> 用来控制内容的显示
        * 格式 `<标记 属性1="属性值" 属性2="属性值">内容</标记>`
        * 例如 `<body bgcolor="red">hello world</body>`
* 语法不区分字母大小写
* 文档注释
    * `<!-- 注释内容 -->`
* 代码格式
* 字符实体
    * 字符实体 --> 在HTML中，某些字符是预留的，例如在HTML中不能使用小于号(<)或大于号(>)，因此想要正确显示预留字符，必须在HTML代码中使用字符实体。
    * 常见字符实体见引用

> 字符实体

## HTML的基本机构

* `<html>`内容`</html>`
    * HTML文档的文档标记，也称为HTML开始标记
    * 功能：这对标记位于网页的最前端和最后端
* `<head>`内容`</head>`
    * HTML文件的头标记，也称为HTML头信息开始标记
    * 功能：用来包含文件的基本信息，例如网页的标记、关键字
    * 可以放`<title></title`、`<meta></meta>`、`<style></style>`等。
    * <head></head>标记内的内容不会再浏览器中显示
* `<title>`内容`</title>`
    * HTML文件的标题标记
    * 功能：网页的主题，显示在浏览器的窗口的左上角
    * `<tilt></title>`中不能包含其他标记
* `<body>`内容`</body>`
    * HTML文档的主体标记
    * 功能：`<body></body>`是网页的主体部分，包含段落、标题、链接等标记。
    * 常见属性：
        * bgcolor -- 设置背景颜色 `<body bgcolor="red"></body>`
        * text -- 设置文本颜色 `<body text="green"></body>`
        * link -- 设置连接颜色 `<body link="blue"></body>`
        * vlink -- 已经访问了的链接颜色 `<body vlink="yellow"></body>`
        * alink -- 正在被点击的链接颜色 `<body alink="red"></body>`
* `<meta>`内容`</meta>`
    * 页面的元信息(meta-information)
    * 功能：提供有关页面的元信息，比如针对搜索引擎和更新频度的描述和关键词
    * 必须属性：content，定义name属性相关的元信息
    * 常见的属性
        * author
        * keywords
        * description
        * others
    * `<meta name="keywords" content="test">`
    * 必须放在head元素里面

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Test HTML</title>
        <meta name="keywords" content="helloworld">
        <meta name="author" content="entercoder1993">
        <meta name="description" content="this is html document">
        <meta name="others" content="i don't know write what">
        <meta charset="UTF-8">
        <link href="index.html" type="text/html">
    </head>
    <body bgcolor="gray" text="red" link="blue" alink="yellow" vlink="orange">
        <h1>hello world</h1>
        <hr>
        <p>hello  my html code</p>
        <a href="www.baidu.com">nihao</a>
        <br>
        <!-- this is annotation -->
        <img src="https://i8.mifile.cn/a1/pms_1527735134.03584233!560x560.jpg">
    </body>
</html>
```

## 文档设置标记

### 格式标记


| 标记 | 名称 | 作用 |
| --- | --- | --- |
| `<br>` | 强制换行标记 | 让图片、文字、表格显示在下一行 |
| `<p>` | 换段落标记 |  |
| `<center>` | 居中对齐标志 | 让段落或者文字相对于父标记居中显示 |
| `<pre>` | 预格式化标记 | 保留预先编排好的格式 |
| `<li>` | 列表项目标记 | 每一个列表使用一个`<li>`标记 |
| `<ul>` | 无序列表标记 | 配置列表项目标记使用 |
| `<ol>` | 有序列表标记 | 可以显示特定序号，有属性值type可以定义显示序号，属性value改变起始值 |
| `<dl>` | 定义型列表标记 | 对列表条目进行简短说明 |
| `<dt>` | 定义型列表标记 | 对列表条目进行简短说明 |
| `<dd>` | 定义型列表标记 | 对列表条目进行简短说明 |
| `<hr>` | 水平割线标记 | 段落间的分割线 |
| `<div>` | 分区显示标记 | 编排一大段HTML段落，也可用于格式化表，科多层嵌套 |

* `<ul>`

```html
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

* `<ol>`

```html
<ol>
    <li></li>
    <li></li>
    <li></li>
</ol>

```

* `<dl><dd><dt>`

```html
<dl>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
</dl>
```

### 文本标记


| 标记 | 名称及作用 |
| --- | --- |
| hn | 标题标记 |
| font | 字体设置标记，size，color，face常用属性 |
| b | 粗字体标记 |
| i | 斜字体标记 |
| sub | 文字下标字体标记 |
| sup | 文字上标字体标记 |
| tt | 打印机字体标记 |
| cite | 引用方式的字体，通常是斜体 |
| em | 表示强调，通常为斜体字 |
| stromg | 表示强调，通常为粗体字 |
| small | 小型字体标记 |
| big | 大型字体标记 |
| u | 下划线字体标记 |

```html

```

## 图像标记

* `<img>`图像标记
    * 使用方法 `<img src="路径/文件名.图片格式" width="属性值" height="属性值" border="属性值" alt="属性值">`
    * 注意
        * `<img>`为单标记
        * 路径或文件名或文件格式错误，将无法加载图片

    * `<img>`标记的属性
        * `src`属性 -- 指定要加载的图片的路径和图片的名称以及图片格式
        * `width`属性 -- 指定图片宽度，单位px，em，cm，mm
        * `height`属性 -- 指定图片的高度，单位px、em、cm、mm
        * `border`属性 -- 指定图标的边框宽度，单位px、em、cm、mm
        * `alt`属性
            * 当图片加载完成，鼠标移动到图片上，显示这个图片指定的属性文字
            * 图像加载失败，使用文字代替图像显示
            * 搜索引擎可以通过这个属性的文字来抓取图片

## 超链接的使用

* `<a>`超链接
    * 基本语法 `<a href="" target="打开方式" name="页面锚点名称">链接文字或图片</a>`
    * 属性
        * href属性 -- 链接地址可以是网页、视频、图片或音乐等
        * target属性
            * _blank -- 在新的窗口打开链接
            * _seif(默认值) -- 在当前窗口打开链接
            * _parent -- 在父窗口中打开页面(框架中使用较多)
            * _top -- 在顶层窗口中打开文件(框架中使用较多)
        * name属性 -- 页面锚点

## 表格

### `<table>`标记

* 基本格式：`<table attr1="value1" attr2="value2" ...>`表格内容`</table>`
* 属性
    * width
    * height
    * border
    * align
    * cellspacing -- 单元格之间的间距，默认2px
    * cellpadding -- 单元格内容与单元格边框的显示距离
    * frame 控制表格边框最外层的四条现况
        * void -- (默认值)无边框
        * above -- 仅有顶部边框
        * below -- 仅有底部边框
        * hsides -- 仅有顶部和底部边框
        * lhs -- 仅有左侧
        * rhs -- 仅有右侧
        * vsides -- 仅有左右侧边框
        * box -- 四个边框
        * border -- 四个边框
    * rules -- 控制是否显示及如何显示单元格之间的分割线
        * none(默认值) -- 无分割线
        * all -- 所有分割线
        * rows -- 仅有行分割线
        * clos -- 仅有列分割线
        * groups -- 尽在行组和列组之间有分割线

### `<caption>`标记

* 表格标题`<caption>`
* `<caption>`属性位于`<table>`属性之后，在`<tr>`属性之前
* align属性
    * top -- 在顶部 
    * bottom -- 在底部
    * left -- 在左部
    * right -- 在右部

### `<tr>`标记

* 定义表格的一行，都是由一对`<tr>`...`</tr>`标记表示你
* 每一行`<tr>`标记可以嵌套多个`<td>`或者`<th>`标记
* 可选属性
    * bgcolor
    * align -- 垂直对齐方式
        * bottom -- 靠顶端对齐
        * top -- 靠底部对齐
        * middle -- 居中对齐
    * vlign -- 水平对齐方向
        * left -- 靠左对齐
        * right -- 靠右对齐
        * center -- 居中对齐

### `<td>`和`<th>`标记

* `<td>`和`<th>`都是单元格的标记，必须嵌套在`<tr>`标签内
* `<th>`是表头标记，通畅位于首行或者首列，`<th>`中的中文默认会被加粗，而`<td>`不会
* `<td>`是数据标记，表示该单元的具体数据
* 属性
    * bgcolor
    * align
    * valign
    * width
    * height
    * rowspan -- 单元格所占行数
    * colspan -- 单元格所占列数

### 练习

1. 表格练习


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>This is Title</title>
</head>
<body>
    <table align="center" width="500px" height="250px" border="1" cellspacing="0px" cellpadding="1px">
        <caption>title</caption>
        <tr bgcolor="gray">
            <th>class</th>
            <th>name</th>
            <th>score</th>
        </tr>
        <tr align="center">
            <td>one</td>
            <td>john</td>
            <td>90</td>
        </tr>
        <tr align="center">
            <td>two</td>
            <td>lili</td>
            <td>90</td>
        </tr>
        <tr align="center">
            <td>three</td>
            <td>jack</td>
            <td>90</td>
        </tr>
    </table>
</body>
</html>
```

2.网页布局练习

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>table</title>
</head>
<body topmargin="0" leftmargin="0" style="font-size: 20px;color: white">
    <table cellspacing="0" cellpadding="0" height="960px" width="960px" border="0" align="center">
        <tr bgcolor="gray" height="90px" align="center">
            <td>头部</td>
        </tr>
        <tr>
            <td>
                <table align="left" bgcolor="yellow" width="30%" height="100%">
                    <tr align="center"><td>
                        网页的左部
                    </td></tr>
                </table>
                <table bgcolor="blue" width="70%" height="100%" align="left">
                    <tr align="center"><td>
                        网页的右部
                    </td></tr>
                </table>
            </td>
        </tr>
        <tr bgcolor="red" height="90px" align="center">
            <td>底部</td>
        </tr>
    </table>
</body>
</html>
```

## HTML框架


* 框架将浏览器划分成不同的部分，每一部分加载不同的网页，实现在同一浏览器窗口中加载多个页面的效果。
* `<frame>`划分框架标记
* 语法格式`<frameset>...</frameset>`
* 属性
    * cols
        * 使用像素数和%分割左右窗口哦，"*"表示剩余部分
        * 使用"*,*"表示框平均分成两个
        * 使用"*,*,*"表示平均分成三个
    * rows -- 使用像素数和%分割上下窗口，"*,*"表示剩余部分
    * frameborder -- 指定是否显示边框，0不显示，1显示
    * border -- 设置边框的大小，默认5px

* `<frame>子窗口标记
* `<frame>`是一个单标记，该标记必须放在`<frameset>`中使用，在`<frameset>`中设置了几个窗口，就必须使用几个`<frame>`框架，还必须使用src属性指定一个网页
* 属性
    * src -- 加载网页文件的URL地址
    * name -- 框架名称，是链接标记的target所要的参数
    * noresize -- 表示不能调整边框的大小，没有设置时就可以调整
    * scrolling
        * auto 自动出现
        * yes 有
        * no 无
    * frameborder -- 1显示边框，0不显示边框

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<frameset rows="90,*,90" frameborder="1">
    <frame name="top"/>
        <frameset cols="20%,80%">
            <frame name="left" />
            <frame name="right" />
        </frameset>
    <frame name="bottom"/>
</frameset>
</html>
```

## 表单设计


* 表单标记
    * 定义表单的开始位置和结束位置，表单提交时的内容就是`<form>`里的内容
    * 格式：`<form action="服务器端地址(接收表单内容的地址)" name="表单名称" method="post|get">...</form>`
    * 常用属性
        * name -- 表单名称
        * method
            * get -- 表单的内容会附加在URL地址后面，因此限制了提交的内容的长度，不超过8192个字符，不具备保密性
            * post -- 将表单中的数据一并包含在表单主体中，一起传送到服务器中处理，无数据大小限制
        * action -- 表单数据的处理程序的URL地址，为空则使用当前文档的URL地址，不需要使用action属性也要指定其属性为"no"
        * enctype -- 设置表单的资料的编码类似
        * target -- 和超链接的属性类似，用来指定窗口
* 文本域和密码
    * `<input>`标记
        *  语法 `<input type="" name="" value="" size="" maxlength="">`
        *  属性
            *  type
                *  text -- 文本输入域
                *  password -- 密码域
            *  name -- 定义控件的名称
            *  value -- 初始化值
            *  size -- 设置控件的长度
            *  maxlength -- 允许输入的最大的字符数
* 提交、重置、普通按钮
    * 提交 -- `<input type="submit">`
    * 重置 -- `<input type="reset">`
    * 普通 -- `<input type="button">`
* 单选框和复选框
    * 单选框 -- `<input type="radio">`
    * 复选框 -- `<input type="checkbox`>
    * 注意：两者都可以使用"checked"属性设置默认值
* 隐藏域
    * 隐藏域 -- `<input type="hidden">`
* 多行文本域
    * 使用`<textaera>`可以实现一个可以输入多行文本的区域
    * 语法格式：`<textaera name="" rows="" cols="" value="">...</textaera>`
* 菜单下拉列表域
    * 使用`<select>`标记实现菜单下拉域
    * 语法格式：`<select name="" size="value" multiple><option value="" selected>选项1</option><option value="value2">选项2</option></select>`