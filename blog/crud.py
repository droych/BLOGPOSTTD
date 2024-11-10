from sqlalchemy.orm import Session
from blog import models, schemas

def create_blog(db: Session, blog: schemas.Blog):
    db_blog = models.Blog(title=blog.title, body=blog.body, published=blog.published)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def get_blogs(db: Session, limit: int = 10, published: bool = None):
    query = db.query(models.Blog)
    if published is not None:
        query = query.filter(models.Blog.published == published)
    return query.limit(limit).all()
