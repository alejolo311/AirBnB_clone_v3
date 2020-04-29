#!/usr/bin/python3
"""
view for states
"""

from api.v1.views import *
from flask import Flask, jsonify
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False, methods=["GET"])
def get_state(state_id=None):
    """Returns a list of all the states
    ---
    tags:
      - States
    definitions:
      State:
        type: object
        properties:
          id:
            type: string
          name:
            type: string
          created_at:
            type: string
          updated_at:
            type: string
    responses:
      200:
        description: a list of states
        schema:
          $ref: '#/definitions/State'
        examples:
          application/json: { "id": 02047f77-f223-47e5-93cc-6eff833ea7e9,
                              "name": "california",
                              "created_at": "2020-04-27T15:27:20.000000",
                              "updated_at": "2020-04-27T15:27:20.000000"}
      404:
        description: not found any state
        schema:
          error:
            type: string
        examples:
           application/json: { "error": "not found"}
    """
    if state_id:
        return get_model(State, state_id)

    return jsonify([obj.to_dict() for obj in storage.all("State").values()])


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
