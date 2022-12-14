from fastapi import FastAPI

from app.routes import blog, user

app = FastAPI()

app.include_router(user.router)
app.include_router(blog.router)


@app.get("/")
def root():
    return {"message": "Root route"}
