from movie.models import MovieModel
from fastapi import HTTPException, status


async def get_movies_list(db):
    movies = db.query(MovieModel).all()

    movie_list = []

    for movie in movies:
        movie_list.append({
            "id": movie.id,
            "name": movie.name,
            "genre": movie.genre,
            "rating": movie.rating,
            "release_date": movie.release_date.strftime('%d-%m-%Y')
        })

    return movie_list


async def add_new_movie(db, movie):
    new_movie = MovieModel(**movie.dict())

    try:
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return movie


async def search_by_name(db, name):
    movie = db.query(MovieModel).filter(MovieModel.name == name).first()

    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    return {
        "id": movie.id,
        "name": movie.name,
        "genre": movie.genre,
        "rating": movie.rating,
        "release_date": movie.release_date.strftime('%d-%m-%Y')
   }