# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import logout_user, login_user, LoginManager, current_user
from onlinedoc import app, db
import os
import latex
import time
import urllib
dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/input')
def input_page():
	project = request.args.get('project')
	print "current_user: ", current_user
	data = db.blogs.find_one({"user": str(current_user.id), "project": project })
	if not data:
		data = ''
	else:
		data = data['data']
	return render_template('input.html', project=project, data = data)

@app.route("/refresh", methods=['post'])
def refresh():
	data = request.form['data']
	dir = os.path.abspath(os.path.dirname(__file__))
	pdf = latex.build_pdf(data, texinputs=[dir, ''])
	project = request.form['project'].encode('utf-8')
	filename = str(current_user.id) + '_' + project
	db.blogs.save({"_id": filename, "user": str(current_user.id), \
		"project": project, "update_time": time.time() , "data": data})
	fs = open(dir + '/static/'+filename+'.pdf', 'w')
	fs.write(bytes(pdf))
	fs.close()
	return redirect(urllib.quote("/static/"+filename+".pdf"))

@app.route("/gen_pdf")
def gen_pdf():
	project = request.args.get('project')
	data = db.blogs.find_one({"user": str(current_user.id), "project": project })
	if not data:
		return redirect("/static/basic.pdf")
	else:
		data = data['data']
		dir = os.path.abspath(os.path.dirname(__file__))
		pdf = latex.build_pdf(data, texinputs=[dir, ''])
		filename = str(current_user.id) + '_' + project.encode('utf-8')
		fs = open(dir + '/static/'+filename+'.pdf', 'w')
		fs.write(bytes(pdf))
		fs.close()
		return redirect(urllib.quote("/static/"+filename+".pdf"))
	

@app.route('/latex')
def latex_online():
	project = request.args.get('project')
	if not project:
		return "<h1>Invalid Project Name<h1>"
	#print "PROJECT: ",project
	return render_template('latex.html', project = project)


