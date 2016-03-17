# user and login manager
from onlinedoc import db
from werkzeug.security import generate_password_hash, check_password_hash

class User():
	id = ''

	def verify(self, passwd):
		'''
		return 
			1: sucess
			0: error password
			-1: no such user
		'''
		data = db.users.find_one({"_id": self.id})
		if data:
			if check_password_hash(data['passwd'], passwd):
				return 1
			else:
				return 0
		return -1
	
	def save(self, passwd):
		hashpw = generate_password_hash(passwd)
		db.users.save({"_id": self.id, "passwd": hashpw})

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



