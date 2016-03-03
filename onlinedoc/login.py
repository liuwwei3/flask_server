# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import logout_user, login_user, LoginManager, current_user
from onlinedoc import app, User
from onlinedoc.Forms import LoginForm
import os

lm = LoginManager()
lm.init_app(app)


@app.route('/logout')
def logout():
	logout_user()
	return redirect('/index')

@app.route('/login', methods=['GET', 'POST'])
def login():
	print current_user
	if request.method == "GET":
		form = LoginForm()
		return render_template('login.html', form = form)
	else:#form.validate_on_submit():
		user = User.User()
		user.id = request.form['email']
		print "PASSWD:", request.form['passwd']
		login_user(user)
		return redirect("/index")

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

