web: python manage.py runserver
web: gunicorn gkb_dory.wsgi --log-file -
heroku ps:scale web=1