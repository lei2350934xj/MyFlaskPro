from flask import Flask

app = Flask(__name__)
app.config.from_object('config')	# 引入根目录下的配置文件


from app import views
