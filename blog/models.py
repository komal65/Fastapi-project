from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import Base

Base = declarative_base()

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Example: Set the length to 255 characters
    body = Column(String(1000), index=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    
    creator = relationship("User",back_populates="blogs")
    
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True ,autoincrement=True)
    name = Column(String(255), index=True)  # Example: Set the length to 255 characters
    email = Column(String(1000), index=True)
    password = Column(String(1000), index=True)
    # blog_id = Column(Integer, ForeignKey('user.id'))
    
    blogs = relationship("Blog",back_populates="creator")
    

    