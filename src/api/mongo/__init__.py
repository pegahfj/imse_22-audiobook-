from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "tweets_db"
mongo = PyMongo(app, config_prefix='MONGO')
APP_URL = "http://127.0.0.1:5000"

