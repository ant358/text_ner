install:
	# install the dependencies
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	# format the code
	yapf *.py src/*.py tests/*.py
lint:
	# see flake8.ini for linting configuration
	flake8 -v *.py src/*.py tests/*.py
test:
	# see pytest.ini for test configuration
	python -m pytest tests/*.py
build:
	# build the container
	docker build -t text_ner .
run:
	# run the container, ports, vols and network in docker-compose.yml
	docker run \
		--name text_ner \
		text_ner
deploy:
	# customise to the cloud provider
	docker login
	docker image tag text_controller svgcant2022/text-ms:text_ner
	docker push svgcant2022/text-ms:text_ner

all: install format lint test build run deploy