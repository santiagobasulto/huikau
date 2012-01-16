import random

from lib import webapp2
from google.appengine.api import users
from google.appengine.ext import db
from models import Campaign,TextAdvert,Advert,ImgAdvert

from django.utils import simplejson

def img_json(ad):
        return simplejson.dumps({
            'name':ad.name,
            'target_url':ad.target_url,
            'mimetype':ad.mimetype,
            'img_path':webapp2.uri_for('image-server',img_advert_id=ad.key().id())
        })
def text_json(ad):
    return simplejson.dumps({
            'name':ad.name,
            'target_url':ad.target_url,
            'title':ad.title
        })
class Random(webapp2.RequestHandler):
    def get(self,campaign_id,type='text'):
        model = TextAdvert
        f = text_json
        if type == 'image':
            model = ImgAdvert
            f = img_json
        c = Campaign.get_by_id(int(campaign_id))
        q = model.all().filter('campaign',c)
        count = model.all().filter('campaign',c).count()
        rdm = random.randint(0,count-1)
        self.response.out.write(f(q.fetch(limit=1,offset=rdm)[0]))
    