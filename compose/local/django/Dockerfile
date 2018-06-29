FROM python:3.6
LABEL mantainer "hacklab/ <contato@hacklab.com.br>"
ENV PYTHONUNBUFFERED 1


RUN apt-get update -y && apt-get install -y \
    gettext \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/django/runserver.sh /runserver.sh
RUN sed -i 's/\r//' /runserver.sh
RUN chmod +x /runserver.sh

ENTRYPOINT ["/entrypoint.sh"]
