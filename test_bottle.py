#coding:utf8
import os
import time
import urllib2
from bottle import *

@route('/')
@route('/hello/<name:path>')
def greet(name='stranger'):
    #time.sleep(5)
    name = request.cookies.account or name
    return template('Hello {{name}}, how are you?, ', name=name)

@route('/hello')
def hello_again():
    if request.get_cookie('visited'):
        count = int(request.cookies.count)
        count += 1
        response.set_cookie('count', str(count))
        return '''Welcome back! Nice to see you again.
                You visit this page %d times
                '''%count
    else:
        response.set_cookie('visited', 'yes')
        response.set_cookie('count', '1')
        return 'Hello there! Nice to meet you'


@get("/login")
def login():
    return '''
        <form action='/login' method='post'>
            Username:<input name='username' type='text' />
            Password:<input name='password' type='password'/>
            <input value='login' type='submit' />
        </form>
        '''

@post("/login")
def do_login():
    '''接收表单数据'''
    username = request.forms.get("username","")
    password = request.forms.get("password","")
    # 应对大容量 post
    j_data = request.body.read()
    if check_login(username, password):
        response.set_cookie('account', username)#, secret='some-secret-key')
        return "<p>Your login information was correct</p>"
    else:
        return "<p>Login failed</p>"

def check_login(username, password):
    return True

@route('/static/<filepath>')
def server_static(filepath):
    '''返回静态文件'''
    return static_file(filepath, root=r'E:\FPAN\somepy\mypyfile',
                       mimetype='text/plain', download=True or filepath
                       )

@error(404)
def error404(error):
    '''参数必须为error, 重写error'''
    # 将404重定向到指定网址
    response.status = 301
    response.add_header("location", "http://www.baidu.com")
    return "Nothing here, sorry"

@route('/return')
def test_return():
    '''测试返回值类型'''
    #return None
    #return False
    #return True
    #return error
    #return {}
    #return {"a":1}
    #return {"a":time}
    def ite():
        num = 0
        yield num
        num += 1
    return ite

@route('/iso')
def get_iso():
    '''? can't not set attribute 设置返回值编码'''
    #response.charset = 'ISO-8859-15'
    #response.charset = 'utf8'
    return u'This will be sent with ISO-8859-15 encoding.'

@route('/latin9')
def get_latin():
    '''设置返回值类型等'''
    response.content_type = 'text/html; charset=latin9'
    #response.content_type = 'application/json'
    return u'ISO-8859-15 is also known as latin9.'

@route('/restricted')
def restricted():
    #抛出指定返回码，并自定义描述
    #abort(401, 'Sorry, access denied.')
    username = request.get_cookie("account")#, secret='some-secret-key')
    if username:
        return template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logined. Access denied."

@route('/wrong/url')
def wrong():
    '''重定向'''
    redirect('/right/url')
    return

@route('/is_ajax')
def is_ajax():
    '''测试请求头部信息中的ajax'''
    if request.headers.get('X-Requested-With','') == 'XMLHttpRequest':
        return 'This is a AJAX request'
    else:
        return 'This is a normal request'

@route('/query')
def test_query():
    '''URL参数测试'''
    qr_str = request.query_string
    return qr_str

@route('/upload', method='POST')
def do_upload():
    '''上传文件'''
    category = request.forms.category
    upload = request.files.upload
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return 'File extension not allowed'
    save_path = get_save_path_for_category(category)
    upload.save(save_path)
    return 'ok'

def get_save_path_for_category(category):
    #return r'E:\FPAN\somepy\temp\fasd.png'
    return r'E:\FPAN\somepy\temp'

@route('/upload', method='GET')
def upload():
    return '''
            <form action='/upload' method='POST' enctype='multipart/form-data'>
                Category:       <input type='text' name='category' />
                Select a file:  <input type='file' name='upload' />
                <input type='submit' value='Start upload'/>
            </form>
            '''

@route('/ip')
def get_ip():
    '''获取访问者ip'''
    ip = request.get("REMOTE_ADDR")
    #ip = request.environ.get("REMOTE_ADDR")
    #ip = request["REMOTE_ADDR"]
    return 'your ip is %s'%ip

@route('/test_post',method='POST')
def test_post():
    response.content_type = 'text/html;charset=utf8'
    #post参数
    post_keys = request.forms.keys()
    #get参数
    get_keys = request.query.keys()
    body = 'this is a %s request\r\n'%request.method
    body += 'get args  %s\r\n'%request.query_string
    body += 'post args %s\r\n'%dict(request.forms)
    return body




#多线程
#run(host="0.0.0.0", port=8080, server='paste')
#自动重载
#run(host="0.0.0.0", port=8080, reloader=True)
run(host="0.0.0.0", port=8080)
