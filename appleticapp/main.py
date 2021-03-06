import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.dirname(__file__)))

from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))) 

class listevent(ndb.Model):
	event = ndb.StringProperty()
	time = ndb.StringProperty()
	date = ndb.StringProperty()
	location = ndb.StringProperty()

#Calls the homepage template
class MainHandler(webapp2.RequestHandler):
HEAD
    def get(self):
        template = jinja_environment.get_template('homescreen.html')
        self.response.write(template.render())

	def get(self):

			template = jinja_environment.get_template('schedule.html')
			self.response.write(template.render())

	def post(self):
		event_from_form = self.request.get('event')
		time_from_form = self.request.get('time')
		date_from_form = self.request.get('date')
		location_from_form = self.request.get('location')


		event_post = listevent(
			event = event_from_form,
			time = time_from_form,
			date = date_from_form,
			location = location_from_form,
			)
		event_post.put()

		template = jinja_environment.get_template('event_added.html')
		self.response.write(template.render(
			{
				'post': event_post
			}))

class EventHandler(webapp2.RequestHandler):
	def get(self):
		eventlist = listevent.query().fetch()
		template = jinja_environment.get_template('eventlist.html')
		self.response.write(template.render(
			{
				'post': eventlist

			}))

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/events', EventHandler),
],debug=True)