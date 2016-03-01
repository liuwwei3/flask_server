# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import logout_user, login_user, LoginManager, current_user
from onlinedoc import app
import os
import latex
dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/input')
def input_page():
	print "current_user: ", current_user
	return render_template('input.html')

@app.route("/refresh", methods=['post'])
def refresh():
	data = request.form['data']
	dir = os.path.abspath(os.path.dirname(__file__))
	pdf = latex.build_pdf(data, texinputs=[dir, ''])
	filename = str(current_user.id)
	fs = open(dir + '/static/'+filename+'.pdf', 'w')
	fs.write(bytes(pdf))
	fs.close()
	return redirect("/static/"+filename+".pdf")

@app.route('/latex')
def latex_online():
	return render_template('latex.html')


