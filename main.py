import os

from lib import webapp2
from lib.webapp2_extras.routes import PathPrefixRoute

from routes import routes
from handlers import error_handlers

#Detecta si esta en AppEngine y pone debug en false para que no se muestren stack traces
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

app = webapp2.WSGIApplication(routes, debug=True)
app.error_handlers[404] = error_handlers.handle_404
def main():
    app.run()

if __name__ == '__main__':
    main()