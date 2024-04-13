from fastapi import FastAPI

app = FastAPI()
@app.get("/get-massage")

async def read_root():
    return{"Message: Congrats! You have build your first API."}