#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py \
    --callable app --stats 0.0.0.0:9191
else
  echo "Running Production Server"
  exec python "identidock.py"
fi