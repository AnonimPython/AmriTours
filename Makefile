build:
	docker build -t amritours .

run:
	docker run -p 8000:8000 amritours

migrate:
	reflex db migrate && reflex db makemigrations