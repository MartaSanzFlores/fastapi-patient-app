from sqlmodel import create_engine, Session, SQLModel
import os

# Create a Engine
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_PORT = os.getenv("MYSQL_PORT", 3306)

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables")

engine = create_engine(DATABASE_URL, echo=True)

# Create a Session Dependency
def get_session():
    with Session(engine) as session:
        yield session

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
