# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import logout_user, login_user, LoginManager, current_user
from flask.ext.openid import OpenID

app = Flask(__name__)
#app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, './tmp')

import User
import os
import latex
from Forms import LoginForm

@app.route('/')
@app.route('/index')
def hello():
	args = {}
	args['location'] = 'home'
	return render_template('index.html', args=args)

@app.route('/generate_md', methods=['GET', 'POST'])
def generate_md():
	if request.method=='GET':
		return "<center><h1>HELLO</h1></md>"
	else:
		script = '''<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>'''
		return script + "<body>" + markdown.markdown(request.form['data']) + "</body>"

@app.route('/md_input')
def md_input():
	return render_template('md_pages/md_input.html')

@app.route('/blogs')
def blogs():
	args = {}
	args['location'] = 'blogs'
	return render_template('blogs.html', args=args)

@app.route('/input')
def input_page():
	print "current_user: ", current_user
	return render_template('input.html')

@app.route('/movie')
def movie():
	return render_template('movie.html')

@app.route("/refresh", methods=['post'])
def refresh():
	data = request.form['data']
	dir = os.path.abspath(os.path.dirname(__file__))
	pdf = latex.build_pdf(data, texinputs=[dir, ''])
	fs = open('static/_temp.pdf', 'w')
	fs.write(bytes(pdf))
	fs.close()
	return redirect("/static/_temp.pdf")

@app.route('/latex')
def latex_online():
	return render_template('latex.html')

@app.route('/md')
def md_main():
	return render_template('md_pages/md.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect('/index')

@app.route('/myinfo')
def myinfo():
	if current_user.id:
		return render_template('myinfo.html', args = {"location": "myinfo"})
	else:
		return "not login yet"

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

if __name__=="__main__":
	app.run(port=8765, debug=True)



