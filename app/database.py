from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# using sqlalchemy instead of this
# while True:
#     try:
#         conn = psycopg.connect(dbname="fastapi02",
#                                host="localhost",
#                                user="postgres",
#                                password="123456",
#                                port=5432,
#                                row_factory=dict_row)
#         cursor = conn.cursor()
#         print("Connected to database")
#         break

#     except Exception as err:
#         print("database connection error")
#         print(err)
#         time.sleep(5)
