# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
from flask.ext.login import current_user
import os
from onlinedoc import app, db
import pymongo
import time

@app.route('/')
@app.route('/index')
def index():
	args = {}
	args['location'] = 'home'
	blog_list = []
	if current_user.id:
		blog_list = [x for x in db.blogs.find({"user" : str(current_user.id) })]
		for ele in blog_list:
			ele['update_time'] = time.strftime("%Y-%m-%d",  time.localtime(ele['update_time']))
	return render_template('index.html', args=args, blogs = blog_list)

@app.route('/blogs')
def blogs():
	args = {}
	args['location'] = 'blogs'
	return render_template('blogs.html', args=args)

@app.route('/movie')
def movie():
	return render_template('movie.html')

@app.route('/myinfo')
def myinfo():
	if current_user.id:
		return render_template('myinfo.html', args = {"location": "myinfo"})
	else:
		return "not login yet"

