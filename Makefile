.PHONY: test run docker-build docker-up

test:
	uv run pytest

run:
	uv run uvicorn openrag_eval.app:app --app-dir src --host 0.0.0.0 --port 8090 --reload

docker-build:
	docker compose build openrag-eval-api

docker-up:
	docker compose up openrag-eval-api
