from fastapi import FastAPI
from blog import models, database, routes

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API"}
