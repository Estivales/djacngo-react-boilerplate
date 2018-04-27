#!/bin/bash
docker-compose run web pipenv install django
docker-compose run web pipenv run django-admin.py startproject $1 .