# -*- coding: utf-8 -*-
"""
@version 3.7
@time 2020/12/12 15:13
@author zwl
@title
@file notes_client.py
"""

from flask import Flask, send_file,render_template, url_for, redirect
import sys


app = Flask(__name__)

@app.route('/index')
def index():
    # 首页
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
