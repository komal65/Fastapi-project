
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+pymysql://root:password@localhost:3005/doctors_appoinment')

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/fastapi"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# meta = MetaData()

# conn = engine.connect()

Base = declarative_base()


def get_db():
    db = SessionLocal()
    
    try:
        yield db
    
    finally:
        db.close()

