from flask.ext.wtf import Form 
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):

	remeber_me = BooleanField('RemeberMe', default = False)
