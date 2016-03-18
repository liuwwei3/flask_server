# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import logout_user, login_user, LoginManager, current_user
from onlinedoc import app, User, db
from onlinedoc.Forms import LoginForm
import os
from Mailer import send_mail
import random
import time
import json

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
	else:
		form = LoginForm()
		print "VALID:", form.validate_on_submit()
		user = User.User()
		user.id = request.form['email']
		passwd = request.form['passwd']
		logres = user.verify(passwd)
		if logres == 1:
			login_user(user)
			return redirect("/index")
		elif logres == 0:
			return "密码错误！"
		else:
			return "没有此用户"

@app.route("/register", methods=['POST'])
def register():
	email = request.form['email']
	if db.users.find_one({"_id":email}):
		return "此用户已存在"
	pw1 = request.form['passwd']
	pw2 = request.form['repasswd']
	yanzheng = request.form['yanzheng']
	if pw1 != pw2:
		return "两次密码不一致"
	data = db.reg.find_one({"_id":email})
	now = time.time()
	if now - data['time'] > 3600:
		return "验证码超时"
	if yanzheng != data['num']:
		return "验证码错误"
	user = User.User()
	user.id = request.form['email']
	user.save(pw1)
	login_user(user)
	return redirect('/index')
			
@app.route("/yanzheng", methods=['POST'])
def yanzhengma():
	print "now yanzhenging ... "
	print request.values['email']
	email = request.values['email']
	num = str(int(random.random() * 10000))
	res = send_mail(email, num)
	if json.loads(res)['message'] == 'error':
		return "发送失败"
	db.reg.save({"_id": email, "time": time.time(), "num" : num})
	return "发送成功"


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

