import uvicorn

from fastapi import FastAPI, HTTPException
# an HTTP-specific exception class  to generate exception information
from fastapi.middleware.cors import CORSMiddleware

from setting import password as _password
from model import Movie

from database import(
    getMovie,
    getAllMovie,
    postMovie,
    putMovie
)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {"response" : "Manoranjan"}

# Movie
@app.get("/movie/*")
async def show_all_movie():
    response = getAllMovie()
    return response

@app.get("/movie/")
async def show_movie(id : str):
    response = getMovie(id)

    if(response):
        return {"response" : response}

    return {"response" : "Not Available"}

@app.post("/add/movie")
async def add_movie(password : str, request : Movie):
    if(password == _password):
        return getAllMovie()

    if(getMovie(request.getId)):
        return {"response" : "ID Already Exist!"}

    response = postMovie(request)
    return {"response":"Successfully Added!"}

@app.put("update/movie")
async def update_movie(password : str, id : str, request : Movie):
    if(password == _password):
        return getAllMovie()

    response = putMovie(id, request.name, request.server_url, request.year)
    if(response):
        return {"response" : "Successfully Updated!"}

    return {"response" : "Movie ID Not Found!"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

