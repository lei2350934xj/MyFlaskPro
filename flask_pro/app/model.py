from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql

from app import app

# mysql+pymysql:     数据库
# root        用户名
# liangting01  密码
# 127.0.0.1    地址
# 3306  端口号 默认
# flask_sql_demo    数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:liangting01@localhost/flask_pro_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # 跟踪数据库的修改 不建议开启
# app.config的导入必须在创建数据库之前
db = SQLAlchemy(app)

'''
数据库模型:
	一张user表 用于存放用户的注册信息
'''
class User(db.Model):
	# 定义表名
	__tablename__ = 'users'	

	# 定义字段
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique = True)
	password = db.Column(db.String(32))

	# __init__() takes 1 positional argument but 3 were given 该报错的解决
	def __init__(self, username, password):
		self.username = username
		self.password = password

	
	def __repr__(self):
		return '<User: %s %s %s>' %(self.id, self.username, self.password)	


if __name__ == '__main__':
	pass