#!/bin/sh

echo "Starting entrypoint script"

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Flushing database..."
python manage.py flush --no-input
echo "Running migrations..."
python manage.py migrate

exec "$@"
