---
title: CSS层叠样式表
date: 2018-03-31 00:39:55
tags: Note
categories: 前端

---

# 层叠样式表

> 层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。

<!-- more -->

![CSS层叠样式表](https://ws1.sinaimg.cn/large/e8c3586egy1fpxkpjnodkj220o28vwuu)

## 使用CSS样式的方式

* 内链样式表

```
<body style="background-color:green; margin:0; padding:0;">

</body>
```

* 嵌入式样式表

```javascript
<head>
    <style type="text/css">

    </style>
</head>
```

* 引入式样式表

```html
<link rel="stylesheet" type="text/css" href="style.css">
```

## 定义样式表

定义方式

* HTML标记定义

```html
<p>...</p>
p{
    属性:属性值;
    属性2:属性值2;
}
//p可以叫选择器，定义那个标记中的内容执行其中的样式
```

* class定义

```html
<p class="a">...</p>
.a {
    属性:属性值;
    属性2:属性值2;
}
```

* id定义

```html
<p id="b">...</p>
#b {
    属性:属性值;
    属性2:属性值2;
}
```

**优先级问题**

id>class>HTML标记

组合选择器

```html
h1,h2,h3,.a,#b {
    属性:属性值;
    属性2:属性值2;
}
```

伪元素选择器

* a:link 正常连接的样式
* a:hover 鼠标放上去的样式
* a:active 选择链接时的样式
* a:visited 已经访问过的链接的样式

## 常见属性

### 颜色

color属性定义文本的颜色

```
color:green
color:#ff6600
color:#f60 //简写式
color:rgb(255,255,255)
color:rgba(255,255,255,1)
```

### 字体

font-size属性定义字体的大小`font-size:14px`

font-family定义字体`font-family:微软雅黑,serif;`使用,隔开,以确保当字体不存在时直接使用下一个

font-family字体加粗`normal|bold|bolder|lighter`,也可以使用100|200|300~900,400=normal,700=bold

### 背景

* 背景颜色`background-color`
* 背景图片`background-image:url(图片路径)|nore`
* 背景重复`background-repeat:repeat|repeat-x|repeat-y|no-repeat`
* 背景位置`background-position:横向(left,center,right)|纵向(top,center,bottom)`

简写方式`background:#f60 url(images/bg,jpt) no-repeat top center`

### 文本

横向排列`text-align:left|center|right`
文本行高`line-height:100%|20`
首行缩进`text-indent:4`
字符间距`letter-spacing:normal|10|inherit`

### 边框

* 边框风格border-style

* 边框宽度border-width

* 边框颜色border-color

简写方式`border:solid 2px #f60

### 列表

* 标记类型list-style-type

```html
none                无标记。
disc                默认。标记是实心圆。
circle              标记是空心圆。
square              标记是实心方块。
decimal             标记是数字。
decimal-leading-zero    0开头的数字标记。(01, 02, 03, 等。)
lower-roman         小写罗马数字(i, ii, iii, iv, v, 等。)
upper-roman         大写罗马数字(I, II, III, IV, V, 等。)
lower-alpha         小写英文字母The marker is lower-alpha (a, b, c, d, e, 等。)
upper-alpha         大写英文字母The marker is upper-alpha (A, B, C, D, E, 等。)
lower-greek         小写希腊字母(alpha, beta, gamma, 等。)
lower-latin         小写拉丁字母(a, b, c, d, e, 等。)
upper-latin         大写拉丁字母(A, B, C, D, E, 等。)
hebrew              传统的希伯来编号方式
armenian            传统的亚美尼亚编号方式
georgian            传统的乔治亚编号方式(an, ban, gan, 等。)
cjk-ideographic     简单的表意数字
hiragana            标记是：a, i, u, e, o, ka, ki, 等。（日文片假名）
katakana            标记是：A, I, U, E, O, KA, KI, 等。（日文片假名）
hiragana-iroha      标记是：i, ro, ha, ni, ho, he, to, 等。（日文片假名）
katakana-iroha      标记是：I, RO, HA, NI, HO, HE, TO, 等。（日文片假名）
```

* 标记位置list-style-position

```
inside 列表项目标记放置在文本以内，且环绕文本根据标记对齐。
outside 默认值。保持标记位于文本的左侧。列表项目标记放置在文本以外，且环绕文本不根据标记对齐。
inherit 规定应该从父元素继承 list-style-position 属性的值。
```

* 设置图像列表标记list-style-image

```
URL 图像的路径。
none 默认。无图形被显示。
inherit 规定应该从父元素继承 list-style-image 属性的值。
```

简写方式list-style:square inside url('/user/hello.jpg');

## DIV+CSS布局

DIV和SPAN在整个HTML标记中，没有任何意义，他们的存在就是为了应用CSS样式,DIV和span的区别在与，span是内联元素，div是块级元素

### **盒模型**

* 盒子外边距 margin
* 盒子内编剧 padding
* 盒子边框宽度 border
* 盒子宽度 width
* 盒子高度 height

### **布局相关属性**

1. position定位方式

    * relative 正常定位
    * absolute 根据父元素定位
    * fixed 根据浏览器窗口定位
    * static 没有定位
    * inherit 继承

2. 定位(离页面顶点的距离)

    * left
    * right
    * top
    * bottom

3. z-index层覆盖先后顺序

4. display显示属性

    * none 层不显示
    * block 块状显示,在元素后面换行,显示下一块元素
    * 内联显示,多个块可以显示在一行内

5. float属性

    * left 左浮动
    * right 右浮动

6. clear属性

    1. clear:both 清除浮动
    2. scroll无论内容是否超出层大小都添加滚动条
    3. auto 超出时自动添加滚动条

7. overflow溢出处理

    hidden隐藏超出层大小的内容

### **兼容问题及高效开发工具**

#### 兼容性测试工具

* IE Tester
* Multibrowser

#### 常用浏览器

* Chrome
* Firefox
* Opera

#### 高效开发工具

1. 轻量级

    * Notepad++
    * Sublime Text

2. 重量级

    * WebStorm
    * Dreamweaver

#### 网页设计工具

* fireworks
* photoshop