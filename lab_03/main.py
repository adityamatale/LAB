# import webapp2
# import os
# from google.appengine.ext.webapp import template

# class MainPage(webapp2.RequestHandler):
#     #to front end
#     def get(self): 
#         path = os.path.join(os.path.dirname(__file__),"index.html")
#         context = {}
#         self.response.out.write(template.render(path, context))
#     #from front end
#     def post(self):
#         pincode = self.request.get()
import webapp2
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self): 
        path = os.path.join(os.path.dirname(__file__), "index.html")
        context = {}
        self.response.out.write(template.render(path, context))
    
    def post(self):
        pincode = self.request.get('zipCode')
        if not pincode:
            context = {'error': 'Please Enter a Valid Pin Code!'}
            path = os.path.join(os.path.dirname(__file__), "index.html")
            self.response.out.write(template.render(path, context))
        else:
            # Here you would typically perform your lookup based on the pincode
            # For now, we will just render the same page with a success message
            context = {'error': f'Searching for Post Offices in {pincode}'}
            path = os.path.join(os.path.dirname(__file__), "index.html")
            self.response.out.write(template.render(path, context))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
