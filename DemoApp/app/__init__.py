from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'y5qytq8757638265uiawsfgouahiuw9058u90y,.l'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)