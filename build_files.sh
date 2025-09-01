#!/bin/bash
pip3 install -r requirements.txt
python3.9 manage.py collectstatic --noinput

# # Install Python dependencies
# echo "Installing Python dependencies..."
# pip3 install -r requirements.txt

# # Run Django migrations
# echo "Running Django migrations..."
# python3.9 manage.py makemigrations --noinput
# python3.9 manage.py migrate --noinput

# # Collect static files
# echo "Collecting static files..."
# python3.9 manage.py collectstatic --noinput

# echo "Build process completed."