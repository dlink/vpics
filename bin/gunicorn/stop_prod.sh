#!/bin/bash

set -e

PIDFILE='/apps/vpics/web/vpics.pid'

if [ ! -s "$PIDFILE" ]; then
    echo 'Error: vpics Gunicorn is not running'
    exit 1
fi

pid=$(<"$PIDFILE")
if ! kill -0 "$pid" 2>/dev/null; then
    echo "Error: stale vpics PID file ($pid)"
    exit 1
fi

kill -TERM "$pid"
echo 'vpics Gunicorn stop requested'
