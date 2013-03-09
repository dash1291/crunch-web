import tornado.ioloop
import tornado.web
from tornado.template import Template

from crunch.crunchauth import add_account, get_user

class index(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html', code=None)

class register(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/register.html', error=None)

    def post(self):
        error = None
        try:
            username = self.request.arguments['username'][0]
            if len(username) == 0:
                raise Exception('bad username')

            """if get_user(username) == True:
                error = 'Username already exists.'
                raise Exception()"""
        except:
            if not error == None:
                error = 'A non-zero length username is required.'

        try:
            password = self.request.arguments['password'][0]
            if len(password) == 0:
                raise Exception('bad password')
        except:
            if not error == None:
                error = 'A non-zero length password is required.'
        print username
        """add_account(username, password)"""

        if error == None:
            t = Template(open('templates/client_sample.html',
                'r').read())
            client_sample_code = t.generate(username=username)

            self.render('templates/index.html', code=client_sample_code)
        else:
            self.render('templates/register.html', error=error)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
        (r"/", index),
        (r"/register/", register),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()