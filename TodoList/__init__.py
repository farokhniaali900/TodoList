from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__ , template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = 'SOME SECRETS'
db = SQLAlchemy(app)

from TodoList import routes