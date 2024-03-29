import uvicorn
import asyncio
from fastapi import FastAPI
from src.app.encrypt.router.api_v1.router import router

app = FastAPI(title="Encrypt")
app.include_router(router)


async def main():
    config = uvicorn.Config(app="main:app", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
