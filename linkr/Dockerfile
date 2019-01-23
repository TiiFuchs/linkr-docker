FROM httpd:alpine
LABEL maintainer="Tii <mail@tii.one>"

RUN set -e \
  && apk add python py2-pip npm apache2-mod-wsgi \
  && apk add git jq mysql-client \
  && apk add build-base python2-dev mariadb-dev \
  && pip install virtualenv \
  && git clone https://github.com/LINKIWI/linkr /linkr \
  && cd /linkr \
  && virtualenv env \
  && source env/bin/activate \
  && pip install -r requirements.txt \
  && npm install --quiet \
  && apk del build-base python2-dev

COPY apache.conf /usr/local/apache2/conf/extra/linkr.conf
RUN echo 'Include conf/extra/linkr.conf' >> /usr/local/apache2/conf/httpd.conf

WORKDIR /linkr
COPY write_config.py write_config.py
COPY entrypoint.sh /entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
