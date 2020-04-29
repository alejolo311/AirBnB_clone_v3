#!/usr/bin/python3
"""
view for states
"""

from api.v1.views import *
from flask import Flask, jsonify
from models import storage
from models.state import State
from flasgger import swag_from


@app_views.route("/states", strict_slashes=False, methods=["GET"])
@swag_from('../doc/states/get.yml')
def get_state(state_id=None):
    """
        GET Request for States
    """
    return jsonify([obj.to_dict() for obj in storage.all("State").values()])


@app_views.route("/states/<state_id>", methods=["GET"])
@swag_from('../doc/states/getById.yml')
def get_state_by_id(state_id=None):
    """
        GET Request for States
    """
    if state_id:
        return get_model(State, state_id)


@app_views.route("/states/<state_id>", methods=["DELETE"])
@swag_from('../doc/states/delete.yml')
def delete_state(state_id):
    """
        DELETE Request for states
    """
    return delete(State, state_id)


@app_views.route("/states", strict_slashes=False, methods=["POST"])
@swag_from('../doc/states/post.yml')
def post_state():
    """
        POST Request for States
    """
    return post(State, None, None, {"name"})


@app_views.route("/states/<state_id>", methods=["PUT"])
@swag_from('../doc/states/put.yml')
def put_state(state_id):
    """
        PUT Request for States
    """
    return put(State, state_id, ["id", "created_at", "updated_at"])
