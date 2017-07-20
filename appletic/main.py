import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.dirname(__file__)))

from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))) 

class listprofile(ndb.Model):
	name = ndb.StringProperty()
	sport = ndb.StringProperty()
	position = ndb.StringProperty()
	school = ndb.StringProperty()
	birthday = ndb.StringProperty()
	age = ndb.StringProperty()
	height = ndb.StringProperty()
	weight = ndb.StringProperty()

class InfoHandler(webapp2.RequestHandler):
	def get(self):

			template = jinja_environment.get_template('profile.html')
			self.response.write(template.render())

	def post(self):
		name_from_form = self.request.get('name')
		sport_from_form = self.request.get('sport')
		position_from_form = self.request.get('position')
		school_from_form = self.request.get('school')
		birthday_from_form = self.request.get('birthday')
		age_from_form = self.request.get('age')
		height_from_form = self.request.get('height')
		weight_from_form = self.request.get('weight')


		profile_post = listprofile(
			name = name_from_form,
			sport = sport_from_form,
			position = position_from_form,
			school = school_from_form,
			birthday = birthday_from_form,
			age = age_from_form,
			height = height_from_form,
			weight = weight_from_form,

			)
		profile_post.put()

		template = jinja_environment.get_template('profileupdated.html')
		self.response.write(template.render(
			{
				'post': profile_post
			}))

class ProfileHandler(webapp2.RequestHandler):
	def get(self):
		

		profilelist = listprofile.query().fetch()
		template = jinja_environment.get_template('profilelist.html')
		self.response.write(template.render(
			{
				'post': profilelist

			}))



app = webapp2.WSGIApplication([
	('/', InfoHandler),
	('/Profile', ProfileHandler),
],debug=True)