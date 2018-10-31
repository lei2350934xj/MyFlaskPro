from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField	# 数据类型
from wtforms.validators import DataRequired, EqualTo	# 验证函数


class LoginForm(FlaskForm):
	username = StringField('用户名',validators=[DataRequired(u'必须填写用户名')])
	password = PasswordField('密码',validators=[DataRequired(u'必须填写密码')])
	login = SubmitField('登录')


class RegisterBtn(FlaskForm):
	register = SubmitField('注册>>')


class RegisterForm(FlaskForm):
	username = StringField('*用户名', validators=[DataRequired(u'必须填写用户名')])
	password = PasswordField('*密码', validators=[DataRequired(u'必须填写密码')])
	password2 = PasswordField('*确认密码', validators=[DataRequired(u'必须填写密码'), EqualTo('password', u'两次输入不一致')])
	register = SubmitField('注册')