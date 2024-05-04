#!/usr/bin/python3
"""
Place model
"""
from . import app_views
from flask import abort, jsonify, request
from models import storage
from models.place import Place
from models.review import Review


@app_views.route("/places/<place_id>/reviews", methods=['GET'])
def list_place(exception):
    """list reviews"""
    all_reviews = []
    for review in storage.all(Review).values():
        all_review.append(review)
    return jsonify([review.to_dict() for review in all_reviews])


@app_views.route("/reviews/<review_id>", methods=['GET'])
def get_place(review_id):
    """get a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())



@app_views.route("/reviews/<review_id>", methods=['DELETE'])
def delete_place(review_id):
    """delete a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    return jsonify({}), 200


@app_views.route("/places/<place_id>/reviews", methods=['POST'])
def add_place(exception):
    """add a review"""
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    if 'name' not in request.json:
        abort(400)
        return jsonify({"error": "Missing name"})
    data = request.get_json()
    data['place_id'] = place_id
    new_c = Review(**data)
    new_c.save()
    return jsonify(new_c.to_dict()), 201


@app_views.route("/reviews/<review_id>", methods=['POST'])
def update_place(review_id):
    """update a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(place.to_dict())
