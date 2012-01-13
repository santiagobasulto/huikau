import os
from lib import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db

from models import Campaign
        
class NewCampaign(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.uri))
        self.response.out.write(template.render('templates/campaigns/new.html',{}))
            
    def post(self):
        user = users.get_current_user()
        if user:
            name = self.request.get('name')
            c = Campaign(name=name,owner=user)
            c.put()
            return self.redirect("/campaign/%s" % c.key().id())
        else:
            return self.redirect(users.create_login_url(self.request.uri))
class ViewCampaign(webapp2.RequestHandler):
    def all_campaigns(self):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.uri))
        q = db.GqlQuery("SELECT * FROM Campaign WHERE owner = :1",user)
        self.response.out.write(template.render('templates/campaigns/all.html',{'campaings':q,}))
            
    def get(self,campaign_id):
        c = Campaign.get_by_id(int(campaign_id))
        user = users.get_current_user()
        if c:
            if c.owner == user:
                self.response.out.write(template.render('templates/campaigns/view.html',{'campaign':c}))
            else:
                self.response.out.write("No tenes permisos")
        else:
            self.response.out.write("La campania no existe")