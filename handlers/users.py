from lib import webapp2
from google.appengine.api import users
        
class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url("/"))
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect(users.create_login_url("/"))