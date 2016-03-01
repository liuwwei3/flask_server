# coding:utf-8

from flask import g, flash, session, Flask, redirect, url_for, render_template, request
import os
from onlinedoc import app

app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
	args = {}
	args['location'] = 'home'
	return render_template('index.html', args=args)

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

