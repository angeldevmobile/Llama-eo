from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
from app.routes.guru import guru_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(guru_routes)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
