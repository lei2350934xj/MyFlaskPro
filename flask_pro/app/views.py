from app import app
from flask import render_template
from .forms import LoginForm, RegisterBtn, RegisterForm
from flask import request, make_response, flash, redirect, Response
from .controller import addUser, validateIdCard


@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():    # 首页
    # username = 'liangting01'
    # return render_template('index.html',
    #             username=username)

    if request.method == 'GET': # 相当于直接输入url访问
        flash('get方式访问index')
        # GET方式：1.判断是否登录，没登录重定向到login页面 2.登录了直接渲染带有用户个人信息的index页面
        username = request.cookies.get('username')
        login_success_flag = request.cookies.get('login_success_flag')
        
        if bool(login_success_flag)!=True:  # 注意数据类型转换 一个坑
            return redirect('/login')
        else:
            return render_template('index.html',
                username=username)

    elif request.method == 'POST':  # 相当于从login页面跳转
        flash('post方式访问index')
        # POST方式：1.验证提交的表单信息是否正确 2.验证通过渲染带有用户个人信息的index页面
        loginform = LoginForm()  # 获取表单信息

        if loginform.validate_on_submit():   # 用户点击登录按钮
            username = request.form.get('username')
            password = request.form.get('password')
            if validateIdCard(username, password):    # 验证用户名和密码 暂时mock为真
                print('账号和密码错误 请重新输入')  # 登录失败 不会弹出提示 暂时只能print后台打印
                # 设置cookie
                res = make_response(render_template('index.html', username=username))
                # res = Response('start set cookies')
                res.set_cookie('username',username)
                res.set_cookie('login_success_flag', 'True')
                res.set_cookie('max_age','600') 
                return res  # 设置cookie这里返回res这个很重要 也是个坑
            else:
                # flash('账户名和密码错误')
                print('账号和密码错误 请重新输入')
                return redirect('/login')

    else:
        flash('请求方式出错，请重试')


@app.route('/login', methods=['GET', 'POST'])
def login():    # 登录页面 只渲染一个登录表单
    loginform = LoginForm()
    registerbtn = RegisterBtn()

    if request.method == 'GET': # get访问login页
        return render_template("login.html",
            title = '登录页面',
            loginform = loginform,
            registerbtn = registerbtn)
    
    elif request.method == 'POST':  # post访问login页
        # 验证 register页面表单中的username是否重复：
        # 重复给出提示 不重复插入数据库 设置cookie  提示注册成功 跳转进入index页
        if addUser(request)==False: # 注册失败
            return "注册失败-.-<a href='/register'>点击此处重新注册</a>"
        
        else:   # 注册成功 自动将注册的用户名和密码填充到login页的登录框中 等待用户点击登录按钮
            return "注册成功<a href='/login'>点击此处进行登录</a>"
            # return render_template(render_template('index.html', username=request.form['username']))


@app.route('/register')
def register():
    registerform = RegisterForm()

    return render_template('register.html',
        registerform = registerform)


@app.route('/getCookie')
def get_cookie():   # cookie设置的测试
    cookies = request.cookies
    username = request.cookies.get('6xiaofei')
    return username


@app.route('/card/codeProduce',methods=['GET'])
def codeProduce():  # card 代码生成器
    return render_template('card_codeProduce.html')


if __name__ == '__main__':
    pass
