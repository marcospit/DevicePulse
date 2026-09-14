# DevicePulse

DevicePulse is a lightweight endpoint monitoring and inventory system built with Python and FastAPI.

## Current features

- Endpoint agent written in Python
- Hardware information collection
- Operating system information collection
- Network information collection
- Device heartbeat/check-in
- REST API
- Swagger/OpenAPI documentation
- JSON-based local persistence

## Tech Stack

- Python
- FastAPI
- Pydantic
- psutil
- Requests
- Uvicorn

## Running the API

```bash
uvicorn server.main:app --reload


API documentation:

http://127.0.0.1:8000/docs

Running the Agent

python -m agent.agent