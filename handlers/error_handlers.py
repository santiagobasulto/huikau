from google.appengine.ext.webapp import template

import logging

def handle_404(request, response, exception):
    logging.exception(exception)
    response.write(template.render('templates/pages/404.html',{}))
    response.set_status(404)
    
def handle_500(request, response, exception):
    logging.exception(exception)
    response.write(template.render('templates/pages/500.html',{}))
    response.set_status(500)