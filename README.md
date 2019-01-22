# How to use this image

## Configuration

**Linkr** needs a MySQL and a Redis instance to work properly. So you may want to create a docker-compose.yml and fill something like this:
```
version: '3'
services:
  linkr:
    image: tiirex9/linkr
    depends_on:
      - mysql
    ports:
      - 5000:80
    env_file: .env

  mysql:
    image: mariadb
    volumes:
      - linkr-data:/var/lib/mysql
    env_file: .env

  redis:
    image: redis
```

Since **Linkr** needs a little bit on configuration you should create an .env file with any of these variables you want to override. For an explanation of the variables head over to the official GitHub Repo of [Linkr](https://github.com/LINKIWI/linkr#configuration).

| Variable                 | Default               |
|:-------------------------|:----------------------|
| TITLE                    | linkr                 |
| LINKR_URL                | http://localhost:5000 |
| ENABLE_RECENT_LINKS      | *true*                |
| REQUIRE_LOGIN_TO_CREATE  | *false*               |
| ALLOW_OPEN_REGISTRATION  | *true*                |
| SECURE_FRONTEND_REQUESTS | *true*                |
| RECAPTCHA_SITE_KEY       | *null*                |
| RECAPTCHA_SECRET_KEY     | *null*                |
| PIWIK_URL                | *null*                |
| PIWIK_SITEID             | *null*                |
| SENTRY_CLIENT_DSN        | *null*                |
| SENTRY_SERVER_DSN        | *null*                |
| MYSQL_HOST               | localhost             |
| MYSQL_USER               | linkr                 |
| MYSQL_PASSWORD           | password              |
| MYSQL_DATABASE           | linkr                 |
| REDIS_HOST               | localhost             |
| REDIS_PORT               | 6379                  |
| REDIS_PASSWORD           | password              |
| STATSD_HOST              | localhost             |
| STATSD_PORT              | 8125                  |

## Setup

To setup Linkr for the first time, run `docker-compose run linkr setup` and wait until the build process finished. After that (and after the database is created properly) the Linkr setup starts, displays you a few config variables and then asks for your first user and password. (You can run this again, if you want to create additional users from the command line.)

After that just run `docker-compose up -d` and your shiny new URL Shortener should just work fine.
