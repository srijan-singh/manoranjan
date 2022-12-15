from pydantic import BaseModel

class Movie(BaseModel):
    _id        : str
    tag        : str
    episode    : str
    name       : str
    server_url : str
    year       : str

    def setId(id):
        _id = id
        return True

    def getId():
        return _id
