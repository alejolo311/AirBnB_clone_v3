#!/usr/bin/python3
"""
view for states
"""

from api.v1.views import *
from flask import Flask, jsonify
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False, methods=["GET"])
def get_states(state_id=None):
    """Returns a list of all the states
    ---
    tags:
      - States
    paths:
      /states/{id}:
        get:
          parameters:
            - in: path
              name: id   # Note the name is the same as in the path
              required: true
              schema:
                type: integer
                minimum: 1
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


@app_views.route("/states/<state_id>", methods=["GET"])
def get_state_by_id(state_id=None):
    """Returns one state using his ID
    ---
    parameters:
      - name: id
        in: path
        type: string
        required: true
        default: 1
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
    return get_model(State, state_id)


@app_views.route("/states/<state_id>", methods=["DELETE"])
def delete_state_(state_id):
    """Delete a state using his ID
    ---
    parameters:
      - in: path
        name: id   # Note the name is the same as in the path
        required: true
        schema:
          type: integer
          minimum: 1
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
        description: a empty object
      404:
        description: not found any state to delete
        schema:
          error:
            type: string
        examples:
           application/json: { "error": "not found"}
    """
    return delete(State, state_id)


@app_views.route("/states", strict_slashes=False, methods=["POST"])
def post_state_():
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
    return post(State, None, None, {"name"})


@app_views.route("/states/<state_id>", methods=["PUT"])
def put_state_(state_id):
    """Returns a list of all the states
    ---
    parameters:
      - in: path
        name: id   # Note the name is the same as in the path
        required: true
        schema:
          type: integer
          minimum: 1
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
    return put(State, state_id, ["id", "created_at", "updated_at"])
