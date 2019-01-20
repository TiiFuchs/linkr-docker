# Installation

1. Copy .env.example to .env and specify a password for the MySQL user.
2. Create a docker-compose.override.yml if you want to publish port 80 or make adjustments for a reverse-proxy.
3. Run `docker-compose run linkr setup` for initial setup. Configuration files will get written and you will get asked for credentials for your first user.
4. Have a look at the config files in ./config and make adjustments where needed.
5. Run `docker-compose up -d` and visit your new url shortener.
