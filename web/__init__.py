from flask import Flask
from flask_pymongo import PyMongo



app = Flask(__name__)

#Secret key
app.config["SECRET_KEY"] = '72109ede3972aab8'

#database for the admin to access
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@cluster0.udzlyml.mongodb.net/myFirstDb?retryWrites=true&w=majority"

#Set up Mongo db
mongodb_client = PyMongo(app)
#db = mongodb_client.db
from web import routes





