from typing import Optional
from fastapi import FastAPI

import dbtools

app = FastAPI()
db = dbtools.get_database()


@app.get("/")
async def home():
    return {"status": "running"}


@app.post("/api/user/exist")
async def exist_user(username):
    return dbtools.exist_user(db, username)


@app.post("/api/user/verify")
async def verify_user(username, password):
    return dbtools.verify_user(db, username, password)


@app.get("/api/indicators")
def get_indicator(uid):
    db = dbtools.get_database()
    return dbtools.get_indicators_by_uid(db, uid)

