import os
import time
import hashlib
from typing import Optional
from fastapi import FastAPI, UploadFile, File

import dbtools
import voice_tools

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
async def get_indicator(uid):
    db = dbtools.get_database()
    return dbtools.get_indicators_by_uid(db, uid)


@app.post("/api/voice/upload")
def upload_file(file: UploadFile = File(...)):
    try:
        os.mkdir("uploads")
    except Exception as e:
        print(e)
    hash_before = str(time.time()) + file.filename
    hash_after = hashlib.md5(hash_before.encode(encoding='UTF-8')).hexdigest()
    file_name = os.getcwd() + "/uploads/" + hash_after
    with open(file_name, 'wb+') as f:
        f.write(file.file.read())
        f.close()
    return {
        "filename": hash_after
    }


@app.get("/api/voice/recognize")
def recognize_voice(filename):
    file2base64 = voice_tools.convert_file(filename)
    return voice_tools.start_recognition(file2base64)


