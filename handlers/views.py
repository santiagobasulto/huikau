from google.appengine.api import users

from lib import webapp2

def index_page(request, *args, **kwargs):
    response = webapp2.Response()
    response.write("<h1>Welcome to Huikau!</h1>")
    response.write("<a href='%s'>Home</a>" % webapp2.uri_for('home'))
    return response

def una_accion(request, *args, **kwargs):
    response = webapp2.Response()
    response.write("<h1>Una Accion!</h1>")
    return response

def test_user(request, *args, **kwargs):
    user = users.get_current_user()
    response = webapp2.Response()
    if user:
        response.headers['Content-Type'] = 'text/html'
        response.out.write('Hello, ' + user.nickname())
    else:
        return webapp2.redirect(users.create_login_url(request.uri))
    return response