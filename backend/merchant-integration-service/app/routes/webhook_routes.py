from flask import Blueprint, jsonify, request
from app.models.webhook import Webhook
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import urlparse

webhook_bp = Blueprint('webhook', __name__)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@webhook_bp.route('/webhooks/user/<int:user_id>', methods=['GET'])
def get_webhooks(user_id):
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    webhooks = Webhook.query.filter_by(user_id=user_id).all()
    webhooks_data = [webhook.json() for webhook in webhooks]
    return jsonify({'webhooks': webhooks_data}), 200

@webhook_bp.route('/webhooks', methods=['POST'])
def create_webhook():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    user_id = data.get('user_id')
    url = data.get('url')

    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    if not url:
        return jsonify({'error': 'url is required'}), 400
    if not is_valid_url(url):
        return jsonify({'error': 'Invalid URL format'}), 400

    try:
        new_webhook = Webhook(user_id=user_id, url=url)
        db.session.add(new_webhook)
        db.session.commit()
        return jsonify(new_webhook.json()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@webhook_bp.route('/webhooks/<int:webhook_id>', methods=['GET'])
def get_webhook(webhook_id):
    webhook = Webhook.query.get(webhook_id)
    if not webhook:
        return jsonify({'error': 'Webhook not found'}), 404
    return jsonify(webhook.json()), 200

@webhook_bp.route('/webhooks/<int:webhook_id>', methods=['PUT'])
def update_webhook(webhook_id):
    webhook = Webhook.query.get(webhook_id)
    if not webhook:
        return jsonify({'error': 'Webhook not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No URL data provided'}), 400

    new_url = data.get('url')
    if not new_url:
        return jsonify({'error': 'url is required'}), 400
    if not is_valid_url(new_url):
        return jsonify({'error': 'Invalid URL format'}), 400

    try:
        webhook.url = new_url
        db.session.commit()
        return jsonify(webhook.json()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@webhook_bp.route('/webhooks/<int:webhook_id>', methods=['DELETE'])
def disable_webhook(webhook_id):
    webhook = Webhook.query.get(webhook_id)

    if not webhook:
        return jsonify({'error': 'Webhook is required'}), 400

    if not webhook.is_active:
        return jsonify({'error': 'Webhook is already inactive'}), 400

    webhook.is_active = False
    db.session.commit()

    return jsonify({'message': 'Webhook revoked successfully'}), 200
