from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel


class Package(BaseModel):
    name: str
    number: int
    description : Optional[str] = None



app = FastAPI()


packages = []


@app.get('/')
async def hello_world():
    return {"the answer of everything": 42}


@app.post('/save_package/')
async def make_package(package: Package):
    packages.append(package)
    return "Post completed."


@app.get('/show_packages/')
def show_packages():
    if len(packages) == 0:
        return "Nothing to show"
    return package.dict()



