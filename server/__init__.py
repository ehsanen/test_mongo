from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
mongo_client = MongoClient()
db = mongo_client.test_database

from server.mod_user.controllers import mod_user as user_module

app.register_blueprint(user_module)
