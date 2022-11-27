# PSPproject

## Documentation

Auto generated documentation which can be plugged into online swagger
editors is in api_documentation.json

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

Start with:

windows users:
Reccomend to use venv(virtual environment)
python3 keyword may be different on your device

```
python3 -m pip install uvicorn
python3 -m pip install fastapi
python3 -m pip install pydantic
python3 -m uvicorn main:app
```

Linux users:

```
uvicorn main:app
```

Available from:

```
localhost:8000/docs
localhost:8000/redoc
```
