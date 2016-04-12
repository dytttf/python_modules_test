#coding:utf8
import imp

test_s = """
import requests
import urllib2

resp = urllib2.urlopen('http://www.baidu.com')

class A():
    pass
"""

mod = imp.new_module('spider')
d = {}
print mod.__dict__
#exec test_s in mod.__dict__
exec test_s in d

mod.__dict__.update(d)

print mod.resp

