# -*- coding: utf-8 -*-
from bottle import Bottle,route,run,debug

from datetime import datetime
import sys

diary=Bottle()

@diary.route('/')
@diary.route('/hello')
def hello():
    return "Hello World!"

run(diary,host='localhost', port=1234, debug=True)
