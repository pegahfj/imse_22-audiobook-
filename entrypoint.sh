#!/bin/sh

echo "Waiting for postgres..."
python cli_manager.py initdb

echo "PostgreSQL started"
echo "---------------------app--------------------"

python cli_manager.py run -h 0.0.0.0