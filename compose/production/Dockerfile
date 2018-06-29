FROM python:3.6 as django
LABEL mantainer "hacklab/ <contato@hacklab.com.br>"
ENV PYTHONUNBUFFERED 1

# Ensure that the the internal user and
# group used by django have a known uid and gid
RUN groupadd -r -g 999 django \
    && useradd -r -u 999 -g django django

RUN apt-get update -y && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal


# Requirements have to be pulled and installed here, otherwise caching won't work
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./compose/production/django/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /gunicorn.sh
RUN chown django /gunicorn.sh

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown django /entrypoint.sh

COPY . /app

RUN mkdir -p /app/staticfiles

# env.example must be used during build to provide a valid environment
RUN export $(cat /app/env.example | grep -v ^# | xargs) && \
    python /app/manage.py collectstatic --noinput

RUN chown -R django: /app

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/gunicorn.sh"]


FROM nginx:1.13 as nginx

COPY ./compose/production/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=django /app/staticfiles/ /usr/share/nginx/html/static/
