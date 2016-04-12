#coding:utf8
import re
import os
import time
from fabric.api import cd, run, env

def get_hosts():
    hosts = []
    #all spider
    #hosts = ['spider@192.168.69.{0}:51120'.format(host) for host in range(45, 52)+range(53, 111)+range(116, 120)]
    #hosts += ['spider@192.168.64.{0}:51120'.format(host) for host in range(60, 80)]
    #  69段
    hosts = ['spider@192.168.69.{0}:51120'.format(host) for host in [60,]]
    #  64段
    hosts += ['root@192.168.64.{0}:51120'.format(host) for host in [71,]]

    return hosts

def get_passwords(hosts):
    dic = {}
    for host in hosts:
        if '192.168.69.' in host:
            dic[host] = 'Zhxg2015!'
        elif '192.168.64.' in host:
            dic[host] = 'duamiawen&&&&'
        else:
            pass
    return dic

env.hosts = get_hosts()
env.passwords = get_passwords(env.hosts)
env.colorize_errors = True

def restart_spider():
    with cd("/work/spider"):
        run("killall -9 python", warn_only=True)
        run("python run.pyc --stop", warn_only=True)
        try:
            run("screen -r spider")
        except:
            print "##############"
            run("screen -S spider")
    return
#fab -f test_fabric.py restart_spider

def restart_spider_wait():
    with cd("/work/spider"):
        run("python run.pyc --stop", warn_only=True)
        time.sleep(90)
        run("python run.pyc --stop", warn_only=True)
        try:
            run("screen -r spider")
        except:
            print "##############"
            run("screen -S spider")
    return
#fab -f test_fabric.py restart_spider_wait

def restart_spider_1():
    with cd("/work/spider"):
        run("killall -9 python", warn_only=True)
        run("python run.pyc --stop", warn_only=True)
        s = run("screen -ls", warn_only=True)
        print s
        s = re.sub("\s", "", s)
        screen_list = re.findall("\d+\.\w+", s)
        print screen_list
        screen_list = [x for x in screen_list if "spider" not in x]
        print screen_list
        screen_list = [x.split(".")[0] for x in screen_list]
        print screen_list
        for screen_id in screen_list:
            print screen_id
            run("kill -9 %d"%int(screen_id))
        run("screen -wipe",warn_only=True)
        try:
            run("screen -r spider")
        except:
            run("screen -S spider")
    return
#fab -f test_fabric.py restart_spider_1

def update_spider():
    with cd("/work/spider"):
        run('rm -rf downloader.py')
        run('rz')
#fab -f test_fabric.py update_spider

def test():
    with cd("/work/spider"):
        print "###########",run("ls")
    return 
#fab -f test_fabric.py test


if __name__ == "__main__":
    #get_hosts()
    pass

#runing as follow:
#[user@host:port] fab -f filename.py function_name




