#!/usr/bin/python3
"""
app module
"""

from flask import Flask
from flask import Blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix="/api/v1")

@app.teardown_appcontext
def teardown():
    storage.close()

if __name__ == "__main__":
    app.run(host=HBNB_API_HOST or "0.0.0.0", port=HBNB_API_PORT or "5000", threaded=True)
