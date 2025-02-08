#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
export DJANGO_SUPERUSER_EMAIL=hamza@admin.com
export DJANGO_SUPERUSER_PASSWORD=Grandfucker1945
python manage.py createsuperuser --no-input
Superuser created successfully.