#!/usr/bin/python3
"""
index route for flask app
"""

from models import storage
from api.v1.views import app_views, Amenity, City, Place, Review, State, User
from flask import Flask, jsonify


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """return the status"""
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def stats():
    """send json with the count of objects"""
    counts = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(counts), 200
