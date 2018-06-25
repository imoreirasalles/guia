#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

apt update
apt-get install gdal-bin libgdal-dev libgdal-doc libgdal-grass python3-gdal

python manage.py migrate
python manage.py runserver_plus 0.0.0.0:8000
