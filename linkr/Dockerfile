FROM httpd:alpine
MAINTAINER Tii <mail@tii.one>

RUN set -e \
  && apk add python py2-pip npm apache2-mod-wsgi \
  && apk add git jq mysql-client \
  && apk add build-base python2-dev mariadb-dev \
  && pip install virtualenv \
  && git clone https://github.com/LINKIWI/linkr /linkr \
  && cd /linkr \
  && virtualenv env \
  && source env/bin/activate \
  && sed -i '/MySQL-python/d' requirements.txt \
  && pip install -r requirements.txt \
  && pip install mysqlclient \
  && npm install --quiet \
  && apk del build-base python2-dev
# MySQL-python has issues on alpine systems but mysqlclient 
# does the same and works as a drop-in replacement

COPY apache.conf /usr/local/apache2/conf/extra/linkr.conf
RUN echo 'Include conf/extra/linkr.conf' >> /usr/local/apache2/conf/httpd.conf

WORKDIR /linkr
COPY entrypoint.sh /entrypoint.sh

VOLUME /config
EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
