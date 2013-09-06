from google.appengine.api import users

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
      user = users.get_current_user()
      if user:
        self.response.headers['Content-Type'] = 'text/plain'
        x=1
        y=0
        while x>=1 and x<5000:
		  if x % 2 > 0:
		    for number in range(1,x,1):
		      if x % number > 0:
		        y+=1
		  if y == (x-2):
		    self.response.write(str(x) + ' is PRIME')
		  else:
		    self.response.write(str(x))
		  y = 0
		  x+=1
            #self.response.write('Hello, ' + user.nickname())
      else:
        self.redirect(users.create_login_url(self.request.uri))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


"""
while x>=1:
  if x % 2 > 0:
    for number in range(1,x,1):
      if x % number > 0:
        y+=1
  if y == (x-2):
    print str(x) + ' is PRIME'
  else:
    print x
  y = 0
  x+=1
  """