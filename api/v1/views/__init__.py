#!/usr/bin/python3
"""
Initializzation Module
"""

from flask import Blueprint

app_views = Blueprint("views", __name__, url_prefix='/api/v1')

from .index import *
from .states import *
