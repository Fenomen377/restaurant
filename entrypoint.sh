python3 ./manage.py wait_for_db --skip-checks
python3 ./manage.py migrate --no-input --skip-checks
python3 ./manage.py runserver 0.0.0.0:8000