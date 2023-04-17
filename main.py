from fastapi import FastAPI
import httpx
from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)

class Post(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    title = fields.CharField(max_length=100)
    body = fields.TextField()

async def populate_users():
    async with httpx.AsyncClient() as client:
        page = 1
        while True:
            response = await client.get("https://gorest.co.in/public-api/users", params={"page": page})
            data = response.json()
            if not data["data"]:
                break
            for user_data in data["data"]:
                await User.get_or_create(id=user_data["id"], name=user_data["name"], email=user_data["email"])
            page += 1

async def populate_posts():
    async with httpx.AsyncClient() as client:
        page = 1
        while True:
            response = await client.get("https://gorest.co.in/public-api/posts", params={"page": page})
            data = response.json()
            if not data["data"]:
                break
            for post_data in data["data"]:
                await Post.get_or_create(id=post_data["id"], user_id=post_data["user_id"], title=post_data["title"], body=post_data["body"])
            page += 1

@app.on_event("startup")
async def on_startup():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()
    if not await User.exists():
        await populate_users()
    if not await Post.exists():
        await populate_posts()

@app.on_event("shutdown")
async def on_shutdown():
    await Tortoise.close_connections()

@app.get("/users")
async def users():
    users = await User.all().values()
    return {"data": users}

@app.get("/users/{user_id}")
async def user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        return {"error": "User not found"}
    return {"data": user}

@app.get("/users/{user_id}/posts")
async def user_posts(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        return {"error": "User not found"}
    posts = await Post.filter(user_id=user_id).values()
    return {"data": posts}

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["__main__"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)