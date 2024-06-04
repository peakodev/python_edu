from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.conf.config import settings


engine = create_engine(settings.postgres_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
