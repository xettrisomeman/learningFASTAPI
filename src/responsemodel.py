from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class PackageIn(BaseModel):
    secret_id : int 
    name: str
    number: str
    description: Optional[str] = None


class PackageOut(BaseModel):
    name: str
    number: str
    description: Optional[str] = None


@app.get('/')
async def hello_world():
    return {"the answer of everything": 42}


# response_model = going out, whats the server gets to see, what we see
@app.post("/package/", response_model=PackageOut, response_model_exclude=["description"]) # dont show description on api
async def make_package(package: PackageIn): # what a suser can input
    return package


