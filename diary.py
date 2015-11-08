# -*- coding: utf-8 -*-
from bottle import Bottle,route,run,debug

from datetime import datetime
import sys

diary=Bottle()

@diary.route('/')
@diary.route('/diary')
def greeting():
    return '''
<p>哥哥，我是你的日记。</p>
<p>你今天有什么想和我分享的吗？</p>
<a href='/writing'>写日记<a>
<a href='/reading'>读日记<a>
'''

@diary.route('/hello')
def hello():
    return "Hello World!"

run(diary,host='localhost', port=1234, debug=True)
