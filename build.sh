#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Set superuser credentials securely
export DJANGO_SUPERUSER_EMAIL="hamza@admin.com"
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_PASSWORD="Grandfucker1945"
# Create the superuser
python manage.py createsuperuser2  --password "Grandfucker1945" --username "admin" --email "hamza@admin.com" --noinput || echo "Superuser already exists."
