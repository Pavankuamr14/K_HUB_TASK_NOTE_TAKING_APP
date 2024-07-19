import secrets
from decouple import config, write_dotenv

# Generate secret keys
jwt_secret_key = secrets.token_urlsafe(32)
jwt_refresh_secret_key = secrets.token_urlsafe(32)

# Write to .env file
write_dotenv(
    ".env",
    JWT_SECRET_KEY=jwt_secret_key,
    JWT_REFRESH_SECRET_KEY=jwt_refresh_secret_key,
)
