import os
from lib import webapp2
from google.appengine.ext.webapp import template

class AdServer(webapp2.RequestHandler):
    def index(self):
        self.response.write("Welcome to AdServer!")
    def new_campaign(self):
        self.response.out.write(template.render('templates/campaigns/new.html',{}))
        
    def test(self,id):
        self.response.write("Your Campaign: "+str(id))
    def view_campaign(self,campaign_id):
        self.response.write("Your Campaign: "+str(campaign_id))
        
class NewCampaign(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('templates/campaigns/new.html',{}))
    def post(self):
        pass