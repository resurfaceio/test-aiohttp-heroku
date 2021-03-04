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

Create Heroku app

```
heroku create aiohttp-resurface

```

Create PGSQL on Herkoku

```
heroku addons:create heroku-postgresql:hobby-dev
```

Push to Heroku

```
heroku container:login
heroku stack:set container -a aiohttp-resurface
git push heroku master
```

OR

```
heroku container:push web --app aiohttp-resurface
heroku container:release web --app aiohttp-resurface
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
