from lib import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from models import Campaign

class NewAdvert(webapp2.RequestHandler):
    def select_campaign(self):
        user = users.get_current_user()
        #q = Campaign.all()
        #q.filter('owner=',user)
        q = db.GqlQuery("SELECT * FROM Campaign " +
                "WHERE owner = :1",user)
        self.response.out.write(template.render('templates/advert/select_campaign.html',{'campaings':q}))
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write(template.render('templates/campaigns/new.html',{}))
        else:
            return self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        user = users.get_current_user()
        if user:
            name = self.request.get('name')
            c = Campaign(name=name,owner=user)
            c.put()
            return self.redirect("/campaign/%s" % c.key().id())
        else:
            return self.redirect(users.create_login_url(self.request.uri))
