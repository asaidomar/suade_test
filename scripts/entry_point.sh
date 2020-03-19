#!/usr/bin/env sh
set -e
cd /app

python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('${SUADE_ADMIN}', '${SUADE_EMAIL}', '${SUADE_PASSWORD}')" > /dev/null 2>&1 || true
# python manage.py load_data

gunicorn --reload -b 0.0.0.0:9090 config.wsgi