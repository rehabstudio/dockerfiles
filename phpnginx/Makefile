help:
	@echo "run	- Runs container and mounts $(CURDIR)/app/ to /var/www/app"

run: build
	docker run -P -d -v=$(CURDIR)/app/:/var/www/app:rw pemcconnell/phpnginx-test

build:
	docker build -t="pemcconnell/phpnginx-test" .
