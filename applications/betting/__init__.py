import uvicorn
from fastapi import FastAPI

from applications.system.router import router
from applications.system import api

app = FastAPI()

app.include_router(router, prefix="/betting", tags=["betting"])

if __name__ == '__main__':
    uvicorn.run(app)
