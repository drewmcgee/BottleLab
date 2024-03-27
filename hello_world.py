from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def fallback():
	return "try setting the URL to localhost:8080/hello/{yourname}"

run(host='localhost', port=8080)
