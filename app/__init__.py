from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# load file config
app.config.from_object(Config)

# create + initialize instance cho DB va DB migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login 
login = LoginManager(app)
# requiring user to login
login.login_view = 'login'

# print(__name__)
from app import routes, models