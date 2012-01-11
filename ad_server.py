from lib import webapp2
class AdServer(webapp2.RequestHandler):
    def index(self):
        self.response.write("Welcome to AdServer!")
    def new_campaign(self):
        self.response.write("New Campaign!")
    def test(self,id):
        self.response.write("Your Campaign: "+str(id))
    def view_campaign(self,campaign_id):
        self.response.write("Your Campaign: "+str(campaign_id))