from sqlalchemy import Column, Integer, String, Boolean
from blog.database import Base


class Blog(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    published = Column(Boolean, default=True) 
