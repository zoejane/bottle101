# -*- coding: utf-8 -*-
from bottle import Bottle,route,run,debug,request,template

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

@diary.route('/reading')
def reading():
    diaryFile = open('diary.txt')
    diaryContent = diaryFile.read()
    diaryFile.close()
    diaryContent=diaryContent.replace('\n', '<br />')
    output='<p>====日记====</p>'+diaryContent+"<br /><br /><a href='/'>Back Home<a>"
    return output

@diary.route('/writing',method='GET')
def writing():
    if request.GET.get('save','').strip():
        '''        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()'''
        
        today=datetime.now()
        newDiary=request.GET.get('task', '').strip()
     
        diaryFile = open('diary.txt','a')
        diaryFile.write('\n'+today.strftime("%y/%m/%d")+ ' '+newDiary)
        diaryFile.close()

        return '''
<p>The new diary was saved.</p>
<a href='/'>Back Home<a>
'''
    else:
        return template('new_diary.tpl')

@diary.route('/hello')
def hello():
    return "Hello World!"

run(diary,host='localhost', port=1234, debug=True)
