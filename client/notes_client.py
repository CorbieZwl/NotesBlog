# -*- coding: utf-8 -*-
"""
@version 3.7
@time 2020/12/12 15:13
@author zwl
@title
@file notes_client.py
"""

from flask import Flask, send_file
import sys


app = Flask(__name__)

@app.route('/')
def index():
    #首页
    return "hello world"








if __name__ == '__main__':
    app.run(debug=True)
