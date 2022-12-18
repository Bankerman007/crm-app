from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY']= 'r46ttr29ara'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://yamacrxc:DaRyQOt9c4ZXMIr09J4KvN5RreIU4JsR@raja.db.elephantsql.com/yamacrxc' #'sqlite:///site.db'
db = SQLAlchemy(app)
#migrate = Migrate(app, db)


bcrypt=Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category= 'info'

from crm_app import routes

