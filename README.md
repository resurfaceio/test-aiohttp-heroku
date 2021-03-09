# test-aiohttp-app
Test GraphQL API built with AIOHTTP

## Configure Environment

Install your Resurface database: https://resurface.io/pilot-edition

```
# configure to point to your Resurface database host
export USAGE_LOGGERS_URL=http://<resurface-host>:4001/message
```

## Deploy Locally

```
make start     # rebuild and start containers
make ping      # make simple ping request
make bash      # open shell session
make logs      # follow container logs
make stop      # halt and remove containers
```

## Deploy to Heroku

1. Create Heroku app

```
heroku create aiohttp-resurface
```

2. Create PGSQL on Herkoku

```
heroku addons:create heroku-postgresql:hobby-dev -a aiohttp-resurface
```

3. Push to Heroku

```
heroku container:login
heroku stack:set container -a aiohttp-resurface
heroku config:set USAGE_LOGGERS_URL="http://marina:4001/message"
git push heroku master
```

4. Make ping request
```
curl "http://aiohttp-resurface.herokuapp.com/ping"
```

5. Delete Heroku app
```
heroku apps:destroy aiohttp-resurface
```
