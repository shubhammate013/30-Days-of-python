from fastapi import FastAPI # type: ignore
from flask import Flask

app = FastAPI()
@app.get("/get-massage")
def hello(name:str):
    return{"Message  : Congrats!"+ name + "  You have build your first API."}