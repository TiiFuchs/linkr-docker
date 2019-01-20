#!/bin/sh

cd /linkr

# Create config files if not already there
for d in options secrets; do
  for f in client server; do
    if [ ! -f /config/$d/$f.json ]; then
      mkdir -p /config/$d

      # Set mysql/redis data from environment
      if [ "$d/$f" == "secrets/server" ]; then
        jq ".database.host=\"mysql\" | .database.name=\"$MYSQL_DATABASE\"
          | .database.user=\"$MYSQL_USER\" | .database.password=\"$MYSQL_PASSWORD\"
          | .redis.host=\"redis\" | .redis.password=\"\"" \
          config/$d/$f.json.template > /config/$d/$f.json
      else
        cp config/$d/$f.json.template /config/$d/$f.json
      fi
    fi
  done
done

# Load configuration
cp -r /config /linkr

# Build assets
source env/bin/activate
NODE_ENV=production npm run build

# Setup or start server
case "$1" in
  setup)
    echo -n "Waiting for database"
    while ! mysqladmin ping -h mysql >/dev/null 2>&1; do
      echo -n .
      sleep 1
    done
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
