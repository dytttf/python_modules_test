#coding:utf8
import urllib2
import urllib
import cookielib
import httplib
import threading
import Queue
import time
import redis
import json

#url = 'http://huzhou.19lou.com/forum-1848-thread-114601404283015549-1-1.html'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#cj = cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),urllib2.HTTPHandler)
#opener.addheaders = [('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
#resp = opener.open(url)
#con = resp.read()
#headers = { 'User-Agent' : user_agent }

#request = urllib2.Request(url,headers = {'User-Agent':user_agent})
#reponse = urllib2.urlopen(request)

#opener = urllib.FancyURLopener()
#op = opener.open('http://www.baidu.com').read()

#for item in cj:
#    print item.name,"\t",item.value



httplib.HTTPConnection.debuglevel = 1
url = "http://huzhou.19lou.com/forum-1848-thread-114601404283015549-1-1.html"
request = urllib2.Request(url)
request.add_header("Accept","text/html,*/*")
request.add_header("Connection","Keep-Alive")

opener = urllib2.build_opener()
response = opener.open(request)

print response.url
print response.headers.dict
print len(response.read())


def check_proxy(proxies):
    pro = urllib2.ProxyHandler(proxies)
    opener = urllib2.build_opener()
    opener.add_handler(pro)
    try:
        resp = opener.open('http://www.baidu.com', timeout=5)
        html = resp.read()
        if '百度' in html:
            return True
    except Exception as e:
        print e
        return False
    return False

def queue_check_proxy(queue):
    conn = redis.StrictRedis.from_url('redis://192.168.110.51/4')
    while 1:
        try:
            proxies = queue.get(True,2)
        except:
            time.sleep(2)
            continue
        if check_proxy(proxies):
            conn.lpush('list_ok_proxies', json.dumps(proxies))
        else:
            pass
    return

def get_proxies():
    url = 'http://192.168.84.4/proxy2_all.txt'
    resp = urllib2.urlopen(url)
    proxy_list = resp.readlines()
    proxy_list = [tuple(x.strip().split('\t')) for x in proxy_list]
    proxies_list = [{'%s'%proxy[0]:'%s://%s:%s'%proxy} for proxy in proxy_list]
    return proxies_list

def mul_check():
    thread_list = []
    proxy_queue = Queue.Queue()
    for i in range(100):
        t = threading.Thread(target=queue_check_proxy, args=(proxy_queue,))
        t.start()
        thread_list.append(t)
    while 1:
        proxies_list = get_proxies()
        for proxies in proxies_list:
            proxy_queue.put(proxies)
    for t in thread_list:
        t.join()
    return
    


if __name__ == "__main__":
    proxies = {"http":"http://111.56.13.172:80", }
    #print check_proxy(proxies)
    mul_check()
