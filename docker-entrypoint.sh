#!/bin/bash

# Collect static files
echo "Collect static files"
env/bin/python3 immersivetech/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
env/bin/python3 immersivetech/manage.py migrate

# Start server
# echo "Starting server"
# env/bin/python3 immersivetech/manage.py runserver 0.0.0.0:8000
