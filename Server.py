# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import login_user, LoginManager, current_user
from flask.ext.openid import OpenID

app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, './tmp')

import User
import os
import latex
from Forms import LoginForm

@app.route('/')
def hello():
	return "<h1>Hello!</h1>"

@app.route('/input')
def input_page():
	print "current_user: ", current_user
	return render_template('input.html')

@app.route('/movie')
def movie():
	return render_template('movie.html')

@app.route("/refresh2", methods=['post'])
def refresh2():
	data = request.form['data']
	fs = open('_temp', 'w')
	fs.write(data)
	fs.close()
	os.system('latexmk -pdf _temp; cp _temp.pdf static/')
	return redirect("/static/_temp.pdf")

@app.route("/refresh", methods=['post'])
def refresh():
	data = request.form['data']
	pdf = latex.build_pdf(data)
	fs = open('static/_temp.pdf', 'w')
	fs.write(bytes(pdf))
	fs.close()
	return redirect("/static/_temp.pdf")

@app.route('/latex')
def latex_online():
	return render_template('latex.html')


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
	print current_user
	if request.method == "GET":
		form = LoginForm()
		return render_template('login.html', form = form)
	else:#form.validate_on_submit():
		user = User.User()
		user.id = request.form['email']
		login_user(user)
		return "GOOD LOGIN : " + user.id

@app.route('/check')
def check():
	return 

@lm.user_loader
def load_user(id):
	print "LOAD user: " + str(id)
	user = User.User()
	user.id = id
	return user

@lm.request_loader
def request_loader(request):
	id = request.form.get('email')
	print "request_loader : "+ str(id)
	user = User.User()
	user.id = id
	return user

if __name__=="__main__":
	app.run(port=8765, debug=True)



