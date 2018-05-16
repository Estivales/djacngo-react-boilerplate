#!/usr/bin/env bash


until cd src
do
    echo "Waiting for django volume..."
done

until python manage.py migrate --settings=project.settings
do
    echo "Waiting for mariadb ready..."
    sleep 2
done

#python manage.py loaddata fixtures.json --settings=project.settings
python manage.py runserver 0.0.0.0:8000 --settings=project.settings
