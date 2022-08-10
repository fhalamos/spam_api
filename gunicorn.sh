#!/bin/sh
gunicorn main:app --access-logfile /var/tmp/gunicorn.logs -w 2 --threads 2 -b 0.0.0.0:8001


