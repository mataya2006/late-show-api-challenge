from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required 
from server.app import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST']) [cite: 7]
@jwt_required() 
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not all([rating, guest_id, episode_id]):
        return jsonify({"message": "Missing required fields"}), 400
    if not (1 <= rating <= 5):
        return jsonify({"message": "Rating must be between 1 and 5"}), 400
    if not Guest.query.get(guest_id):
        return jsonify({"message": f"Guest with ID {guest_id} not found"}), 404
    if not Episode.query.get(episode_id):
        return jsonify({"message": f"Episode with ID {episode_id} not found"}), 404

    new_appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )
    db.session.add(new_appearance)
    db.session.commit()

    return jsonify({
        'id': new_appearance.id,
        'rating': new_appearance.rating,
        'guest_id': new_appearance.guest_id,
        'episode_id': new_appearance.episode_id
    }), 201

# Optiona