import os
import asyncpg
from fastapi import FastAPI
from fastapi.responses import JSONResponse


DATABASE_URL = os.environ["DATABASE_URL"]
CONNECT_TIMEOUT = int(os.environ.get("CONNECT_TIMEOUT", "3"))


app = FastAPI()


@app.get("/healthz")
async def healthz():
    try:
        conn = await asyncpg.connect(DATABASE_URL, timeout=CONNECT_TIMEOUT)
        try:
            is_in_recovery = await conn.fetchval("SELECT pg_is_in_recovery()")
            status = "standby" if is_in_recovery else "primary"
            return {"status": status}
        finally:
            await conn.close()
    except Exception:
        return JSONResponse(status_code=503, content={"status": "offline"})
