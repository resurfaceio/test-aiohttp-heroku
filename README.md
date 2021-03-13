# test-aiohttp-app
Example GraphQL API built with AIOHTTP

## Requirements

* Install `docker` and `docker-compose`
* Sign up for [Resurface Pilot Edition](https://resurface.io/pilot-edition) access

## Ports Used

* 80 - GraphQL API
* 4002 - Resurface API Explorer
* 4001 - Resurface microservice
* 4000 - Trino database UI
* 5432 - Postgresql database

## Deploy Locally

```
make start     # rebuild and start containers
make ping      # make simple ping request
make bash      # open shell session
make logs      # follow container logs
make stop      # halt and remove containers
```
