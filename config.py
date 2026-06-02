"""
Configuration module for Land Intelligence Platform.
Loads environment variables and provides application settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # Flask
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'land-intel-dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    # Firebase
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH', 'serviceAccountKey.json')

    # NASA API
    NASA_API_KEY = os.getenv('NASA_API_KEY', 'DEMO_KEY')
    NASA_EARTH_IMAGERY_URL = 'https://api.nasa.gov/planetary/earth/imagery'
    NASA_EARTH_ASSETS_URL = 'https://api.nasa.gov/planetary/earth/assets'

    # External APIs
    NOMINATIM_BASE_URL = 'https://nominatim.openstreetmap.org'
    OVERPASS_API_URL = 'https://overpass-api.de/api/interpreter'
    OPEN_ELEVATION_URL = 'https://api.open-elevation.com/api/v1/lookup'

    # Cache settings (seconds)
    CACHE_TTL_GEOCODING = 3600       # 1 hour
    CACHE_TTL_SATELLITE = 86400      # 24 hours
    CACHE_TTL_INFRASTRUCTURE = 3600  # 1 hour
    CACHE_TTL_ELEVATION = 86400      # 24 hours

    # Analysis defaults
    INFRASTRUCTURE_SEARCH_RADIUS = 5000  # meters
    DEFAULT_MAP_CENTER = [20.5937, 78.9629]  # India center
    DEFAULT_MAP_ZOOM = 5
