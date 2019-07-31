import uvicorn
from fastapi import FastAPI

from applications.users.router import router
from applications.users import api

app = FastAPI()

app.include_router(router, prefix="/user", tags=["user"])

if __name__ == '__main__':
    uvicorn.run(app)
