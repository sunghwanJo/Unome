from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DB:
    DATABASE_URI = 'sqlite:////tmp/flask-oauth.db'

    engine = create_engine(DATABASE_URI)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base = declarative_base()
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    

class User(DB.Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    name = Column(String(60))
    oauth_token = Column(String(200))
    oauth_secret = Column(String(200))

    def __init__(self, name):
        self.name = name
