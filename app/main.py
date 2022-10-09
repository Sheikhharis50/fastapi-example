from fastapi import FastAPI

from .routers import router as app_router

app = FastAPI(debug=True)
app.include_router(router=app_router)


@app.get("/health")
async def health():
    return {"message": "Ok"}
