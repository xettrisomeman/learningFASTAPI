from fastapi import FastAPI, Form

# Forms is alternative to JSON

app = FastAPI()


# forms
@app.post("/language/")
async def language(name: str = Form(default=None), type: str = Form(default=None)):
    return {"name": name, "type": type}

