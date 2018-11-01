#!flask_env/bin/python3.6
from app import app
from app.controller import dropTable, createTable

# dropTable()    
# createTable()   # 注册用户之前 先生成表单

'''
	待开发
	1.数据库读写分离
	2.nginx配置的代理
	3.redis
	4.上线部署
	5.前端美化
'''

app.run(debug=True)