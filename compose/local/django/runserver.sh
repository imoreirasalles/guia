#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
# Creates an superuser with login=admin password=test
python manage.py loaddata superuser
python manage.py runserver_plus 0.0.0.0:8000
