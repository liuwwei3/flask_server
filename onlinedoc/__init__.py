from flask import Flask
import pymongo

app = Flask(__name__)
app.config.from_object('config')
mongo_conn = pymongo.MongoClient(host=app.config['MONGO_HOST'], port = app.config['MONGO_PORT'])
db = mongo_conn.olatex

print "__name__ = " + __name__

from onlinedoc import index, login, olatex, omd
