from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:123@localhost/n75fastdb')
Base = declarative_base()
Session = sessionmaker(bind=engine)

