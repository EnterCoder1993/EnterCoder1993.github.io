---
title: Python网络爬虫与信息提取
date: 2018-07-01 23:52:36
tags: Python
---

# Python网络爬虫与信息提取

* 文本工具类IDE

  * IDLE — 自带、默认、常用（适用于Python入门）
  * Sublime Text — 第三方专用编程工具

* 集成工具类IDE

  * PyCharm
  * Anaconda & Spyder


<!-- more -->

## Requests库入门

### Request库的安装

终端运行下列命令

```bash
$ pip install requests
```

获得源码

```bash
$ git clone git://github.com/kennethreitz/requests.git
```

也可以下载tarball

```
$ curl -OL https://github.com/requests/requests/tarball/master
```

现在完成后，使用如下命令进行安装

```bash
$ cd requests
$ pip install .
```

简单使用

```python
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code) # 200
r.encoding = 'utf-8'
print(r.text) # baidu的html源码
```



### Requests库的7个主要方法

| 方法                | 说明                                           |
| ------------------- | ---------------------------------------------- |
| requests.requests() | 构造一个请求，支撑一下各方法的基础方法         |
| requests.get()      | 获取HTML网页的主要方法，对应于HTTP的GET        |
| requests.head()     | 获取HTML网页头信息的方法，对应于HTTP的HEAD     |
| requests.post()     | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
| requests.put()      | 向HTML网页提交PUT请求的方法，对应与HTTP的PUT   |
| requests.patch()    | 向HTML网页提交局部修改请求，对应于HTTP的PATCH  |
| requests.delete()   | 向HTML页面提交删除请求，对应于HTTP的DELETE     |

#### Requests库的get()

