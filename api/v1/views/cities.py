#!/usr/bin/python3
"""
State model
"""
from . import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=['GET'])
def list_state(exception):
    """list cities"""
    all_cities = []
    for city in storage.all(City).values():
        all_city.append(city)
    return jsonify([city.to_dict() for city in all_cities])


@app_views.route("/cities/<city_id>", methods=['GET'])
def get_state(city_id):
    """get a city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())



@app_views.route("/cities/<city_id>", methods=['DELETE'])
def delete_state(city_id):
    """delete a city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities", methods=['POST'])
def add_state(exception):
    """add a city"""
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    if 'name' not in request.json:
        abort(400)
        return jsonify({"error": "Missing name"})
    data = request.get_json()
    data['state_id'] = state_id
    new_c = City(**data)
    new_c.save()
    return jsonify(new_c.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=['POST'])
def update_state(city_id):
    """update a city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    city.save()
    return jsonify(state.to_dict())
