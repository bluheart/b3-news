from fastapi import Depends, FastAPI, Depends, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/news")
def test_news(db: Session = Depends(get_db)):

    news = db.query(models.News).all()
    return {"data": news}



@app.post("/news", status_code=status.HTTP_201_CREATED)
def create_news(news: schemas.CreateNews, db: Session = Depends(get_db)):
    new_news = models.News(**news.model_dump())
    try:
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return {"data": new_news}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return f"Failed to insert: {error}"


