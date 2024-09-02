
# Movie Rating System

## Language & framework
* Framework - Python (FastAPI)

* Database - Postgresql Cloud 

* ORM - Sqlalchemy

## Setup Instructions:

 
* ``` pip install -r requirements.txt ```
* ``` python main.py ```
* http://localhost:8000/docs for API testing with swagger integration.

 ## REST API Endpoints:
* `POST /user/signup` signup router
* `POST /user/login` login router
* `POST /movie/` add new movie
* `GET /movie/` get all movies
* `POST /rating/` add new rating
* `GET /movie/search?name=movie_name` search movie by name

## Assumptions:
* Assuming `"rating:"` field in Ratings JSON would be `"rating"` without semicolon.
* Assuming user has to be logged in to perform operations of Movies and Ratings.
* Assuming user can search movies by name with exact match.

## Notes and Details About project
* JWT token authentication is implemented for authorization.
* Tried to follow `Modular Design Pattern`
* Business logic separated to `services` file
* Routers are separated to `routers` file 




