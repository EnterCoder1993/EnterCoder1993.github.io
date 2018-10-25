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

* HTML声明标签`<!DOCTYPE>`
    * 定义与用法
        * `<!DOCTYPE>`必须是HTML文档的第一行
        * `<!DOCTYPE>`声明不是HTML标签，它是指示web浏览器关于页面使用哪个浏览器版本进行编写的指令
        * 
    * 各个版本的声明
        * HTML5 `<!DOCTYPE HTML><meta charset="utf-8">`
        * HTML4.01
* 内链样式表
    * 格式：`<body style="backgroudcolor:green;font-size:20px"></body>`
* 嵌入式样式表
    * 语法格式：`<style type="text/css"></style>`
    * 样式放在<head></head>中
* 引入式样式表
    * 语法格式：`<link rel="stylesheet" type="text/css" href="style.css">`

## 定义样式表

* HTML标记定义
    * `<p>...</p>`
    * p{属性1:属性值;属性2:属性值}
    * p可以叫做选择器，定义标记中的内容执行其中的样式

* Class定义
    * 格式：`<p class="p">...</p>`
    * class选择器是以"."开始的
    * `.p{属性1:属性值;属性2:属性值}`
* ID定义
    * 唯一选择器
    * 格式：`<p id="p">...</p>`
    * ID选择器是以"#"开始的
    * `#p{属性1:属性值;属性2:属性值}`
* 优先级问题
    * ID > CLASS > HTML
    * 同级时选择离元素最近的一个
* 组合选择器(同时控制多个元素)
    * 选择器组合可以使用"."隔开
    * 例如：`h1,h2,h3 {color:red;font-size:14px}`
* 伪元素选择器
    * a:link -- 正常连接的样式
    * a:hover -- 鼠标放上去的样式
    * a:active -- 选择链接时的样式
    * a:visited -- 已经访问过的链接的样式

> CSS注释：/* 注释内容 */

## 常见属性

* 颜色属性
    * color属性定义文本的颜色
    * color:green;
    * color:#ff6600(简写：color:#f60) -- 红 绿 蓝
    * color:rgb(255,255,255)
    * color:rgba(255,255,255,1)
* 字体属性
    * font-size
        * px
        * %
        * smaller
        * larger
        * inheritt -- 继承父元素
    * font-family
        * 多个字体使用","隔开，若字体不存在则直接使用下一个
    * font-weight -- 字体加粗
        * normal -- 400
        * bold -- 700
        * bolder
        * lighter
    * font-style --字体样式
        * normal
        * italic -- 斜体
        * oblique -- 倾斜
        * inherit -- 继承
    * font-variant -- 小型大写字母显示文本
* 文本属性
    * text-align -- 横向排列
    * line-height -- 文本行高
        * %
        * 数值
    * text-indent -- 首行缩进
        * %
        * 数值
        * inherit 
    * letter-space -- 字符间距
        * normal
        * length(可设置为负值)
        * inherit
    * word-space -- 单词间距
        * normal
        * px
        * inherit
    * direction -- 文本方向
        * ltr
        * rtl
        * inherit
    * text-transform -- 文本大小写
        * capitalize -- 每个单词以大写字母开头
        * uppercase
        * lowercase
        * inherit
* 背景属性
    * 背景颜色background-color
    * 背景图片background-image
        * 格式：`background-image:url(图片路径)`
        * background-image:none
    * 背景重复background-repeat
        * 格式：`background-repeat:repeat`
        * repeat-x
        * repeat-y
        * no-repeat -- 不重复
    * 背景位置background-position
        * 格式：`background-postion:(x) (y)`
        * 垂直方向默认居中
        * right
        * left
        * center
        * top
        * bottom
        * 也可以用数值表示位置

    * 简写方式
        * background:背景颜色 url(图像) 重复 位置
        * 例：`background:#f60 url(image/bg.jpg) no-repeat top center`
* 边框属性
    * border-style -- 边框风格
        * 单独定义某一方向
            * border-bottom-style
            * border-top-style
            * border-left-style
            * border-right-style
        * 边框风格样式属性值
            * none -- 无边框
            * solid -- 直线边框
            * dashed -- 虚线边框
            * dotted -- 点状边框
            * double -- 双线边框
    * border-width
        * 单独定义某一方向
        * 属性值
            * thin
            * medium
            * thick
            * px
            * inherit
    * border-color
        * 单独定义某一方向
        * 属性值
            * rgb
            * rgba
            * 十六进制
            * inherit
        * 属性值的四种情况
            * `border-color:red` -- 上下左右红
            * `border-color:red blue` -- 上下红左右蓝
            * `border-color:blue red blue` 上下蓝左右红
            * `border-color:blue white black red` 
    * 简写方式 `border:solid 2px #f60`
* 列表属性
    * list-style-type -- 标记类型
        * none -- 无标记
        * disc -- 实心圆
        * circle -- 空心圆
        * square -- 实心方框
        * decinal -- 数字
        * ...
    * list-style-position -- 标记的位置
        * inside
        * outside(默认值)
        * inherit
    * list-style-image -- 设置图像列表标记
        * URL
        * none
        * inherit
    * 简写方式：`list-style:square inside url(/image/1.jpg)`