![屏幕快照 2018-06-30 上午12.06.26](https://ws4.sinaimg.cn/large/006tKfTcgy1fsshyc4nm3j30g106vtdz.jpg)

* 使用方法

  ```python
  requests.get(url,params=None,**kwargs)
  ```

  * url：拟获取页面的url链接
  * params：url中的额外参数，字典或字节流格式，可选
  * **kwargs：12个控制访问的参数

* Response对象的属性

  | 属性                | 说明                                             |
  | ------------------- | ------------------------------------------------ |
  | r.status_code       | HTTP请求的返回状态，200表示连接成功，404表示失败 |
  | r.text              | HTTP相应内容的字符串形式，即，url对应的页面内容  |
  | r.encoding          | 从HTTP header中猜测的相应内容编码方式            |
  | r.apparent_encoding | 从内容中分析出的相应内容编码方式（备选编码方式） |
  | r.content           | HTTP相应内容的二进制形式                         |

  ![image-20180630001738309](https://ws1.sinaimg.cn/large/006tKfTcgy1fssi9kew65j30bv068wf1.jpg)

栗子：

```python
>>> import requests
>>> r = requests.get('https://www.baidu.com')
>>> r.encoding = 'utf-8'
>>> r.text
'<!DOCTYPE html>\r\n<!--STATUS OK-->
<html> 
	<head>
    ......
    </head>
    <body>
    ......
    </body> 
</html>
```

> r.encoding：如果header中不存在charset，则认为编码为ISO-8859-1

* Requests库的异常

  | 异常                      | 说明                                        |
  | ------------------------- | ------------------------------------------- |
  | requests.ConnectionError  | 网络连接错误异常，如DNS查询失败、拒绝连接等 |
  | requests.HTTPError        | HTTP错误异常                                |
  | requests.URLRequired      | URL缺失异常                                 |
  | requests.TooManyRedirects | 超过最大重定向次数，产生重定向异常          |
  | requests.ConnectTimeout   | 连接远程服务器超时异常                      |
  | requests.Timeout          | 请求URL超时，产生超时异常                   |

* 状态响应码status_code

  ```python
  >>> r = requests.get('https://www.baidu.com')
  >>> r.status_code
  200
  # 为方便引用，Requests还有一个内置的状态码查询对象
  >>> r.status_code == requests.codes.ok
  True
  # 如果是一个错误请求，可以通过Response.raise_for_status()来抛出异常
  >>> bad_r = requests.get('http://httpbin.org/status/404')
  >>> bad_r.status_code
  404
  
  >>> bad_r.raise_for_status()
  Traceback (most recent call last):
    File "requests/models.py", line 832, in raise_for_status
      raise http_error
  requests.exceptions.HTTPError: 404 Client Error
  # r.status == 200,当我们调用raise_for_status()时，得到的是
  >>> r.raise_for_status()
  None
  ```

* 爬取网页的通用代码框架TTP

  ```python
  import requests
  
  def getHTMLText(url):
      try:
          r = requests.get(url,time=30)
          r.raise_for_status() #如果状态不是200，将引发HTTPError异常
          r.encoding = r.apparent_encoding
          return r.text
      except：
      	return "产生异常"
      
  if __name__ = "__main__":
      url = 'https://www.baidu.com'
      print(getHTMLText(url))
  ```


### HTTP协议

  * HTTP，Hypertext Transfer Protocol，超文本传输协议。

  * HTTP是一个基于“请求与响应”模式的、装状态的应用层协议。

  * HTTP协议采用URL作为定位网络资源的标识

  * URL格式 `http://host[:port][path]` 
    * host：合法的Internet主机域名或IP地址
    * port：端口号，缺省端口为80
    * path：请求资源的路径

  * HTTP协议对资源的操作

    | 方法   | 说明                                                      |
    | ------ | --------------------------------------------------------- |
    | GET    | 请求获取URL位置的资源                                     |
    | HEAD   | 请求获取URL位置资源的响应消息报告，即获得该资源的头部信息 |
    | POST   | 请求向URL位置的资源后附加新的数据                         |
    | PUT    | 请求向URL位置存储一个资源，覆盖原URL位置的资源            |
    | PATCH  | 请求局部更新URL位置的资源，即改变该处资源的部分内容       |
    | DELETE | 请求删除URL位置存储的资源                                 |

    ![image-20180701153345007](https://ws4.sinaimg.cn/large/006tNc79gy1fsued0uqbtj30l005dn17.jpg)

  * 理解PATCH和PUT的区别

    * 采用PATCHA，仅向URL提交局部更新的请求
    * 采用PUT，必须将所有字段一并提交到URL，未提交字段被删除

  * Requests库的head()方法

    * ```python
      >>> r = requests.head('http://www.baidu.com')
      >>> r.headers
      {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Sun, 01 Jul 2018 07:38:20 GMT', 'Last-Modified': 'Mon, 13 Jun 2016 02:50:26 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18'}
      >>> r.text
      ''
      ```

  * Requests库的post()方法

    ```python
    >>> payload = {'key1':'value1','key2':'value2'}
    >>> r = requests.post('http://www.baidu.com/post',data = payload)
    >>> print(r.text)
    { # 向URL POST一个字典，自动编码为form(表单)
        ...
        "form":{
            "key2":"value2",
            "key1":"value2"
        },
        ...
    }
    ```

  * Requests库的put()方法

    ```python
    >>> payload = {'key1':'value1','key2':'value2'}
    >>> r = requests.put("http://www.baidu.com/put',data = payload")
    >>> print(r.text)
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    	<html>
        	<head>
    			<title>405 Method Not Allowed</title>
    		</head>
            <body>
    			<h1>Method Not Allowed</h1>
    			<p>The requested method PUT is not allowed for the URL 					/put',data=payload.</p>
    		</body>
    	</html>
    ```

    

### Requests库主要方法解析

* requests.request(method,url,**kwargs)

  * method：请求方式，对应get/put/post等7种

    * r = requests.request('GET',url,*kwargs)
    * r = requests.request('HEAD',url,*kwargs)
    * r = requests.request('POST',url,*kwargs)
    * r = requests.request('PUT',url,*kwargs)
    * r = requests.request('PATCH',url,*kwargs)
    * r = requests.request('delete',url,*kwargs)
    * r = requests.request('OPTIONS',url,*kwargs)

  * url：获取页面的url链接

  * **kwargs：控制访问参数，共13个

    * params：字典或字节序列，作为参数增加到url种

      ```python
      >>> kv = {'key1':'value1','key2':'value2'}
      >>> r = requests.request('GET','http://www.baidu.com/s',params=kv)
      >>> print(r.url)
      http://www.baidu.com/s?key1=value1&key2=value2
      ```

    * data：字典、字节序列或文件对象，作为Request的内容，向服务器提交资源时使用

      ```python
      >>> kv = {'key1':'value1','key2':'value2'}
      >>> r = requests.request('POST','http://www.baidu.com/s',data=kv)
      >>> body = '主体内容'
      >>> r = requests.request('POST','http://www.baidu.com/s',data=body)
      ```

    * json：JSON格式的数据，作为Request的内容

      ```python
      >>> kv = {'key1':'value1'}
      >>> r = requests.request('POST','http://www.baidu.com/s',json=kv)
      ```

    * headers：字典，HTTP定制头

      ```python
      >>> hd = {'user-agent':'Chrome/10'}
      >>> r = requests.request('POST','http://python123.io/ws',headers=hd)
      ```

    * cookies：字典或CookieJar，Request中的cookie

    * auth：元组，支持HTTP认证功能

    * file：字典类型，传输文件

      ```python
      >>> fs = {'file':open('data.xls','rb')}
      >>> r = requests.request('POST','http://python123.io/ws',files=fs)
      ```

    * timeout：设定超时时间，秒为单位

      ```python
      >>> r = requests.request('GET','http://www.baidu.com',timeout=10)
      ```

    * proxies：字典类型，设定访问代理服务器，可以增加登录认证

      ```python
      >>> pxs = {'http':'http://user:pass@10.10.10.1:1234','https':'https://10.10.10.1:4321'}
      >>> r = requests.request('GET','http://www.baidu.com',proxies=pxs)
      ```

    * allow_redirects：True/False，默认为True，重定向开关

    * stream：True/False，默认为True，获取内容立即下载开关

    * verify：True/False，默认为True，认证SSL证书开关

    * cert：本地SSL证书路径

## 网络爬虫的盗亦有道

* 网络爬虫的尺寸

![img](https://ws2.sinaimg.cn/large/006tNc79gy1fsuhzdxon1j30oz07s0u3.jpg)

* 网络爬虫的法律风险

  * 服务器上的数据有产权归属
  * 网络爬虫获取数据后牟利将带来法律风险

* 网络爬虫泄露数据

* 网络爬虫的限制

  * 来源审查：判断User-Agent进行限制
    * 检查来访HTTP协议头的User-Agent域，只响应浏览器或友好爬虫的访问
  * 发布公告：Robots协议
    * 告知所有爬虫网站的爬取策略，要求爬虫遵守

* Robots协议（Robots Exclusion Standard 网络爬虫排除标准）

  * 作用：网站告知网络爬虫哪些页面可以抓取，哪些不行 

  * 形式：在网站根目录下的robots.txt文件

  * https://www.jd.com/rboots.txt

    ```txt
    User-agent: * 
    Disallow: /?* 
    Disallow: /pop/*.html 
    Disallow: /pinpai/*.html?* 
    User-agent: EtaoSpider 
    Disallow: / 
    User-agent: HuihuiSpider 
    Disallow: / 
    User-agent: GwdangSpider 
    Disallow: / 
    User-agent: WochachaSpider 
    Disallow: /
    # 注释 * 代表所有 /代表根目录
    User-agent: *
    Disallow: /
    ```

  * 遵守方式

    * 网络爬虫：自动或人工识别robots.txt，再进行内容爬取
    * 约束性：Robots协议是建议但非约束性，网络爬虫可以不遵守，但存在法律风险

  * 理解

    ![img](https://ws2.sinaimg.cn/large/006tNc79gy1fsuinx4kc6j30np05wgmm.jpg)




## Requests库爬取实例

### 实例1：京东商品页面的爬取

```python
import requests
url = 'https://item.jd.com/2967929.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')
```

### 实例2：亚马逊商品的爬取

```python
import requests
url = "https://www.amazon.cn/dp/B00QJDOLIO/ref=lp_1536596071_1_1?s=amazon-devices&ie=UTF8&qid=1530439999&sr=1-1"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_coding
    print(r.text[1000:2000])
except:
    print("爬取失败")
```

### 实例3：百度和360搜索关键字提交

* 百度

```python
import requests
keyword = "Python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
```

* 360

```python
import requests
keyword = "Python"
try:
    kv = {'q':keyword}
    r = requests.get("http://www.so.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
```

### 实例4：网络图片的爬取和存储

```python
import requests
import os
root = "/Users/entercoder/Documents/123.jpg"
url = "https://ws2.sinaimg.cn/large/006tNc79gy1fsuinx4kc6j30np05wgmm.jpg"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("save successful")
    else:
        print("file already exists")
except:
    print("download fail")
```

### 实例5：IP地址归属地自动查询

```python
import requests
url = "http://ip138.com/ips138.asp?ip="
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
```



## BeautifulSoup入门

### BeautifulSoup库的安装

* 使用pip安装

  ```bash
  $ pip3 install BeautifulSoup4
  ```

* 源码安装

  * [下载源码](http://www.crummy.com/software/BeautifulSoup/download/4.x/)

  * 通过setup.py安装

    ```bash
    $ Python setup.py install
    ```

* 安装解析器

  * lxml

    ```bash
    $ pip3 install lxml
    ```

  * html5lib

    ```bash
    $ pip3 install html5lib
    ```

* 主要解析器及使用方法

  | 解析器           | 使用方法                                                     |
  | ---------------- | ------------------------------------------------------------ |
  | Python标准库     | BeautifulSoup(markup,"html.parser")                          |
  | lxml HTML 解析器 | BeautifulSoup(markup,"lxml")                                 |
  | lxml XML 解析器  | BeautifulSoup(markup,["lxml-xml"])<br />BeautifulSoup(markup,"xml") |
  | html5lib         | BeautifulSoup(markup,"html5lib")                             |

* 测试

  ```python
  >>> import requests
  >>> r = requests.get('https://python123.io/ws/demo.html')
  >>> demo = r.text
  >>> from bs4 import BeautifulSoup
  >>> soup = BeautifulSoup(demo,'html.parser') # 需要解析的html格式的内容和解析器
  >>> print(soup.prettify())
  <html>
   <head>
    <title>
     This is a python demo page
    </title>
   </head>
   <body>
    <p class="title">
     <b>
      The demo python introduces several python courses.
     </b>
    </p>
    <p class="course">
     Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
     <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
      Basic Python
     </a>
     and
     <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
      Advanced Python
     </a>
     .
    </p>
   </body>
  </html>
  ```

### BeautifulSoup库的基本元素

* BeautifulSoup库是解析、遍历、维护“标签树”的功能库

* BeautifulSoup类的基本元素

  | 基本元素        | 说明                                                       |
  | --------------- | ---------------------------------------------------------- |
  | Tag             | 标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾    |
  | Name            | 标签的名字，\<p>...\<p>的名字是'p'，格式：\<tag>.name      |
  | Attributes      | 标签的属性，字典形式组织，格式：\<tag>.attrs               |
  | NavigableString | 标签内非属性字符串，\<>...</>中字符串，格式：\<tag>.string |
  | Comment         | 标签内字符串的注释部分，一种特殊的Comment类型              |

  ![img](https://ws4.sinaimg.cn/large/006tNc79gy1fsuqg0h7bvj30nb09d3zm.jpg)

  ```python
  >>> import requests
  >>> from bs4 import BeautifulSoup
  
  >>> r = requests.get("http://python123.io/ws/demo.html")
  >>> demo = r.text
  >>> soup = BeautifulSoup(demo,"html.parser")
  >>> soup.title
  <title>This is a python demo page</title>
  >>> tag = soup.a
  >>> tag
  <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
  >>> soup.a.name
  'a'
  >>> soup.a.parent.name
  'p'
  >>> soup.a.parent.parent.name
  'body'
  >>> tag.attrs
  {'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
  >>> tag.attrs['class']
  ['py1']
  >>> tag.attrs['href']
  'http://www.icourse163.org/course/BIT-268001'
  >>> type(tag.attrs)
  <class 'dict'>
  >>> type(tag)
  <class 'bs4.element.Tag'>
  >>> soup.a.string
  'Basic Python'
  >>> soup.p.string
  'The demo python introduces several python courses.'
  >>> type(soup.p.string)
  <class 'bs4.element.NavigableString'>
  >>> newsoup = BeautifulSoup("<b><!-- This is a comment --></b><p>This is not a comment</p>","html.parser")
  # 不常用
  >>> newsoup.b.string
  ' This is a comment '
  >>> type(newsoup.b.string)
  <class 'bs4.element.Comment'>
  >>> newsoup.p.string
  'This is not a comment'
  >>> type(newsoup.p.string)
  <class 'bs4.element.NavigableString'>
  ```

  

### 基于bs4库的HTML内容遍历方法

* 遍历方式

  ![img](https://ws4.sinaimg.cn/large/006tNc79gy1fsuqjfmvegj30no08ojse.jpg)

  * 标签树的下行遍历

    | 属性         | 说明                                                    |
    | ------------ | ------------------------------------------------------- |
    | .contents    | 子节点的列表，将所有\<tag>所有儿子节点存入列表          |
    | .children    | 子节点的迭代类型，与.contents类似，用于循环遍历儿子节点 |
    | .descendants | 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历      |

    ```python
    >>> from bs4 import BeautifulSoup
    >>> soup = BeautifulSoup(demo,"html.parser")
    >>> soup.head
    <head><title>This is a python demo page</title></head>
    >>> soup.head.contents
    [<title>This is a python demo page</title>]
    >>> soup.body.contents
    ['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
    <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\n']
    >>> len(soup.body.contents)
    5
    >>> soup.body.contents[1]
    <p class="title"><b>The demo python introduces several python courses.</b></p>
    >>> 
    # 遍历儿子节点
    for child in soup.body.children:
        print(child)
    # 遍历子孙节点
    for child in soup.body.descendants:
        print(children)
    ```

  * 标签树的上行遍历

    | 属性     | 说明                                           |
    | -------- | ---------------------------------------------- |
    | .parent  | 节点的父亲标签                                 |
    | .parents | 节点的先辈标签的迭代烈性，用于循环遍历先辈节点 |

    ```python
    >>> soup = BeautifulSoup(demo,"html.parser")
    >>> soup.title.parent
    <head><title>This is a python demo page</title></head>
    >>> soup.html.parent
    <html><head><title>This is a python demo page</title></head>
    <body>
    <p class="title"><b>The demo python introduces several python courses.</b></p>
    <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
    <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
    </body></html>
    >>> soup.parent
    # 标签树的上行遍历
    >>> soup = BeautifulSoup(demo,"html.parser")
    >>> for parent in soup.a.parents:
        	if parent is None:
                print(parent)
            else:
                print(parent.name)
    ```

  * 标签树的平行遍历

    | 属性               | 说明                                                 |
    | ------------------ | ---------------------------------------------------- |
    | .next_sibling      | 返回按照HTML文本顺序的下一个平行节点标签             |
    | .previous_sibling  | 返回按照HTML文本顺序的上一个平行节点标签             |
    | .next_siblings     | 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签 |
    | .previous_siblings | 迭代类型，返回按照HTML文本顺序的前续所有平行节点标签 |

    ```python
    >>> soup = BeautifulSoup(demo,"html.parser")
    >>> soup.a.next_sibling
    ' and '
    >>> soup.a.next_sibling.next_sibling
    <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>
    >>> soup.a.previous_sibling
    'Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n'
    >>> soup.a.previous_sibling.previous_sibling
    
    # 标签树的平行遍历
    # 遍历后续节点
    for sibling in soup.a.next_siblings
    	print(sibling)
    # 遍历前续节点
    for sibling in soup.a.previous_siblings:
        print(sibling)
    ```

  * 总结

    ![img](https://ws3.sinaimg.cn/large/006tNc79gy1fsurizrbltj30ns0bfgne.jpg)

### 基于bs4库的HTML格式输出

* prettify()方法可以格式化输出HTML文本

  ```python
  >>> soup = BeautifulSoup(demo,"html.parser")
  >>> soup.prettify()
  >>> print(soup.prettify())
  ```

## 三种信息标记形式

* 三种形式
  * XML
  * JSON
  * YAML
* 三种信息标记形式的比较
* 信息提取的一般方法



​    

​    

​    