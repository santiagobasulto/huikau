from lib import webapp2
from lib.webapp2_extras.routes import PathPrefixRoute
import os

#http://webapp-improved.appspot.com/guide/routing.html
#Handlers en Strings para LazyLoading
routes = [
    webapp2.Route(r'/', handler='handlers.views.index_page', name='home',methods=['GET']),
    #webapp2.Route(r'/adserver/', handler='ad_server.AdServer', handler_method='index',methods=['GET']),
    PathPrefixRoute('/campaign', [
        webapp2.Route(r'/new', handler='handlers.campaign.NewCampaign',methods=['GET','POST']),
        webapp2.Route(r'/<campaign_id:\d+>', handler='handlers.campaign.ViewCampaign', handler_method='view_campaign',methods=['GET']),
    ]),
    PathPrefixRoute('/adserver', [
        webapp2.Route(r'/', handler='ad_server.AdServer', handler_method='index',methods=['GET']),
    ]),
    #webapp2.Route(r'/adserver/(.*)', handler='actions.ad_server.AdServer',handler_method='get',methods=['GET']),
    #(r'/adserver/.*', 'actions.ad_server.AdServer'),
    #('/c-server', 'actions.click_server.ClickServer'),
]
#Detecta si esta en AppEngine y pone debug en false para que no se muestren stack traces
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

app = webapp2.WSGIApplication(routes, debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()