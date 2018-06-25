# Catalogue Collections

# Requirements

-   Python 3.5 >= (<https://www.python.org>)
-   Django 2.0 >= (<https://www.djangoproject.com>)
    -   Django Rest Framework 3.0 >= (<http://www.django-rest-framework.org>)
-   PostgreSQL 9.6 >= (<https://www.postgresql.org>)

## How to: Deploy

> On a Debian 9/Ubuntu 16.04 server.

### 1. Server Dependencies

##### 1.1. GIT Install

     apt install -y git

##### 1.2. PostgreSQL, Postgis

    apt install -y postgresql postgresql-contrib postgis postgresql-9.6-postgis-2.3 postgresql-9.6-postgis-2.3-scripts

##### 1.3. GDAL

    apt-get install -y gdal-bin libgdal-dev libgdal-doc libgdal-grass python3-gdal

##### 1.4. Python3, PIP

    apt install -y python3 build-essential python3-dev gettext
    apt install -y python3-venv python3-pip

##### 1.5. Virtualenv

    pip3 install virtualenv

> You can use python default virtualenv for installing dependencies but as an personal favorite you should use virtualenvwrapper, as it is faster to activate envs. and saves you a lot of time. Read more on: [virtualenvwrapper documentation page](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

##### 1.5.1. Virtualenv creation and usage

    virtualenv env
    source env/bin/activate
> From here install all packages with the env activate to avoid any conflicts on your machine



### 2. Python Package Dependencies

##### 2.1. Django

    pip3 install django

##### 2.1.1. Requirements.txt

    pip install -r requirements.txt -v

##### 2.2. Python-Decouple to set some settings for the project

Python-Decouple makes easier to set some settings for the project.
You should create a file named `.env` on the project root with the following settings:

    DEBUG=True
    URL=localhost
    SECRET_KEY=YourSecretHere
    DB_NAME=YourDataBase
    DB_USER=YourUserDB
    DB_PASSWORD=YourPasswordDatabse
    DB_HOST=localhost

Docs: <https://pypi.org/project/python-decouple/#where-the-settings-data-are-stored>

### 3. Database

##### 3.1. User database

Create the user that will handle the database with your OS way of adding users, here we use `guia` for all the operations:

    On Debian: adduser guia

Create the user for postgres:

    sudo su postgres -c "createuser guia -P --interactive"

Logged in as  **guia** - create the database

    createdb --encoding "UTF-8" guia

To use postgis extension:

    guia=# CREATE EXTENSION IF NOT EXISTS postgis;

##### 3.2. Django Database

    python manage.py makemigrations
    python manage.py migrate


### 4. Application

Now we can run the django development server:

    python manage.py runserver

### References

-   UWSGI
    -   <https://docs.djangoproject.com/pt-br/2.0/howto/deployment/wsgi/uwsgi/>
