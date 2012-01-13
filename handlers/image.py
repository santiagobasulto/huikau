from lib import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from models import Campaign,TextAdvert,Advert,ImgAdvert

class ImageAdvertServer(webapp2.RequestHandler):
    def get(self,img_advert_id):
        ad = ImgAdvert.get_by_id(img_advert_id)
        if ad.img:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(greeting.avatar)
        else:
            self.response.out.write("No image")