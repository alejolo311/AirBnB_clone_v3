#!/usr/bin/python3
"""
view for Place
"""

from api.v1.views import *
from flask import Flask, jsonify
from models import storage
from models.city import City
from models.place import Place


@app_views.route("/cities/<city_id>/places", strict_slashes=False,
                 methods=["GET"])
def get_places(city_id):
    """
        GET Request all places in a city
    """
    return parent_model(City, city_id, "places")


@app_views.route("/places/<place_id>", strict_slashes=False, methods=["GET"])
def get_place(place_id):
    """
        GET Request for a place
    """
    return get_model(Place, place_id)


@app_views.route("/places/<place_id>", methods=["DELETE"])
def delete_place(place_id):
    """
        DELETE Request for a place
    """
    return delete(Place, place_id)


@app_views.route("/cities/<city_id>/places", strict_slashes=False,
                 methods=["POST"])
def post_place(city_id):
    """
        POST Request for a place
    """
    return post(Place, City, city_id, {"name", "user_id"})


@app_views.route("/places/<place_id>", methods=["PUT"])
def put_place(place_id):
    """
        PUT Request for a city
    """
    return put(Place, place_id, ["id", "created_at", "updated_at", "user_id",
               "city_id"])
