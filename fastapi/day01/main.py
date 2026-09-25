from fastapi import FastAPI

app=FastAPI()   

@app.get("/")
def home():
    return {"message" : "My First Fast-API endpoint"}


@app.get("/about")
def about():
    return{"Name : Muhammad Hassan \n, Class : BESE30 B\n , Room : 43"}

@app.get("/status")
def status():
    return{"Day of learning fastapi : 1 , OK "}


#on the server you can check official documentation by loophole address /doc or /redoc  
#  uvicorn day01.main:app --reload(--reload is running, your server should automatically reload.)
#http://127.0.0.1:8000/openapi.json (You'll see a large JSON document.That's your application's OpenAPI schema)
