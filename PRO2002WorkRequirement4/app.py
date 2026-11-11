"""Flask application for WR4"""
from flask import Flask
from PRO2002WorkRequirement4.health_api.routes.health_route import health_bp

def create_app() -> Flask:
    """Creates a new Flask application instance"""

    # New Flask application instance
    flask_app = Flask(__name__)

    # Register the health API blueprint on the application
    flask_app.register_blueprint(health_bp)
    return flask_app

# The application instance
app = create_app()

# Direct local run
# "flask_app.run(debug=True)" enables live reloading
#if __name__ == '__main__':
#    app.run(debug=True)
