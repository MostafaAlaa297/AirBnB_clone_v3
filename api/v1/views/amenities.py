#!/usr/bin/python3
"""
Amenity model
"""
from . import app_views
from flask import abort, jsonify, request
from models import storage
from models.amenity import Amenity


@app_views.route("/amenities", methods=['GET'])
def list_amenity(exception):
    """list amenities"""
    all_amenities = []
    for amenity in storage.all(Amenity).values():
        all_amenities.append(amenity)

    return jsonify([amenity.to_dict() for amenity in all_amenities])


@app_views.route("/amenities/<amenity_id>", methods=['GET'])
def get_amenity(amenity_id):
    """get a amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route("/amenities/<amenity_id>", methods=['DELETE'])
def delete_amenity(amenity_id):
    """delete a amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    return jsonify({}), 200


@app_views.route("/amenities", methods=['POST'])
def add_amenity(exception):
    """add a amenity"""
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    if 'name' not in request.json:
        abort(400)
        return jsonify({"error": "Missing name"})
    new_s = Amenity(**request.get_json())
    new_s.save()
    return jsonify(new_s.to_dict()), 201



@app_views.route("/amenities/<amenity_id>", methods=['POST'])
def update_amenity(amenity_id):
    """update a amenity"""
    amenity = storage.get('Amenity', amenity_id)
    if amenity is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict())
