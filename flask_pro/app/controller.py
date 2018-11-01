from .model import *
from flask_httpauth import HTTPTokenAuth
# from flask_httpauth import HTTPBasicAuth

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import g, make_response, jsonify, request


auth = HTTPTokenAuth()
# auth = HTTPBasicAuth()


# 一些常用的 业务逻辑

'''
	1.数据库原子操作
'''
def createTable():
	db.create_all()

def dropTable():	# 一般不要用这个方法
	db.drop_all()


def hasUser(name):
	if User.query.filter_by(username=name).first():
		return True
	else:
		return False

'''
	2.数据库 业务操作
'''
# 2.1 新增用户
def addUser(request):
	# 验证 register页面表单中的username是否重复：
    # 重复给出提示 不重复插入数据库 设置cookie  提示注册成功 跳转进入index页	
	flag = User.query.filter_by(username=request.form['username'])
	# has = User.query.filter_by(username=request.form['username'])
	# print('has=%s'%has)
	# if has:
	# 	flag = True
	# 	print('has不为0,flag=%s'%flag)
	# else:
	# 	flag = False
	# 	print('has为0,flag=%s'%flag)
	name = request.form.get('username')
	if hasUser(name):
		# db.session.rollback()
		return False
	else:
		try:
			user = User(request.form['username'],request.form['password'])
			print('user=%s'%user)
			db.session.add(user)
			db.session.commit()
			return True
		except Exception as e:
			print(e)
			db.session.rollback()
		# 设置cookie
		# res = make_response('set cookie when you createDb')
		# print('111111')
		# res = Response('name')
		# print('222222')
		# res.set_cookie('username', request.form['username'])
		# res.set_cookie('login_success_flag', 'True')
		# res.set_cookie('max_age','600')

		# return res


# 2.2 表单匹配 验证输入信息与数据库数据是否一致
def validateIdCard(username, password):
	pwdInDb = User.query.filter_by(username=username).first().password
	print('数据库中username=%s对应的密码是password=%s'%(username, pwdInDb))

	if password==pwdInDb:
		return True
	else:
		return False


'''
	3.token生成与校验
'''
# 3.1 token生成
# 生成token：可供用户的登录成功时候调用生成token，存入cookie里
# 因为该token里含有id，可以在校验的时候跟数据库中的id比对 确认登录
def generate_token(id, expiration=600):
    # token生成函数做的工作是：一个加密过的字典，
    # 里面包含了用户的id和expiration（600秒）的过期时间
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id':id})


# 3.2 token校验
'''
	这个校验token的函数不好用 因为我现在不知道该函数中的token什么时候传递 在哪里传递
	所以我打算自己重新写一个token的校验函数 以及一个login_required装饰器
	见3.3 和 3.4
'''
# 3.3 cookie里的token校验
@auth.verify_token
def verify_token(token):
	g.user = None
	print(token)
	print('=====')
	print(type(token))
	print('=====')
	s = Serializer(app.config['SECRET_KEY'])
	try:
		data = s.loads(token)   # 包含id和过期时间
		print('进入try语句了')
		print('data=%s'%data)
		print(type(data))
	except:
		print('进入except语句了')
		return False

	if 'id' in data:
		g.user = User.query.get(data['id'])
		return True
	else:
		return False


# 3.4 My_login_required装饰器
def My_login_required(self, fn):

	def wrap():
		print('verify_token(request)=%s'%verify_token(request))
		if verify_token(request):
			print('开始执行wrap里的fn函数了')
			fn()
		else:
			print('开始执行return 错误处理函数了')
			return self.auth_error_callback()
	return wrap
	

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'errno':401,'errmsg':'未登录'}))


'''
	4.通用写cookie
'''
# 4.1 生成cookie
# 因为cookie里的字段是不确定的 所以用不定长的参数
'''
	def fn(a, b, c=20, *args, **kwargs)
	多的参数只有不带key则全存在元组中
	带参数的则以key:value形式存在字典中
'''
def generate_cookie(expiration=600, **kwargs):
	# 遍历字典 key value
	resp = make_response('set cookie')
	
	for key in kwargs:
		resp.set_cookie(key, kwargs[key], max_age=expiration)

	return resp

	# pass



if __name__ == '__main__':
	pass































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































