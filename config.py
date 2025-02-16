import os


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "your_secret_key"
    )  # Replace with a strong, random key
    JWT_SECRET_KEY = (
        os.environ.get("JWT_SECRET_KEY") or "your_jwt_secret_key"
    )  # Replace with a strong, random key
    DATABASE_URL = (
        os.environ.get("DATABASE_URL")
        or "postgresql://user:password@host:port/database"
    )  # Replace!

    # Add other configuration variables as needed
    # Example:
    # UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'uploads'
    # MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.example.com'

    # Configuration for different environments (optional but recommended)
    class DevelopmentConfig(Config):
        DEBUG = True  # Enable debugging in development

    class TestingConfig(Config):
        TESTING = True

    class ProductionConfig(Config):
        DEBUG = False


# Choose the active configuration
config_name = os.environ.get("FLASK_CONFIG") or "development"  # Default to development
config = {
    "development": Config.DevelopmentConfig,
    "testing": Config.TestingConfig,
    "production": Config.ProductionConfig,
}.get(config_name)

# Make sure config is set even if the environment variable is not defined
if not config:
    config = Config.DevelopmentConfig
