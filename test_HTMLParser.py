#coding:utf8
import HTMLParser
import urllib2
class myHtmlParser(HTMLParser.HTMLParser):
    def __init__(self):
        #super(HTMLParser.HTMLParser, self).__init__()
        #旧式类
        HTMLParser.HTMLParser.__init__(self)
        self.pd = 0
        self.con = ''

    def handle_starttag(self,tag,attrs):
        if tag=='div':
            for (key,value) in attrs:
                if key=='class' and value=='WB_detail':
                    self.pd=1

    def handle_data(self,data):
        self.con +=data

    def handle_endtag(self,tag):
        pass

    def getresult(self):
        print self.data


#html实体字符转义
print HTMLParser.HTMLParser().unescape("&lt;")


if __name__=="__main__":
    #html = urllib2.urlopen('http://www.baidu.com').read()
    #myhtml = myHtmlParser()
    #myhtml.feed(html)
    pass
    
