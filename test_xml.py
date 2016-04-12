#coding:utf8
import requests
import urllib2
from lxml import etree
from xml.etree import ElementTree

from lxml.html.clean import Cleaner
def filter_style_script(text):
    url = 'http://www.amazon.in/Hate-Story-3-Harman-Joshi/dp/B01CSH5LTW'
    text = requests.get(url).text
    s = filter_style_script(text)
    s = s.strip()
    print s[:100]
    html_cleaner = lxml.html.clean.Cleaner(scripts=True, javascript=True, comments=False, style=True,
                    links=False, meta=False, page_structure=False, processing_instructions=False,
                    embedded=False, frames=False, forms=False, annoying_tags=False, remove_tags=None,
                    remove_unknown_tags=False, safe_attrs_only=False)
    etree = lxml.html.document_fromstring(text, lxml.html.HTMLParser(remove_comments=True))
    text = html_cleaner.clean_html(text)
    return text



def text(html):
    data = etree.HTML(html)
    #print dir(data)
    #build = etree.XPath("//p[@id='nv']//text()")
    build = etree.XPath("//popularity/@text")
    print build(data)


xml_text = '''<?xml version="1.0" encoding="utf-8"?>  
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
    
