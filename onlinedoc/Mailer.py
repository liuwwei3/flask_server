#!/usr/bin/python
#coding:utf-8
import requests, json


def send_mail(to, content):       
	url="http://sendcloud.sohu.com/webapi/mail.send.json"
	params = {"api_user": "liuwwei3_test_dMVK6e", \
    "api_key" : "J3piTy9YEzqC1G2D",\
    "from" : "no-replay@onlatex.com", \
    "to" : to, \
    "subject" : "请激活您的邮箱", \
    "html": "hello，欢迎加入我们! 为了保证您正常使用我们的功能，请激活账号。验证码："+content, \
    "resp_email_id": "true"
	}
  
	r = requests.post(url, files={}, data=params)
	print r.text
	return  r.text


if __name__=="__main__":
	send_mail("810721065@qq.com", "hello，欢迎加入我们! 为了保证您正常使用我们的功能，请激活账号。验证码：123456")

