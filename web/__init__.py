from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

from web import routes

client = MongoClient('localhost', 1337)

db = client.flask_db
todos = db.todos



