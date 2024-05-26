from fastapi import FastAPI

server = FastAPI()

#test the server is up
@server.get("/test")
def test():
    return "The server is working properly!"