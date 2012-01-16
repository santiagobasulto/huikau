from lib import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from models import Campaign,TextAdvert,Advert,ImgAdvert

class NewTextAdvert(webapp2.RequestHandler):
    def get(self,campaign_id,errors=None):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.uri))
        self.response.out.write(template.render('templates/advert/new-text.html',{'errors':errors}))
        
    def post(self,campaign_id):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.uri))
        name = self.request.get('name',None)
        target_url = self.request.get('target_url',None)
        priority = self.request.get('priority',None)
        title = self.request.get('title',None)
        description_text_line_1 = self.request.get('description_text_line_1',None)
        description_text_line_2 = self.request.get('description_text_line_2',None)
        visible_url = self.request.get('visible_url',None)
        if not target_url or not title or not description_text_line_1:
            return self.get(campaign_id,['Faltan campos obligatorios',])
        campaign = Campaign.get_by_id(int(campaign_id))
        ad = TextAdvert(
            name = name,
            target_url=target_url,
            priority=int(priority),
            title=title,
            description_text_line_1=description_text_line_1,
            description_text_line_2=description_text_line_2,
            visible_url = visible_url,
            campaign=campaign)
        ad.put()
        if ad.is_saved():
            return self.redirect(webapp2.uri_for('advert.view',advert_id=ad.key().id()))
        self.response.out.write("Error Raro")

class NewImgAdvert(webapp2.RequestHandler):
    def get(self,campaign_id,errors=None):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.uri))
        self.response.out.write(template.render('templates/advert/new-img.html',{'errors':errors}))
            
    def post(self,campaign_id):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.uri))
        name = self.request.get('name',None)
        target_url = self.request.get('target_url',None)
        priority = self.request.get('priority',None)
        img = self.request.POST['img']
        alt_text = self.request.get('alt_text',None)
        title_text = self.request.get('title_text',None)
        if not target_url  or not img.value:
            return self.get(campaign_id,['Faltan campos obligatorios',])
        campaign = Campaign.get_by_id(int(campaign_id))
        ad = ImgAdvert(
            name = name,
            target_url=target_url,
            priority=int(priority),
            img=img.value,
            mimetype=img.type,
            alt_text = alt_text,
            title_text = title_text,
            campaign = campaign)
        ad.put()
        if ad.is_saved():
            return self.redirect(webapp2.uri_for('advert.view',advert_id=ad.key().id()))
        self.response.set_status(500)
        
class ViewAdvert(webapp2.RequestHandler):
    def get(self,advert_id,errors=None):
        ad = Advert.get_by_id(int(advert_id))
        if ad.class_name() == "TextAdvert":
            self.response.out.write(template.render('templates/advert/view-text.html',{'ad':ad}))
        elif ad.class_name() == "ImgAdvert":
            self.response.out.write(template.render('templates/advert/view-img.html',{'ad':ad}))
        else:
            self.response.set_status(500)