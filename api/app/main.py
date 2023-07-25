from fastapi import Depends, FastAPI, Depends, status, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/news")
def test_news(db: Session = Depends(get_db)):
    db_item = db.query(models.News).all()
    return {"data": db_item}

@app.post("/news", status_code=status.HTTP_201_CREATED)
def create_news(news: schemas.CreateNews, db: Session = Depends(get_db)):
    new_news = models.News(**news.model_dump())
    try:
        db.add(new_news)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return f"Failed to insert: {error}"

@app.post("/bulk_news", status_code=status.HTTP_201_CREATED)
def create_news(news: List[dict], db: Session = Depends(get_db)):
    try:
        db.bulk_insert_mappings(models.News, news)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return f"Failed to insert: {error}"
    
@app.delete("/news/{id}", status_code=status.HTTP_200_OK)
def delete_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.News).filter(models.News.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item