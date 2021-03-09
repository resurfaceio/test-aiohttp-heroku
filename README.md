# test-aiohttp-app

## Environment Setup

_Note: You should be on the project root directory_

### ENV variables

**IMPORTANT:** change the environment variables in `.env` file

```
USAGE_LOGGERS_URL = http://<resurface-host>/message
DATABASE_URL = postgres://postgres:postgres@postgres/postgres
```

### Resurface setup using ngrok

You can use `ngrok` as a tunnel for `resurface`

```bash
ngrok http 4001
```

now set the environment variables

```
USAGE_LOGGERS_URL = https://<ngrok-id>.ngrok.io/message
DATABASE_URL = postgres://postgres:postgres@postgres/postgres
```

## Run the application

Execute the following commands in bash to get started.

```
make
```

### Make database migrations

```
make migrations

make migrate
```

### Update app on logger change

You can run the following command to build & run the application without cache.

```
make upgrade-run
```

Now you can access the app from: `http://localhost/`

# Heroku Deployment

Create Heroku app

```
heroku create aiohttp-resurface
```

Create PGSQL on Herkoku

```
heroku addons:create heroku-postgresql:hobby-dev -a aiohttp-resurface
```

Push to Heroku

```
heroku container:login
heroku stack:set container -a aiohttp-resurface
heroku config:set USAGE_LOGGERS_URL="http://marina:4001/message"
git push heroku master
```

# HTTP Health Check

Request:

```bash
curl http://localhost:8000/ping
```

Response:

```
{"msg": "pong"}
```
