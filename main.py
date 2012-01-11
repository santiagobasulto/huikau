from lib import webapp2
import AdServer.AdServer
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, webapp2!')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/adserver', AdServer.AdServer),
], debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()