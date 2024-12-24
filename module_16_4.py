from fastapi import FastAPI, HTTPException, Path, Body
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int = Field(ge=0, description="Enter User ID", example=1)
    username: str = Field(min_length=5, max_length=20, description="Enter username", example='Verikon')
    age: int = Field(ge=0, description="Enter User Age", example=13)

users = []

@app.get("/users", response_model=List[User ])
async def get_users() -> List[User ]:
    return users

@app.post("/user/", response_model=User )
async def create_user(user: User) -> User:
    new_id = 1 if not users else users[-1].id + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}", response_model=User )
async def update_user(user_id: int, user: User) -> User:
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = user.username
            existing_user.age = user.age
            return existing_user
    raise HTTPException(status_code=404, detail="User  was not found")

@app.delete("/user/{user_id}", response_model=User )
async def delete_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User  was not found")

