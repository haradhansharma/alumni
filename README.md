# Project Structure
This document provides an overview of the project structure.

## Table of Contents
- [Backend](#backend)
- [Backups](#backups)
- [Cronjobs](#cronjobs)
- [Frontend](#frontend)
- [NGINX](#nginx)
- [Other Files](#other-files)

## Backend
Django Rest API project
```
backend
|-- Dockerfile
|-- Pipfile
|-- Pipfile.lock
|-- abackend
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- account
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- alumapi
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- common
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- logs
|   `-- all_logs.log
|-- manage.py
|-- media
|-- pytest.ini
|-- requirements.txt
|-- start-reload.sh
|-- static
|-- templates
`-- test
    |-- __init__.py
    |-- test_models.py
    `-- test_views.py

9 directories, 36 files
```

## Backups
Postgrey SQL backup and restore system by cronjob service
```
backups
|-- backup.sh
`-- restore.sh

0 directories, 2 files
```

## Cronjobs
Periodicly backing up postgre database
```
cronjob
|-- Dockerfile
`-- backup.sh

0 directories, 2 files
```

## Frontend
Vue Project For Frontend
```
frontend
|-- .gitignore
|-- Dockerfile
|-- README.md
|-- babel.config.js
|-- jsconfig.json
|-- package-lock.json
|-- package.json
|-- public
|   |-- favicon.ico
|   `-- index.html
|-- src
|   |-- App.vue
|   |-- assets
|   |   `-- logo.png
|   |-- components
|   |   `-- HelloWorld.vue
|   `-- main.js
`-- vue.config.js

4 directories, 14 files
```

## NGINX
Serving frontend and backend service by this nginx
```
nginx
|-- Dockerfile
|-- nginx.conf
`-- ssl
    |-- ssl-cert.crt
    `-- ssl-cert.key

1 directory, 4 files
```

## Other Files
```
.
|-- .dockerignore
|-- .env
|-- .gitignore
|-- README.md
|-- acmd.py
|-- backend_comments.md
|-- backup_comments.md
|-- cronjob_comments.md
|-- docker-compose.yml
|-- essential_commands.txt
|-- frontend_comments.md
|-- generate_comments.sh
|-- generate_structure.sh
`-- nginx_comments.md

0 directories, 14 files
```

