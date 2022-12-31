# PSPproject

## Documentation

Auto generated documentation which can be plugged into online swagger
editor is in a file: api_documentation.json

We implemented all API endpoints, however we did not find it necessary to implement all the features in the endpoints.
For example, we didn't include pagination, it only works if we put in number 1. Also, querying in specific endpoints was simplified, because we did not find it important and useful enough.


## Starting the API with Docker

* Install docker: https://docs.docker.com/get-docker/

* Run docker

* Go to PSPproject

Start containers:

```
docker compose up --build
```

Open API with these links:

```
localhost:8000/docs
localhost:8000/redoc
```

## Optional Docker commands

Build and tag the image:

```
docker build . -t psp
```

Start the application:

```
docker run -p8000:8000 psp
```

## Without Docker

Recommend to use venv (virtual environment)
python3 keyword may be different on your device
Python 3.11 recommended

Install the dependencies:

```
python3 -m pip install -r requirements.txt
```

Start the application:

```
python3 -m uvicorn main:app
```

## Documentation portals

Available from:

```
localhost:8000/docs
localhost:8000/redoc
```
