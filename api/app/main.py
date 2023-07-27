from fastapi import Depends, FastAPI, Depends, status, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from sqlalchemy import and_, func
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from datetime import date

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/news")
def get_news(dateStart: date | None = None, dateEnd: date | None = date.today(), db: Session = Depends(get_db)):
    if dateStart is None:
        db_item = db.query(models.News).all()
    else: 
        db_item = db.query(models.News).filter(and_(func.date(models.News.dateTime) >= dateStart),\
                                                    func.date(models.News.dateTime) <= dateEnd).all()
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
def create_news(news: List[schemas.CreateNews], db: Session = Depends(get_db)):
    for n in news:
        try:
            n_news = models.News(**n.model_dump())
            db.add(n_news)
            db.commit()
            print('news inserted')
        except SQLAlchemyError as e:
            error = str(e.__dict__)
        
@app.put("/news/{id}", status_code=status.HTTP_200_OK)
def update_news(news: schemas.CreateNews, id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.News).filter(models.News.id == id)
    n_news = db_item.first()
    if n_news == None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_item.update(news.model_dump())
    db.commit()
    return news


@app.delete("/news/{id}", status_code=status.HTTP_200_OK)
def delete_news(id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.News).filter(models.News.id == id).first()
    if db_item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item