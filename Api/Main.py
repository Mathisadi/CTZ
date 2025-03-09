from fastapi import FastAPI
from Routes import router as route_router

app = FastAPI()

app.include_router(route_router)
