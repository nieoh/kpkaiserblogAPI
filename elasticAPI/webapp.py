#Run with:
# gunicorn -k tornado egg:gunicorn #tornado webapp:app

from tornado.web import Application, RequestHandler

class MainHandler(RequestHandler):
	def get(self):
		self.write("Hello, world")

app = Application([
	(r"/", MainHandler)
	])