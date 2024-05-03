#!/usr/bin/python3
"""
State model
"""
from . import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State


@app_views.route("/states", methods=['GET'])
def list_state(exception):
    """list states"""
    all_states = []
    for state in storage.all(State).values():
        all_states.append(state)

    return jsonify([state.to_dict() for state in all_states])


@app_views.route("/states/<state_id>", methods=['GET'])
def get_state(state_id):
    """get a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state(state_id):
    """delete a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return jsonify({}), 200


@app_views.route("/states", methods=['POST'])
def add_state(exception):
    """add a state"""
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    if 'name' not in request.json:
        abort(400)
        return jsonify({"error": "Missing name"})
    new_s = State(**request.get_json())
    new_s.save()
    return jsonify(new_s.to_dict()), 201



@app_views.route("/states/<state_id>", methods=['POST'])
def update_state(state_id):
    """update a state"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
