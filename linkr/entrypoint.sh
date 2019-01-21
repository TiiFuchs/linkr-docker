#!/bin/sh

cd /linkr

python write_config.py

# Build assets
source env/bin/activate
NODE_ENV=production npm run build

# Setup or start server
case "$1" in
  setup)
    host=$(jq -r '.database.host' config/secrets/server.json)
    echo -n "Waiting for database"
    while ! mysqladmin ping -h $host >/dev/null 2>&1; do
      echo -n .
      sleep 1
    done
    echo ""
    echo ""

    python linkr_setup.py
    ;;

  "")
    exec httpd-foreground
    ;;

  *)
    exec $@
    ;;
esac
