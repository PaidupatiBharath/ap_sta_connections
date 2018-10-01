from bottle import route, run, template

@route('/clients')
def index():
    details = [{'s_no':1, 'mac':'ab:cd:ef:gh:ij:kl', 'ip':'127.0.0.1'},{'s_no':2, 'mac':'aa:bb:cc:dd:Ee:ff', 'ip':'192.168.1.10'}]
    fold='100-clients'
    element = []
    element.append(template('index', name='Access Point 1'))
    for i in details:
        element.append(template('table', **i ))
    return element

if __name__ == '__main__':
    run(debug=True, reloader=True)
