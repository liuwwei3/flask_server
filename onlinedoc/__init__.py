from flask import Flask

app = Flask(__name__)

print "__name__ = " + __name__

from onlinedoc import index, login, olatex, omd
