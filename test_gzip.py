#coding:utf8
import gzip
import StringIO
import requests

def ungzip_text(response):
    content = response.content
    _io = StringIO.StringIO()
    _io.write(content)
    _io.seek(0)
    gz = gzip.GzipFile(fileobj=_io)
    return gz.read()

if __name__ == "__main__":
    url = 'http://www.myntra.com/sitemap-index.xml.gz'
    resp = requests.get(url)
    text = ungzip_text(resp)
