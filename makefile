PROJECT_NAME=hackernews

start:
	@docker-compose up --force-recreate --build --detach
	@docker exec -it hackernews alembic revision --autogenerate
	@docker exec -it hackernews alembic upgrade head

stop:
	@docker-compose stop
	@docker-compose down
	@docker rmi test-aiohttp-heroku_hackernews

bash:
	@docker exec -it hackernews bash

logs:
	@docker logs -f hackernews

ping:
	@echo curl "http://localhost/ping"
	@curl "http://localhost/ping"

psql:
	@docker exec -it hackernews_postgres psql -U postgres

restart:
	@docker-compose stop
	@docker-compose up
