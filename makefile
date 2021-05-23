PROJECT_NAME=hackernews

start:
	@docker stop resurface || true
	@rm -f ./hackernews/migrations/versions/*_.py
	@docker build -t test-aiohttp-hackernews --no-cache .
	@docker-compose up --detach
	@until docker exec -it hackernews_postgres psql -q -U postgres -c "select 1 as postgres_ready" -d postgres; do sleep 1; done
	@docker exec -it hackernews alembic revision --autogenerate
	@docker exec -it hackernews alembic upgrade head

stop:
	@docker-compose stop
	@docker-compose down --volumes
	@docker image rmi -f test-aiohttp-hackernews:latest

bash:
	@docker exec -it hackernews bash

logs:
	@docker logs -f hackernews

ping:
	@curl "http://localhost/ping"

psql:
	@docker exec -it hackernews_postgres psql -U postgres

restart:
	@docker-compose stop
	@docker-compose up
