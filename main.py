from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
from app.routes.guru import guru_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(guru_routes)
