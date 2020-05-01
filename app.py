from flask import Flask, render_template
import os
from os import path
if path.exists("env.py"):
  import env 
SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')


APP = Flask(__name__)

@APP.route('/')
def hello_world():
    return render_template('pages/index.html', title="The Lazy Padwan and his lost Son, 70 camels, 50 lambs, and young Jesus")
@APP.route('/<name>')
def hello_user(name):
    return render_template('pages/name.html', title="The Lazy Padwan and his lost Son", submittedName=name)
    

if __name__ == '__main__':
    APP.run(host=os.environ.get('HOSTNAME'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEV'))