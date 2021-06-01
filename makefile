PROJECT_NAME=aiohttp

start:
	@docker stop resurface || true
	@rm -f ./hackernews/migrations/versions/*_.py
	@docker build -t test-aiohttp --no-cache .
	@docker-compose up --detach
	@until docker exec -it aiohttp_postgres psql -q -U postgres -c "select 1 as postgres_ready" -d postgres; do sleep 1; done
	@docker exec -it aiohttp alembic revision --autogenerate
	@docker exec -it aiohttp alembic upgrade head

stop:
	@docker-compose stop
	@docker-compose down --volumes --remove-orphans
	@docker image rmi -f test-aiohttp

bash:
	@docker exec -it aiohttp bash

logs:
	@docker logs -f aiohttp

ping:
	#todo switch to GraphQL post
	@curl "http://localhost/ping"

psql:
	@docker exec -it aiohttp_postgres psql -U postgres

restart:
	@docker-compose stop
	@docker-compose up --detach

test:
	@docker exec -it aiohttp python3 test.py