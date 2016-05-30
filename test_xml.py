#coding:utf8
import requests
import urllib2
from lxml import etree
from xml.etree import ElementTree

import lxml
from lxml.html.clean import Cleaner

def filter_style_script(text):
    u'''去除注释 style script'''
    html_cleaner = Cleaner(scripts=True, javascript=True, comments=True, style=True,
                    links=False, meta=False, page_structure=False, processing_instructions=False,
                    embedded=False, frames=False, forms=False, annoying_tags=False, remove_tags=None,
                    remove_unknown_tags=False, safe_attrs_only=False)
    text = html_cleaner.clean_html(text)
    return text

html = '''
<html>
    <head>
    <title>fasdfasd</title>
    <!--
    hello
    -->
    </head>
    <body>
    </body>
</html>
'''
print filter_style_script(html)

def text(html):
    data = etree.HTML(html)
    #print dir(data)
    #build = etree.XPath("//p[@id='nv']//text()")
    build = etree.XPath("//popularity/@text")
    print build(data)


xml_text = '''<?XML version="1.0" encoding="utf-8"?>
<root>
 <person age="18">
    <name>hzj</name>
    <sex>man</sex>
 </person>
 <person age="19" des="hello">
    <name>kiki</name>
    <sex>female</sex>
 </person>
</root>'''

root = ElementTree.fromstring(xml_text)
print dir(root)
list_node = root.getiterator('person')
for node in list_node:
    print node.tag

print ElementTree.tostring(node)

if __name__=="__main__":
    url = "http://www.baidu.com"
    url = 'http://data.alexa.com/data?cli=10&&url=ldnews.cn'
    html = urllib2.urlopen(url).read()
    #text(html)
    
