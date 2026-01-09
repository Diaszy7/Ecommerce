#!/usr/bin/env bash
gunicorn loja.wsgi:application --bind 0.0.0.0:$PORT
