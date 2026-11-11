"""Defines the health API endpoint for WR4"""
from flask import Blueprint, jsonify

# Creating a variable that groups a health related routes with the "/health" URL prefix
health_bp = Blueprint("health", __name__, url_prefix="/health")

# Creates a GET endpoint at "/health"
@health_bp.get('')
def get_status():
    """Return the API health status with the HTTP status code 200"""
    return jsonify({'status': 'ok'}), 200
