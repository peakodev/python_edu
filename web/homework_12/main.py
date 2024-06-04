from fastapi import FastAPI

from src.routes import auth, contacts, users
from src.middleware.cors import apply_cors

app = FastAPI()

apply_cors(app)

app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')
app.include_router(users.router, prefix='/api')


@app.get("/")
def read_root():
    return {"Hello": "World"}
