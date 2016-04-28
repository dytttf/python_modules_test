#coding:utf8
import locale


print locale.getdefaultlocale()
print locale.getlocale()
print locale.setlocale(locale.LC_ALL, "")
