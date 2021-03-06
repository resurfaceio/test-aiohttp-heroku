# Integration testing app for aiohttp | Usagelogger

## Run the project (Development Setup)

Note: You should be on the project root directory

### ENV variables

change the environment variables in `.env` file

```
USAGE_LOGGERS_URL = http://<resurface-host>/message
DATABASE_URL = postgres://postgres:postgres@postgres/postgres
```

### Resurface setup

You can use `ngrok` as a tunnel for `resurface`

```bash
ngrok http 4001
```

now set the environment variables

```
USAGE_LOGGERS_URL = https://<ngrok-id>.ngrok.io/message
DATABASE_URL = postgres://postgres:postgres@postgres/postgres
```

### Run the application

```
make
```

### Make migrations

```
make migrations
```

### Make migrate

```
make migrate
```

### Upgrade on logger change

```
make upgrade-run
```

Now you can access the app from: `http://localhost/`

## Heroku Deployment

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

# Todo

- [x] Add general query and mutations
- [ ] Add authentication
- [ ] Add authenticated query and mutations
