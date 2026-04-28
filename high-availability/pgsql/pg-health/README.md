# pgsql-health

A lightweight FastAPI service that exposes a health-check endpoint for PostgreSQL instances. It queries `pg_is_in_recovery()` to report whether each instance is running as **primary**, **standby**, or **offline**.

## Configuration

Database connection strings are read from environment variables following the pattern:

```
DATABASE_{id}_URL=postgresql://user:password@host:5432/dbname
```

For example:

```env
DATABASE_URL=postgresql://postgres:secret@12.34.56.78:5432/mydb
```

## API

### `GET /healthz`

Returns the replication mode of the PostgreSQL instance.

**Responses:**

| Scenario | Status | Body |
|---|---|---|
| Instance is primary | 200 | `{"status": "primary"}` |
| Instance is standby | 200 | `{"status": "standby"}` |
| Instance is unreachable | 200 | `{"status": "offline"}` |

## Project Structure

```
pg-health/
├── pyproject.toml   # dependencies and project metadata
├── app.py           # FastAPI application
├── Dockerfile
└── README.md
```

## Dependencies

- Python 3.13
- FastAPI + Uvicorn
- psycopg\[binary\] (PostgreSQL driver, v3)
- Managed with uv

## Development

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Run the server
uv run uvicorn app:app --host 0.0.0.0 --port 8000

# Or with auto-reload for development
uv run uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## Docker

```bash
# Build
docker build -t pg-health .

# Run
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://postgres:secret@host1:5432/mydb \
  pg-health
```
