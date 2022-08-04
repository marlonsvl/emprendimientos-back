web: gunicorn emprendimientos.wsgi --log-file -
web: python manage.py collectstatic --no-input; gunicorn giftme.wsgi
release: python manage.py migrate
