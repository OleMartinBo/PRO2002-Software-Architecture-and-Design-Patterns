"""Flask application for WR4"""
from flask import Flask
from .health_api.routes.health_route import health_bp

def create_app() -> Flask:
    """Creates a new Flask application instance"""

    # New Flask application instance
    flask_app = Flask(__name__)

    # Register the health API blueprint on the application
    flask_app.register_blueprint(health_bp)
    return flask_app

# The application instance
app = create_app()
