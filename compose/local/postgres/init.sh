#!/bin/bash
set -e

apt update
apt install postgresql postgresql-contrib postgis postgresql-9.6-postgis-2.3 postgresql-9.6-postgis-2.3-scripts

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" "$POSTGRES_DB" <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS postgis;
EOSQL
