from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy Base
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Database connection information
DB_USER = 'root'
DB_PASSWORD = 'ayoub'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'hbtn_0e_6_usa'

# Create a MySQL engine
DATABASE_URL = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(DATABASE_URL)

# Create the tables defined by the classes that inherit from Base
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
