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

特点

1. 可以设置文本的格式，比如标题、字号、文本颜色、段落等等
2. 可以创建列表
3. 可以插入图像和媒体
4. 可以建立表格
5. 超链接，可以使用鼠标点击超链接来实现页面之间的跳转

## HTML的语法

HTML文档的保存格式

* .html
* .htm
* xhtml

标记和被标记的内容构建出HTML文档,格式为`<标记>内容</标记>`

标记的属性是用来控制内容(图像、文本等的)如何的显示，格式为

```html
<标记 属性1=属性值 属性2=属性值 ......>内容</标记>
```

语法不区分字母大小写

代码注释使用"\<!-- 注释内容 -->",代码格式使用空格和回车(在网页中不起作用)进行编排，以“TAB”键进行缩进。

* 字符实体

```html
 ---------------------空格----------  &nbsp; ----------&#160;
<--------------------小于号---------- &lt;---------- &#60;
>--------------------大于号---------- &gt;---------- &#62;
&--------------------和号---------- &amp;---------- &#38;
"--------------------引号---------- &quot; ---------- &#34;
'--------------------撇号---------- &apos; (IE不支持)---------- &#39;
￠--------------------分---------- &cent;---------- &#162;
£--------------------镑---------- &pound;---------- &#163;
¥--------------------日圆---------- &yen;---------- &#165;
€--------------------欧元---------- &euro;---------- &#8364;
§--------------------小节---------- &sect;---------- &#167;
©--------------------版权----------&copy;---------- &#169;
®--------------------注册商标---------- &reg;---------- &#174;
™--------------------商标---------- &trade;---------- &#8482;
×--------------------乘号---------- &times;---------- &#215;
÷--------------------除号---------- &divide;---------- &#247;
```

## HTML的基本结构

```html
<!DOCTYPE html>
<html>
    <head>
        <title></title> 
        <meta name="keywords" content="hello world"> 
        <meta charset="UTF-8">
                                //页面的元信息，提供有关页面的元信息，针对搜索引擎和更新频度的描述和关键词
                                //必须的属性 content=some_text
                                //常见属性 author keywords description others
                                //meta标记必须放在head元素里面
    </head>
    <body>

        //网页的主体标记，可以包含段落、标题、回车、横线等标记
        //常见属性 bgcolor text link vlink alink

    </body>
</html>
```

## 文档设置标记

### 格式标记

`<br>` 换行标记
`<p>` 段落标记
`<center>` 居中标记
`<pre>` 预格式化标记
`<li>` 列表项目标记
`<ul>` 无序列表标记
`<ol>` 有序列表标记

```html
<ol type="1">
    <li type="A"></li>
    <li type="a"></li>
    <li type="a"></li>
    <li type="I"></li>
    <li type="i"></li>
</ol>
```

`<dl><dt><dd>` 定义型列表
`<hr>` 水平分割线
`<div>` 分区标记，也称为层标记

### 文本标记

1. hn 标题标记
2. font 字体设置标记
3. sub 下标字体标记
4. sup 上标字体标记
5. tt 打印机字体标记
6. cite 引用方式的字体，通常是斜体
7. b strong 粗体字体标记
8. i em 斜字体标记
9. small 小型字体标记
10. big 大型字体标记
11. u 下划线字体标记

## 图像标记

使用方法

```html
<img src="路径/文件名.图片格式 " width="属性值" height="属性值" border="属性值" alt="属性值">
//src属性 指定我们要加载的图片的路径和图片的名称以及图片格式
//width属性 指定图片的宽度，单位px、em、cm、mm
//height属性 指定图片的高度，单位px、em、cm、mm
//border属性 指定图标的边框宽度，单位px、em、cm、mm
//alt属性 1.当网页上的图片被加载完成后，鼠标移动到上面去，会显示这个图片指定的属性文字 
        //2.如果图像没有下载或者加载失败，会用文字来代替图像显示
        //3.搜索引擎可以通过这个属性的文字来抓取图片
```

* 注意

1. img为单标记，不需要使用\</img>闭合
2. 加载图片时，文件路径或者文件名文件格式错误，将无法加载图片

## 超链接的使用

```html
<a href="" target="打开方式" name="页面锚点名称">链接文字或者图片</a>
//target属性 _blank 新窗口打开链接
//          _self() 当前窗口打开链接
//          _parent 父窗口打开链接
//          _top 顶层窗口打开链接
//name属性 制定页面的锚点名称
```

## 表格

### table标记

```html
<table
    width="" //px or %
    height="" //px or %
    border="" //外边框的宽度
    align""   //left or center or right,default=left 
    cellspacing="" //单元格之间的间距，默认是2px
    cellpadding="" //单元格内容与边框的现实距离
    frame=""       //控制表格边框最外层的四条线框 void above below hsides lhs rhs vsides box border       
    rules=""       //控制是否显示以及如何显示单元格之间的分割线 none all rows clos groups
    >表格内容</table>
```

### caption标记

表格需要使用表格时，可以使用`<caption>`标记，caption属性位于table属性之后，tr属性之前。

属性值

* top
* bottom
* left
* right

### tr标记

定义表格的一行，每一行tr标记可以嵌套多个td或th标记

属性

* bgcolor
* align 设置垂直方向对齐方式
    * bottom
    * top
    * middle
* valign 设置水平方向对齐方式
    * left
    * right
    * center

### td和th标记

th是表头标记，通常 位于首行或首列，th中的文字默认会被加粗，而td不会

td是数据标记，表示该单元的具体数据

属性值

* bgcolor
* align
* valign
* width
* height
* rowspan 设置单元格所占行数
* colspan 设置单元格所占列数

## HTML框架

框架将浏览器划分成不同的部分，每一部分加载不同的网页，实现在同一浏览器窗口中加载多个页面的效果

frameset标记

```html
<frameset cols="*,* or px or %" frameborder="0 or 1" border="5px(default)">
    <frame src="" name="" noresize="noresize" //表示不能调整框架的大小，没有设置时就可以调整
    scrolling="auto or yes or no" frameborder="1 or 0">
    <frame>
</frameset>
```

## 表单设计

### 表单标记

```html
<from actoin="服务器端地址" method="post|get" enctype="" target="">
    //post:post方式提交时，将表单中的数据一并包含在表单主体中，一起传送到服务器中处理，没有数据大小限制
    //get:get方式提交时，会将表单的内容附加在URL地址的后面，所以限制了提交的内容的长度，不超过8192个字符，且不具备保密性
    //enctype 设置表单的资料的编码方式
    //指定目标窗口打开方式
</from>
```

### 文本域和密码

```html
<input
type="" //text|password
name=""
value=""
size=""
maxlength="">
```

### 提交、重置和普通按钮

```html
<input
    type="submit"
    type="reset"
    type="button"
>
```

### 单选框和复选框

```html
<input
    type="radio"
    //使用checked属性来设置默认选中项
>
<input
    type="checkbox"
    //使用checked属性来设置默认选中项
>
```

### 隐藏域

当type为hidden时为隐藏表单域

### 多行文本域

```html
使用<textarea>标记可以实现一个能够输入多行文本的区域
<textarea name="" rows="" cols="" value="">

</textarea>
```

### 菜单下拉列表域

```html
<select name="" size="" mulitple> //设置多选
    <option value="" selected>选项1</option> //给选项赋值，指定传送到服务器上面的值，selected设置默认选中项
    <option>选项2</option>
    <option>选项3</option>
</select>

```