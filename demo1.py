# !/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
# 下载一个网址
url = 'http://www.jingcaiyuedu.com/book/23269.html'
# 模拟浏览器发送http请求
response = requests.get(url)
#编码方式
response.encoding = 'utf-8'
#目标小说主页的网页源码
html = response.text
# 小说名
title = re.findall(r'<meta property="og:title" content="(.*?)"/>',html)[0]
#新建一个文件，保存小说内容
fb = open('%s.txt' % title,'w',encoding='utf-8')
#获取每一章的信息（章节，url）
dl = re.findall(r'<dl id="list">.*?</dl>',html,re.S)[0]
chapter_info_list = re.findall(r'href="(.*?)">(.*?)<',dl)
#循环每一个章节，分别下载
for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = 'http://www.jingcaiyuedu.com%s' % chapter_url
#下载章节内容
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'
    chapter_html = chapter_response.text
    #提取章节内容
    chapter_content = re.findall(r'<script>a1\(\);</script>(.*?)<script>a2\(\);</script>',chapter_html, re.S)[0]
#清洗数据
    chapter_content = chapter_content.replace('','')
    chapter_content = chapter_content.replace('<br />','')
    chapter_content = chapter_content.replace('<br>','')
    chapter_content = chapter_content.replace('<BR>','')
#持久化
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url)

