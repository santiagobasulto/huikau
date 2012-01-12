from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Campaign(db.Model):
    name = db.StringProperty(required=True)
    owner = db.UserProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    active = db.BooleanProperty(default=False)

class Advert(polymodel.PolyModel):
    name            = db.StringProperty(required=False)
    target_url      = db.StringProperty(required=True)
    priority        = db.IntegerProperty(required=False)
    
class TextAdvert(Advert):
    title                   = db.StringProperty(required=True)
    description_text_line_1 = db.StringProperty(required=True)      
    description_text_line_2 = db.StringProperty()
    visible_url             = db.StringProperty()
    
    
class ImgAdvert(Advert):
    img_path    = db.StringProperty(required=True)
    alt_text    = db.StringProperty()
    title_text  = db.StringProperty()