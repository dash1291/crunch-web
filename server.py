import tornado.ioloop
import tornado.web

from crunch.crunchauth import add_account, get_user

class index(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class register(tornado.web.RequestHandler):
	def get(self):
		self.render('templates/register.html')

	def post(self):
		error = None
		try:
			username = self.request.arguments['username']
			if len(username) == 0:
				raise Exception('bad username')

			if get_user(username) == True:
				error = 'Username already exists.'
				raise Exception()
		except:
			if not error == None:
				error = 'A non-zero length username is required.'

		try:
			password = self.request.arguments['password']
			if len(password) == 0:
				raise Exception('bad password')
		except:
			if not error == None:
				error = 'A non-zero length password is required.'
		
		add_account(username, password)
		self.render('templates/register.html', error=error)

if __name__ == "__main__":
    application = tornado.web.Application([
    	(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
        (r"/", index),
        (r"/register/", register),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()