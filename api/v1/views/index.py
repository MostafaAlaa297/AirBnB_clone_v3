#!/usr/bin/python3
"""
Index Module
"""
from flask import Blueprint

index_views = Blueprint("index", __name__)


@index_views.route("/status")
def status():
    return {
            "status": "OK"
            }
