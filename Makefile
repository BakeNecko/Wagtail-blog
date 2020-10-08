PROJECT_NAME ?= wagtail_blog
VERSION = $(shell python3.8 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= neorusa
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make prod        - Create & run production development"
	@echo "make migrate     - Create and Apply all migrations in django"
	@echo "make clean       - Clean docker volumes"
	@echo "make shell       - Start Django shell in terminal"
	@echo "make stop        - Stops docker containers and delete them"
	@exit 0


_clean_makefile:
	rm -fr *.egg-info dist

_down_docker:
	docker-compose -f docker-compose.prod.yml down --remove-orphans

clean:
	docker volume prune

prod:
	docker-compose -f docker-compose.prod.yml up --build -d --force-recreate

run:
	docker-compose -f docker-compose.prod.yml up --build --force-recreate

migrate:
	docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations && \
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate

createsuperuser:
	docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

shell:
	docker-compose -f docker-compose.prod.yml exec web python manage.py shell

stop: _down_docker _clean_makefile
