import os
from lib import webapp2
from google.appengine.ext.webapp import template
        
class NewCampaign(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('templates/campaigns/new.html',{}))
    def post(self):
        pass