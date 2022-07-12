import re
from fastapi import FastAPI
from env2 import env2 as env


app = FastAPI(debug=bool(env('APP_LEVEL', False, False)))


@app.get('/')
async def index():
    """
    Index page

    Just exists, to show possibilities of this project
    """
    return {"status": "working"}


@app.get('/files/private/{token}')
async def private_endpoint():
    # TODO: model
    return {"status": "accepted token"}


@app.get('/files/public/')
async def public_files():
    # TODO: model
    return {"status": "accepted"}
