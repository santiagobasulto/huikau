'''
Created on 29/08/2011

@author: santiago
'''
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