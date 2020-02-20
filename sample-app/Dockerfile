FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev=3.8.1-r0  \
            build-base=0.5-r1  \
            linux-headers=4.19.36-r0 \
            pcre-dev=8.43-r0
RUN apk add --no-cache pcre=8.43-r0
WORKDIR /app
COPY /app /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
