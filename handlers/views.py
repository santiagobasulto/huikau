from google.appengine.api import users
from google.appengine.ext.webapp import template

from lib import webapp2
from models import Campaign

def index_page(request, *args, **kwargs):
    response = webapp2.Response()
    user = users.get_current_user()
    #response.write("<a href='%s'>Home</a>" % webapp2.uri_for('home'))
    campaigns = None
    if user:
        url = users.create_logout_url(request.uri)
        link_text = "Logout"
        campaigns = Campaign.all().filter('owner',user)
    else:
        url = users.create_login_url(request.uri)
        link_text = "Login"
    response.write(template.render('templates/pages/index.html',{'user':user,'url':url,'link_text':link_text,'campaigns':campaigns}))
    #self.response.out.write(template.render('templates/campaigns/new.html',{}))
    return response

def json_test(request, *args, **kwargs):
    response = webapp2.Response()
    response.write(template.render('templates/pages/json_test.html',{}))
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