#!/usr/bin/python3
"""
User model
"""
from . import app_views
from flask import abort, jsonify, request
from models import storage
from models.user import User


@app_views.route("/users", methods=['GET'])
def list_user(exception):
    """list users"""
    all_users = []
    for user in storage.all(User).values():
        all_users.append(user)

    return jsonify([user.to_dict() for user in all_users])


@app_views.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    """get a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    """delete a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    return jsonify({}), 200


@app_views.route("/users", methods=['POST'])
def add_user(exception):
    """add a user"""
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    if 'email' not in request.json:
        abort(400)
        return jsonify({"error": "Missing email"})
    if 'password' not in request.json:
        abort(400)
        return jsonify({"error": "Missing password"})
    new_s = User(**request.get_json())
    new_s.save()
    return jsonify(new_s.to_dict()), 201



@app_views.route("/users/<user_id>", methods=['POST'])
def update_user(user_id):
    """update a user"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())
