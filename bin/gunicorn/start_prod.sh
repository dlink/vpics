#!/bin/bash

set -e

cd /apps/vpics
source bin/set_prod_env.sh
export PYTHONPATH='/apps/vpics/lib:/apps/vpics/web'
export SCRIPT_NAME='/sebastianlinkmusic'

cd web
gunicorn --daemon -c gunicorn.conf.py wsgi:app

for attempt in {1..50}; do
    if curl --silent --fail --unix-socket vpics.sock \
            http://localhost/sebastianlinkmusic/ >/dev/null; then
        echo 'vpics Gunicorn successfully started'
        exit 0
    fi
    sleep 0.1
done

echo 'Error: vpics Gunicorn did not become ready' >&2
exit 1
