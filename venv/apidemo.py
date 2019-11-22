# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/10/24 16:48
import flask
from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
   return flask.Response("zhouzhou")

@app.route('/login', methods=['GET', 'POST'])
def login():
   return flask.Response("这是一个查询接口")

@app.route('/', methods=['GET', 'POST'])
def index():
   return flask.Response("{\"username\":\"admin\"}")
if __name__ == '__main__':
   app.run()