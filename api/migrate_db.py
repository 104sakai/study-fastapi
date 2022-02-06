from sqlalchemy import create_engine

from api.models.sample import Base

DB_URL = "mysql+pymysql://root:mysql@127.0.0.1:55001/sample?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
  reset_database()