import bottle
import sys
app = application = bottle.Bottle()

@app.route('/hello')
def hello():
	return "hello world"

if __name__ == '__main__':
	app.run()