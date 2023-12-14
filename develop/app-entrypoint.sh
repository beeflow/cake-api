#!/usr/bin/env bash
set -e

echo "Migrating..."

python manage.py makemigrations
python manage.py migrate

echo "Collect static..."
python manage.py collectstatic --no-input

exec "$@"
