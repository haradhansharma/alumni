#!/bin/sh

watchmedo auto-restart --directory=/app --pattern=*.py --recursive -- daphne -b 0.0.0.0 -p 8000 abackend.asgi:application
