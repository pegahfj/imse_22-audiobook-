#!/bin/sh

echo "Waiting for postgres..."
python manage.py initdb

echo "PostgreSQL started"
echo "---------------------app--------------------"

python manage.py run -h 0.0.0.0