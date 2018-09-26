---
title: 初识Python数据分析
date: 2018-09-26 14:55:37
tags: [Python,数据分析]
categories: Note
---

# 初识Python数据分析

> 使用Python进行数据分析，本次使用Python爬取淘宝网全网月饼销售数据，并依据此数据生成词云。

## 获取数据

目标链接：[https://s.taobao.com/search?q=月饼](https://s.taobao.com/search?q=月饼)

模块：requests、jieba、matplotlib、wordcloud、imread、pandas等

## 代码及知识点

### 获取数据

代码：

```python
import requests
import re


def get_html_text(url):
    try:
        res = requests.get(url,timeout=30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return ""


def parse_page(html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        loc = re.findall(r'\"item_loc\"\:\".*?\"', html)
        sale = re.findall(r'\"view_sales\"\:\".*?\"', html)
        # print(plt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            location = eval(loc[i].split(':')[1])
            location = location.split(' ')[0]
            sales = eval(sale[i].split(':')[1])
            sales = re.match(r'\d+', sales).group(0)
            print(price)
            with open("月饼数据.txt", 'a', encoding='utf-8') as f:
                print(f)
                f.write(title + ',' + price + ',' + sales + ',' + location + '\n')
    except:
        print("")


def main():
    goods = '月饼'
    depth = 100
    start_url = 'https://s.taobao.com/search?q=' + goods
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            print('url=',url)
            html = get_html_text(url)
            parse_page(html)
        except:
            continue


if __name__ == '__main__':
    main()
```


### 数据清洗

代码：

```python
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Geo,Style,Line,Bar,Overlap

f = open(r'月饼数据.txt',encoding='utf-8')

df = pd.read_csv(f,sep=',',names=['title','price','sales','location'])

print(df.describe())
```

### 生成词云

代码：

```python
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

f = open('月饼数据.txt',encoding='utf-8')

df = pd.read_csv(f,sep=',',names=['title','price','sales','location'])

title = df.title.values.tolist()

title_s = []

for line in title:
    title_cut = jieba.lcut(line)
    title_s.append(title_cut)

title_clean = []

# 停用词表
stopwords = ["月饼","礼品","口味","礼盒","包邮","【","】","送礼","大","中秋节","中秋月饼","2","饼","蓉","多","个","味","斤","送"," ","老","北京","云南","网红老"]

# 删除停用词表
for line in title_s:
    line_clean = []
    for word in  line:
        if word not in stopwords:
            line_clean.append(word)
    title_clean.append(line_clean)

title_clean_dist = []

# 进行去重
for line in title_clean:
    line_dist = []
    for word in line:
        if word not in line_dist:
            line_dist.append(word)
    title_clean_dist.append(line_dist)

allwords_clean_dist = []

for line in title_clean_dist:
    for word in line:
        allwords_clean_dist.append(word)

df_allwords_clean_dist = pd.DataFrame({'allwords':allwords_clean_dist})

# 对过滤去重词汇进行统一汇总
word_count = df_allwords_clean_dist.allwords.value_counts().reset_index()
word_count.columns = ['word','count']
# backgroud_image = plt.imread('man.jpeg')
# 设置词云样式
wc = WordCloud(width=1920,height=1080,max_words=2000,background_color='white',font_path='simhei.ttf',max_font_size=400,random_state=50)
wc = wc.fit_words({x[0]:x[1] for x in word_count.head(100).values})
plt.imshow(wc,interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("data.png")
```

结果：

![wordcloud](https://ws3.sinaimg.cn/large/006tNc79gy1fvn9yrox5lj30sg0lc45p.jpg)

> 以上参考来源：
* 公众号**恋习Python**-`Python分析今年的月饼之王花落谁家？`
* [https://blog.csdn.net/fly910905/article/details/77763086](https://blog.csdn.net/fly910905/article/details/77763086)
* 

