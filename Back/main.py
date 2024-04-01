import uvicorn
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from core.config import redis
from src.app.encrypt.router.api_v1.router import router
from src.app.auth.router.api_v1.router import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(title="Encrypt")
app.include_router(router)
app.include_router(auth_router)
app.mount("/", StaticFiles(directory="../Front/"), name="css", )

origins = ["http://localhost:8080", ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin", "Authorization"],
)


async def main():
    config = uvicorn.Config(app="main:app", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
