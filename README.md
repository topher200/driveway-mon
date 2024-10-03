# Driveway Monitor
Continuously monitor the driveway to determine whose cars are parked.

## Running in Docker

```
$ docker compose up --build --watch
```

## Run locally (not as tested)

### Install uv

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Run picture-taker

```
$ uv run src/picture-taker/picture-taker.py
```
