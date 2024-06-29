# Intial Static String
from fastapi import FastAPI
from flask import app


static_string = "Intial Text"

@app.post("/add")
async def add_text(text:str):
    global static_string
    static_string += text
    return{"Message": "Text added", "current string": static_string}

@app.change("/change")
async def change_text(new_text:str):
    global static_string
    static_string += new_text
    return{"Message": "Text changed", "current string": static_string}

@app.delete("/remove")
async def removed():
    global static_string
    static_string = " "
    return{"Message": "Text removed"}
