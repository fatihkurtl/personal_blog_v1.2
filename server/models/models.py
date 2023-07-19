from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from sqlalchemy.sql import func

engine = create_engine("sqlite:///./my-site.db")
Base = sqlalchemy.orm.declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    token = Column(String(255), nullable=True)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(100), nullable=False)
    reading_time = Column(String(15), nullable=False)
    image = Column(String(150), nullable=True)
    subject = Column(String(200), nullable=False)
    content = Column(String(15000), nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())

    posts_category = relationship('PostsCategories', backref='post', lazy=True)
    posts_hashtags = relationship('PostsHashtags', backref='post', lazy=True)
    
    def __repr__(self):
        return '<Post %r>' % self.title
    
class PostsCategories(Base):
    __tablename__ = "posts_categories"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    category = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    
    def __repr__(self):
        return '<PostCategory %r>' % self.category
    
class PostsHashtags(Base):
    __tablename__ = "posts_hashtags"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    hashtag = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    def __repr__(self):
        return '<PostHashtag %r>' % self.hashtag

  
class Snippets(Base):
    __tablename__ = "snippets"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(100), nullable=False)
    reading_time = Column(String(15), nullable=False)
    image = Column(String(150), nullable=True)
    subject = Column(String(200), nullable=False)
    content = Column(String(15000), nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    snippets_category = relationship('SnippetsCategories', backref='snippets', lazy=True)
    snippets_hashtags = relationship('SnippetsHashtags', backref='snippets', lazy=True)
        
    def __repr__(self):
        return '<Snippet %r>' % self.title
    
class SnippetsCategories(Base):
    __tablename__ = "snippets_categories"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    category = Column(String(50), nullable=False)
    snippet_id = Column(Integer, ForeignKey('snippets.id'), nullable=False)
    
    def __repr__(self):
        return '<SnippetCategory %r>' % self.category
    
class SnippetsHashtags(Base):
    __tablename__ = "snippets_hashtags"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    hashtag = Column(String(50), nullable=False)
    snippet_id = Column(Integer, ForeignKey('snippets.id'), nullable=False)

    def __repr__(self):
        return '<SnippetHashtag %r>' % self.hashtag


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()