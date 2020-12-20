from fastapi import FastAPI


app = FastAPI(debug=True)


# root page
@app.get("/")
async def root():
    return {"message" : "Hello World"}


# home page
@app.get('/home')
async def home():
    return {"message" : "Home Page"}



