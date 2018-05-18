FROM python:3.4.3

ENV PYTHONUNBUFFERED 1

COPY ./docker/django/django-entrypoint.sh /
COPY ./py-requirements /django/py-requirements

WORKDIR /django

RUN pip install pip
RUN pip install --upgrade pip
RUN pip install -r py-requirements/dev.txt


CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
