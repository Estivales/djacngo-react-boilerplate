# A Docker Compose to set up and run a Django/MariaDB/Redis app, with Pipenv.

First you need to docker-compose run to install django from the top level directory.

`docker-compose run web pipenv install django`

After that run the docker-compose command to start the new django project.

`docker-compose run web pipenv run django-admin.py startproject PROJECT_NAME .`

Run the docker-compose up command from the top level directory for your project.

`docker-compose up`
