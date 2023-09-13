from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '91b40d208c37c1f100d88c85'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes