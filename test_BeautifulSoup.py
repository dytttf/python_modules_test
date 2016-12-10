#coding:utf8
import re
import pprint

from bs4 import BeautifulSoup, UnicodeDammit, SoupStrainer
from bs4.diagnose import diagnose

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p><P></P>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<b><!-- i am a comment --></b>

<p class="story">...</p>
"""

# 编码监测 可设置可能编码
dammit = UnicodeDammit(html_doc, ["utf8", "gbk"])
if 0:
    print dammit.original_encoding

# 转换掉字符中的Windows-1252字符
html_doc = UnicodeDammit.detwingle(html_doc)

# 文档解析过程
# diagnose(html_doc)


# 解析部分文档  提高效率
only_a_tag = SoupStrainer("a")

# html_doc 可以是 文件对象或字符串
soup = BeautifulSoup(html_doc, features=["lxml"], from_encoding='utf8')
'''
:param: features=[] 解析器列表
:param: from_encoding='utf8' 编码
:param: parse_only SoupStrainer 实例
'''

if 0:
    print type(soup).__bases__
    #>>> (bs4.element.Tag,)
# 每一个节点都是一个Tag类

# 格式规范
if 0:
    print soup.prettify()

if 0:
    # dom节点属性
    print "#########################"
    print soup.title
    print "#########################"
    print soup.head
    print "#########################"
    # Tag类自身属性
    print soup.title.name
    print "#########################"
    # 父节点
    print soup.title.parent
    print "#########################"
    pprint.pprint(list(soup.title.parents))
    print "#########################"
    # 兄弟节点
    # 换行符和文本也算兄弟节点。。。
    print soup.p.previous_sibling
    print "#########################"
    print soup.p.next_sibling

if 0:
    Tag_list = soup.find_all()
    # findAll == find_all
    # 搜索父节点
    print soup.p.find_parents()
    # 不显式调用find_all
    print soup('p')
    # 仅搜索子节点 忽略孙...
    print soup.find_all('p', limit=1, recursive=False)
    # 限制搜索结果数量 提升性能
    print soup.find_all('p', limit=1)
    print soup.find(id='link3')
    print soup.find('body').get_text()
    print soup.find(attrs={"class": "title"})
    print soup.find(class_="title")
    print soup.find(attrs={"class": re.compile("title")})

    # string 仅对只含文本子节点的节点有效
    print soup.find('body').string
    print list(soup.find('body').strings)
    print list(soup.find('body').stripped_strings)
    # comment 注释格式的
    # 为毛不是 bs4.element.Comment 
    for tag in soup.find_all('b'):
        print tag
        print type(tag)

if 0:
    # 子节点
    print soup.contents
    # 子节点迭代器
    print soup.children
    # 后代节点迭代器
    print soup.descendants

if 0:
    # 解析过程重现
    print repr(soup.p.previous_element)
    print soup.p.next_element

if 0:
    # css选择器
    print soup.select(".title")
