#coding:utf8
import time
import datetime
from bottle import get, route, request, static_file, run

@get('/html')
def hello():
    filename = request.query.get('file', '')
    if not filename:
        return "nothing!!!"
    with open('/work/spider/html/%s'%filename, 'r') as f:
        html = f.read()
    return html

@get('/mengjie')
def wangmengjie():
    ip = request.get("REMOTE_ADDR")
    with open('/work/spider/html/ip/log', 'a+') as f:
        f.write("%s\t%s\t%s\r\n"%(ip, str(datetime.datetime.now()), int(time.time())))
        for k,v in request.headers.iteritems():
            f.write('%s\t%s\r\n'%(k,v))
        f.write('\r\n')
    with open('/work/spider/html/mobile/index.html') as f:
        html = f.read()
    return html

@route('/css/<filepath>')
def server_static(filepath):
    '''返回静态文件'''
    return static_file(filepath, root=r'/work/spider/html/mobile/css',
                       mimetype='text/plain', download=True or filepath
                       )

@route('/images/<filepath>')
def server_static(filepath):
    '''返回静态文件'''
    return static_file(filepath, root=r'/work/spider/html/mobile/images',
                       mimetype='text/plain', download=True or filepath
                       )

run(host='0.0.0.0', port=80, server='paste')
