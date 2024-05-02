#!/usr/bin/python3
"""
Initializzation Module
"""

from flask import Blueprint
from .index import *

app_views = Blueprint("views", __name__)

@app_views.route("/")
def app_views():
    return "App views"
