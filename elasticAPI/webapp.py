#Run with:
# gunicorn -k tornado egg:gunicorn #tornado webapp:app

from tornado.web import Application, RequestHandler, HTTPError

class MainHandler(RequestHandler):
	def get(self):
		self.write("Hello, world")

class DealsHandler(RequestHandler):
	def get(self, merchant_name):
		self.write(merchant_name)

	def post(self, merchant_name):
		raise HTTPError(403)

	def delete(self, merchant_name):
		raise HTTPError(403)

	def put(self, merchant_name):
		raise HTTPError(403)




app = Application([
	(r"/", MainHandler),
	(r"/v1/(.*)/deals", DealsHandler)
	])