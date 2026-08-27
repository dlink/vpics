#!/bin/bash

PIDFILE='/apps/vpics/web/vpics.pid'

if [ ! -s "$PIDFILE" ]; then
    echo 'vpics Gunicorn is not running'
    exit 1
fi

pid=$(<"$PIDFILE")
if ! kill -0 "$pid" 2>/dev/null; then
    echo "vpics Gunicorn has a stale PID file ($pid)"
    exit 1
fi

echo "vpics Gunicorn is running (PID $pid)"
