from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int) -> User:
