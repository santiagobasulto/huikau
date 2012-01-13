from lib import webapp2
from lib.webapp2_extras.routes import PathPrefixRoute

#http://webapp-improved.appspot.com/guide/routing.html
#Handlers en Strings para LazyLoading
routes = [
    webapp2.Route(r'/', handler='handlers.views.index_page', name='home',methods=['GET']),
    #webapp2.Route(r'/adserver/', handler='ad_server.AdServer', handler_method='index',methods=['GET']),
    webapp2.Route(r'/test-user', handler='handlers.views.test_user',methods=['GET']),
    PathPrefixRoute('/campaign', [
        webapp2.Route(r'/new', handler='handlers.campaign.NewCampaign',methods=['GET','POST']),
        webapp2.Route(r'/all', handler='handlers.campaign.ViewCampaign',handler_method='all_campaigns',methods=['GET','POST']),
        webapp2.Route(r'/<campaign_id:\d+>', handler='handlers.campaign.ViewCampaign',name='campaign.view',methods=['GET']),
    ]),
    PathPrefixRoute('/advert', [
        webapp2.Route(r'/new', handler='handlers.advert.NewAdvert',handler_method='select_campaign',methods=['GET']),
        webapp2.Route(r'/new-text/campaign_id:<campaign_id:\d+>', handler='handlers.advert.NewTextAdvert',methods=['GET','POST']),
        webapp2.Route(r'/new-img/campaign_id:<campaign_id:\d+>', handler='handlers.advert.NewImgAdvert',methods=['GET','POST']),
        webapp2.Route(r'/<advert_id:\d+>', handler='handlers.advert.ViewAdvert',name='advert.view',methods=['GET']),
    ]),
    PathPrefixRoute('/users', [
        webapp2.Route(r'/logout', handler='handlers.users.LogoutHandler',name='logout',methods=['GET']),
        #webapp2.Route(r'/login', handler='handlers.users.LoginHandler',name='login',methods=['GET']),
    ]),
    webapp2.Route(r'/image-ad/<img_advert_id:\d+>', handler='handlers.image.ImageAdvertServer',methods=['GET']),
    #webapp2.Route(r'/adserver/(.*)', handler='actions.ad_server.AdServer',handler_method='get',methods=['GET']),
    #(r'/adserver/.*', 'actions.ad_server.AdServer'),
    #('/c-server', 'actions.click_server.ClickServer'),
]