from bottle import route, run


# link the /hello path to the hello() function
# Whenever a browser requests a URL,
# the associated function is called
# and the return value is sent back to the browser
@route('/hello')
def hello():
    return "Hello World!"

# starts a built-in development server
# The Debug Mode is very helpful during early development,
# but should be switched off for public applications. 
run(host='localhost', port=8080, debug=True)
