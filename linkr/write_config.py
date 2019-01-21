#!/usr/bin/python

import os, json

opt_client = {
  "title": os.environ.get("TITLE", "linkr"),
  "piwik": {
    "url": os.environ.get("PIWIK_URL", None),
    "siteId": os.environ.get("PIWIK_SITEID", None)
  },
  "enable_recent_links": os.environ.get("ENABLE_RECENT_LINKS", True)
}
with open('config/options/client.json', 'w') as file:
  json.dump(opt_client, file)

opt_server = {
  "linkr_url": os.environ.get("LINKR_URL", "http://localhost:5000"),
  "require_login_to_create": os.environ.get("REQUIRE_LOGIN_TO_CREATE", False),
  "allow_open_registration": os.environ.get("ALLOW_OPEN_REGISTRATION", True),
  "secure_frontend_requests": os.environ.get("SECURE_FRONTEND_REQUESTS", True)
}
with open('config/options/server.json', 'w') as file:
  json.dump(opt_server, file)

sec_client = {
  "sentry_client_dsn": os.environ.get("SENTRY_CLIENT_DSN", None),
  "recaptcha_site_key": os.environ.get("RECAPTCHA_SITE_KEY", None)
}
with open('config/secrets/client.json', 'w') as file:
  json.dump(sec_client, file)

sec_server = {
  "sentry_server_dsn": os.environ.get("SENTRY_SERVER_DSN", None),
  "recaptcha_secret_key": os.environ.get("RECAPTCHA_SECRET_KEY", None),
  "database": {
    "host": os.environ.get("MYSQL_HOST", "localhost"),
    "name": os.environ.get("MYSQL_DATABASE", "linkr"),
    "user": os.environ.get("MYSQL_USER", "linkr"),
    "password": os.environ.get("MYSQL_PASSWORD", "password")
  },
  "redis": {
    "host": os.environ.get("REDIS_HOST", "localhost"),
    "port": os.environ.get("REDIS_PORT", 6379),
    "password": os.environ.get("REDIS_PASSWORD", "password")
  },
  "statsd": {
    "host": os.environ.get("STATSD_HOST", "localhost"),
    "port": os.environ.get("STATSD_PORT", 8125)
  }
}
with open('config/secrets/server.json', 'w') as file:
  json.dump(sec_server, file)
