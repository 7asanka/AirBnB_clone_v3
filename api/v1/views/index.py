#!/usr/bin/python3
"""index.py"""

from api.v1.views import app_views
from flask import jsonify


@app_viesw.route('/status', strict_slashes=False)
def status():
    """returns status"""
    return jsonify({"status": "OK"})
