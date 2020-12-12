# -*- coding: utf-8 -*-
"""
@version 3.7
@time 2020/12/12 15:13
@author zwl
@title
@file notes_client.py
"""

from flask import Flask, send_file,render_template, url_for, redirect,abort,request
import sys

USER_KEY = ["123456"]

app = Flask(__name__)

@app.route('/index')
def index():
    # 首页
    return render_template('index.html')

@app.route('/')
def redirect_toindex():
    return redirect(url_for('index'))


@app.route("/login")
def admin_login():
    # 主动跳转404
    try:
        uskey = request.args['key']

    except:
        abort(404)
    else:
        if uskey in USER_KEY:
            return render_template("login.html")
        else:
            abort(404)






if __name__ == '__main__':
    app.run(debug=True)
