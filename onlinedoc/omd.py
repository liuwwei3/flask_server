# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import logout_user, login_user, LoginManager, current_user
from onlinedoc import app
import os
import markdown

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

@app.route('/md')
def md_main():
	return render_template('md_pages/md.html')


