from app import app
from flask import render_template
from .forms import LoginForm
from flask import request, make_response, flash, redirect, Response


# @app.route('/',methods=['GET','POST'])
# @app.route('/index',methods=['GET','POST'])
@app.route('/setCookie')
def index():    # 首页
    resp = make_response('lxs set_cookie')
    resp.set_cookie('6xiaofei','666')
    # res = make_response('set cookies')
    # res.set_cookie('pwd', 'hahaha')
    # res.set_cookie('login_success_flag', '1')
    # flash('设置cookies成功,请去/get_cookie访问')
    return resp
    # if request.method == 'GET': # 相当于直接输入url访问
    #     flash('get方式访问index')
    #     # GET方式：1.判断是否登录，没登录重定向到login页面 2.登录了直接渲染带有用户个人信息的index页面
    #     username = request.cookies.get('username')
    #     login_success_flag = request.cookies.get('login_success_flag')
    #     if login_success_flag != 1:
    #         return redirect('/login')
    #     else:
    #         return render_template('index.html',
    #             username=username)

    # elif request.method == 'POST':  # 相当于从login页面跳转
    #     flash('post方式访问index')
    #     # POST方式：1.验证提交的表单信息是否正确 2.验证通过渲染带有用户个人信息的index页面
    #     form = LoginForm()  # 获取表单信息

    #     if form.validate_on_submit():   # 用户点击登录按钮
    #         username = request.form.get('username')
    #         password = request.form.get('password')
    #         if True:    # 验证用户名和密码 暂时mock为真
    #             # 设置cookie
    #             # res = make_response(render_template('index.html',username=username))
    #             # res = make_response('start set cookies')
    #             res = Response('start set cookies')
    #             res.set_cookie('username','liangting')
    #             res.set_cookie('login_success_flag','1')
    #             # res.set_cookie('max_age','600') 
    #             return render_template('index.html',
    #                 username=username)   # 登录成功 进入首页
    #         else:
    #             flash('账户名和密码错误')
    #             return redirect('/login')

    # else:
    #     flash('请求方式出错，请重试')


@app.route('/login')
def login():    # 登录页面 只渲染一个登录表单
    form = LoginForm()
    return render_template("login.html",
        title = '登录页面',
        form = form)


@app.route('/getCookie')
def get_cookie():
    cookies = request.cookies
    username = request.cookies.get('6xiaofei')
    return username
    # login_success_flag = request.cookies.get('login_success_flag') 
    # return render_template('test.html', 
    #     username=username, 
    #     login_success_flag=login_success_flag,
    #     cookies=cookies) 



