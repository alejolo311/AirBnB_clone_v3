#!/usr/bin/python3
"""
view for states
"""

from api.v1.views import *
from flask import Flask, jsonify
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False, methods=["GET"])
@app_views.route("/states/<state_id>", methods=["GET"])
def get_state(state_id=None):
    """
        GET Request for States
    """
    if state_id:
        return get_model(State, state_id), 200

    return jsonify([obj.to_dict() for obj in storage.all(State).values()]), 200


@app_views.route("/states/<state_id>", methods=["DELETE"])
def delete_state(state_id):
    """
        DELETE Request for states
    """
    return delete(State, state_id)


@app_views.route("/states", strict_slashes=False, methods=["POST"])
def post_state():
    """
        POST Request for States
    """
    return post(State, None, None, {"name"})


@app_views.route("/states/<state_id>", methods=["PUT"])
def put_state(state_id):
    """
        PUT Request for States
    """
    return put(State, state_id, ["id", "created_at", "updated_at"])
