import uvicorn
from fastapi import FastAPI, Query, Body

from hotels import router as hotels_router

app = FastAPI(debug=True)
app.include_router(hotels_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
