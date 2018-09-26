from bottle import route, run, template

@route('/clients')
def index():
    details = {'a':'122334', 'b':'32441'}
    fold='bharath'
    items=[]
    return template('index',  fold='bharath')

if __name__ == '__main__':
    run(debug=True, reloader=True)
