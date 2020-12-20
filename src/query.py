from fastapi import FastAPI
from typing import Optional



app = FastAPI()


# ?number=1&text=johncena
@app.get("/query/")
async def get_query(number: int, text: str) -> str:
    return {"number": number, "text" : text}


