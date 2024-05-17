from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

CONN = "sqlite:///projeto_login.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column (String(50))
    email = Column(String(200))
    senha = Column(String(100))
    
Base.metadata.create_all(engine)