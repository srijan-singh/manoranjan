import pymongo

from model import Movie
from setting import access_key

client = pymongo.MongoClient(access_key)

database = client["Manoranjan"]

movie_collection = database["Movie"]

def getAllMovie():
    movie_list = list(movie_collection.find({}))

    stack = [movie for movie in movie_list]

    movie_list = []

    for movie in stack:

        json = {
            "tag"        : movie["tag"],
            "episode"    : movie["episode"],
            "name"       : movie["name"],
            "server_url" : movie["server_url"],
            "year"       : movie["year"],
        }

        movie_list.append(json)

    return movie_list

def getMovie(_id : str):
    try:
        movie = movie_collection.find_one({"_id":_id})

        json = {
            "tag"        : movie["tag"],
            "episode"    : movie["episode"],
            "name"       : movie["name"],
            "server_url" : movie["server_url"],
            "year"       : movie["year"],
        }

        return json

    except:

        return False

def postMovie(movie : Movie):

    json = {
            "_id"        : movie.name.lower()+movie.year,
            "tag"        : movie.tag,
            "episode"    : movie.episode,
            "name"       : movie.name,
            "server_url" : movie.server_url,
            "year"       : movie.year,
        }    

    movie_collection.insert_one(json)

    return True

def putMovie(id : str, tag : str = None, episode : str = None,  name : str = None, server_url : str = None, year : str = None): 
    try:

        if(tag):
            update_data = {
                "$set":{
                    "tag":tag
                }
            }

        
        if(episode):
            update_data = {
                "$set":{
                    "episode":episode
                }
            }

        if(name):
            update_data = {
                "$set":{
                    "name":name
                }
            }

            movie_collection.insert_one({"id",id}, update_data)


        if(server_url):
            update_data = {
                "$set":{
                    "server_url":server_url
                }
            }

            movie_collection.insert_one({"id",id}, update_data)

        if(year):
            update_data = {
                "$set":{
                    "year":year
                }
            }

            movie_collection.insert_one({"id",id}, update_data)

        return True

    except:

        return False






