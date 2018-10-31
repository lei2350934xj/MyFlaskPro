#!flask_env/bin/python3.6
from app import app
from app.controller import dropTable, createTable

# dropTable()    
# createTable()   # 注册用户之前 先生成表单

app.run(debug=True)