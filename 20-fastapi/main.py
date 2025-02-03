from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World"}


@app.get("/learn")
async def learn():
    return {"message": "Learning Python in 2025 🐍"}


# Path parameter
@app.get("/user/{user_name}")
async def user(user_name):
    return {"message": f"Hello, {user_name}"}
    # e.g. /user/Ashmin
    # -> {"message": "Hello, Ashmin"}
