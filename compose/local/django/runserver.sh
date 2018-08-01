#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
# Creates an superuser with login=admin password=test
python manage.py loaddata superuser
python manage.py loaddata glossary_AccessCondition_initial_data.json
python manage.py loaddata glossary_AggregationType_initial_data.json
python manage.py loaddata glossary_DescriptionLevel_initial_data.json
python manage.py loaddata glossary_GenreTag_initial_data.json
python manage.py loaddata location_Location_initial_data.json
python manage.py loaddata management_ManagementUnit_initial_data.json
python manage.py runserver_plus 0.0.0.0:8000
