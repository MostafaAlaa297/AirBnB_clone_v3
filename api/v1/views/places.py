#!/usr/bin/python3
"""
Place model
"""
from . import app_views
from flask import abort, jsonify, request
from models import storage
from models.place import Place


@app_views.route("/places", methods=['GET'])
def list_place(exception):
    """list places"""
    all_places = []
    for place in storage.all(Place).values():
        all_places.append(place)

    return jsonify([place.to_dict() for place in all_places])


@app_views.route("/places/<place_id>", methods=['GET'])
def get_place(place_id):
    """get a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>", methods=['DELETE'])
def delete_place(place_id):
    """delete a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    return jsonify({}), 200


@app_views.route("/places", methods=['POST'])
def add_place(exception):
    """add a place"""
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    if 'name' not in request.json:
        abort(400)
        return jsonify({"error": "Missing name"})
    new_s = Place(**request.get_json())
    new_s.save()
    return jsonify(new_s.to_dict()), 201



@app_views.route("/places/<place_id>", methods=['POST'])
def update_place(place_id):
    """update a place"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict())
