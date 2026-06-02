"""
Land Intelligence Platform - Main Application Entry Point.
A premium GIS intelligence web application for real estate investors.
"""

from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
from config import Config
from firebase import init_firebase

# Import route blueprints
from routes.auth_routes import auth_bp
from routes.analysis_routes import analysis_bp
from routes.report_routes import report_bp
from routes.user_routes import user_bp


def create_app():
    """Application factory."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Initialize Firebase
    init_firebase()

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(user_bp)

    # ── Page Routes ──────────────────────────────────────────────

    @app.route('/')
    def landing():
        """Landing page."""
        return render_template('landing.html')

    @app.route('/login')
    def login_page():
        """Login/Register page."""
        return render_template('auth.html')

    @app.route('/register')
    def register_page():
        """Register page (redirects to auth with register mode)."""
        return render_template('auth.html', mode='register')

    @app.route('/dashboard')
    def dashboard_page():
        """User dashboard."""
        return render_template('dashboard.html')

    @app.route('/analyze')
    def analysis_page():
        """Land analysis page."""
        return render_template('analysis.html')

    @app.route('/reports')
    def reports_page():
        """Saved reports page."""
        return render_template('reports.html')

    @app.route('/profile')
    def profile_page():
        """User profile page."""
        return render_template('profile.html')

    # ── Error Handlers ───────────────────────────────────────────

    @app.errorhandler(400)
    def bad_request(e):
        return {'error': 'Bad request'}, 400

    @app.errorhandler(401)
    def unauthorized(e):
        return {'error': 'Unauthorized'}, 401

    @app.errorhandler(403)
    def forbidden(e):
        return {'error': 'Forbidden'}, 403

    @app.errorhandler(404)
    def not_found(e):
        return render_template('landing.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        return {'error': 'Internal server error'}, 500

    return app


# Create the application instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=5000)
