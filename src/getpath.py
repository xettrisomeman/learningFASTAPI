from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet =  "alexnet"
    lenet = "lenet"
    resnet = "bert"


app = FastAPI(debug=True)


# # get to the path
# @app.get("/items/{item_id}")
# async def items(item_id: int): # can only pass integer
#     return {"item_id" : item_id}


# @app.get("/users/{username}")
# async def read_user(username: str):
#     return {"username" : username}

# @app.get("/users/{user_id:int}"):
# async def get_id(user_id):
    # return {"user_id": user_id}


# parameters which takes pre-defined values

@app.get("/model/{model_name}/")
async def get_model_name(model_name: ModelName): # inputted value should be of Enum modelClass
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    elif model_name == ModelName.lenet:
        return {"model_name" : model_name , "message" : "LeCNN all the images"}
    return {"model_name" : model_name, "message": "The godfather of Deep Learning Models."} 


