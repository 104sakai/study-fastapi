from fastapi import FastAPI

from api.routers import sample

app = FastAPI()
app.include_router(sample.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}