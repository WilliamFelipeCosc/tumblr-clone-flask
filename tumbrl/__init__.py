from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = 'p128edyiKASkasjnHLhnsdsxp197278619xkjhka'
app.config["UPLOAD_FOLDER"] = 'static/fotos_dos_posts'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap5(app)

login_manager = LoginManager(app)
# login_manager.login_view = 'homepage'

from tumbrl import routes

