from lib import webapp2
from lib.webapp2_extras.routes import PathPrefixRoute
import os
from routes import routes

#Detecta si esta en AppEngine y pone debug en false para que no se muestren stack traces
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

app = webapp2.WSGIApplication(routes, debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()