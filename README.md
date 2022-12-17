# PSPproject

## Documentation

Auto generated documentation which can be plugged into online swagger
editors is in api_documentation.json

## Docker Compose

Start containers:

```
docker compose up --build
```

## Docker

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
