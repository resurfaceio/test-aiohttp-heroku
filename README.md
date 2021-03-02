# Integration testing app for aiohttp | Usagelogger

## Run the project (Development)

Note: You should be on the project root directory

### Create virtual env

```
$ python -m venv .venv
$ source activate ./.venv/bin/activate
```

### Run app

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

Now you can access the app from: `http://localhost:8080/`

## Heroku Deployment

```
heroku container:login
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME
heroku config:set WORKERS=2 --app $HEROKU_APP_NAME
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
