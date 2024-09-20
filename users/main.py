import aiohttp
from fastapi import FastAPI, HTTPException

app = FastAPI(title="task2")


async def get_users():
    async with aiohttp.ClientSession("https://jsonplaceholder.typicode.com") as session:
        async with session.get("/users/") as resp:
            print(type(await resp.json()))
            return await resp.json()


async def get_user_by_email(email: str):
    users = await get_users()
    for user in users:
        if user["email"] == email:
            return user

@app.get("/users")
async def root():
    return await get_users()

@app.get("/users/{email}")
async def get_users_by_email(email: str):
    user = await get_user_by_email(email)
    if user:
        return user
    else:
        raise HTTPException(status_code=404)