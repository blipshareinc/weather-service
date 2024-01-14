#!/bin/sh

# source the environment first
if [[ $1 == "prod" ]]; then
    echo "Creating environment ..."
    python3 -m venv .env
    echo "Starting production run ..."
    . .env/bin/activate
    pip3 install -r requirements.txt
fi

cd app
gunicorn --workers ${WORKERS} --bind ${HOST}:${PORT} 'wsgi:app'
