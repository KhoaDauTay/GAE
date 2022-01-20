export $(grep -v '^#' .env | xargs)
python3 manage.py createsuperuser --noinput
