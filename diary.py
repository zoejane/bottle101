# -*- coding: utf-8 -*-
from bottle import route,run,debug

from datetime import datetime
import sys


@route('/')
@route('/diary')
def diary():
    return "哥哥，我是你的日记。"

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=1234, debug=True)
