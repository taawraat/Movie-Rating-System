from fastapi import HTTPException, status
from .models import RatingModel


async def create_rating(db, rating):
    new_rating = RatingModel(
        user_id=rating.user_id,
        movie_id=rating.movie_id,
        rating=rating.rating
    )

    try:
        db.add(new_rating)
        db.commit()
        db.refresh(new_rating)
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str("Internal Server Error"))


def average_ratings(movie_id, db):
    ratings = db.query(RatingModel).filter(RatingModel.movie_id == movie_id).all()

    if not ratings:
        return 0

    total = 0
    for rating in ratings:
        total += rating.rating

    return total/len(ratings)