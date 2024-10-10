from . import Base, engine
from sqlalchemy import Column, Integer, String, DateTime


class JobSQLAlchemy(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(String)
    img_link = Column(String)
    slug_url = Column(String)
    date = Column(DateTime)


Base.metadata.create_all(engine)
