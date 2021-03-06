#!/bin/sh

if [ "$DATABASE" = "morozov_blog" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

chmod -R 777 static
exec "$@"
