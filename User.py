# user and login manager
from flask import g
from flask.ext.login import LoginManager, current_user
from flask.ext.openid import OpenID
from Server import lm, app, oid


class User():
	id = ''
 
	def is_authenticated(self):
		return True
 
	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False
 
	def get_id(self):
		return unicode(self.id)
 
	def __repr__(self):
		return '<User %r>' % (self.id)



