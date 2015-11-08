import sqlite3
from bottle import route, run,debug,template

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)

@route('/hello')
def hello():
    return 'hello'

run(host='localhost', port=8111, debug=True)
