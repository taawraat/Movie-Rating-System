import uvicorn
from fastapi import FastAPI, Depends
from database import get_db, init_db

from movie.routes import router as movie_router
from user.routers import router as user_router
from auth.routers import router as auth_router
from rating.routers import router as rating_router

app = FastAPI()

# initialize the database
app.add_event_handler("startup", init_db)

# include routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(movie_router)
app.include_router(rating_router)


def start():
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    start()
