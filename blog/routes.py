from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from blog import crud, schemas, database

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/blog", response_model=List[schemas.Blog])
def index(limit: int = 10, published: bool = None, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db=db, limit=limit, published=published)
    return blogs


@router.get("/blog/unpublished")
def unpublished(db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db=db, published=False)
    return {'data': blogs}


@router.get("/blog/{id}", response_model=schemas.Blog)
def show(id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog(db=db, blog_id=id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.post("/blog", response_model=schemas.Blog)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return crud.create_blog(db=db, blog=request)
