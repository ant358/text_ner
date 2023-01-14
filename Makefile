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
	# deploy the code
	docker run \
		--rm -d -p 7080:7080 \
		--name text_ner \
		-e CONTAINER_NAME \
		--env CONTAINER_NAME="text_ner" \
		--env-file .env \
		-v text_data_vol:/app/data \
		-v text_data_logs:/app/logs \
		text_ner
deploy:
	# customise to the cloud provider
	docker login
	docker image tag text_controller svgcant2022/text-ms:text_ner
	docker push svgcant2022/text-ms:text_ner

all: install format lint test build run deploy