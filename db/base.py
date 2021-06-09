from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine('sqlite:///db.sqlite', echo=True)
metadata = MetaData(bind=engine)

@as_declarative(metadata=metadata)
class Base:
    pass

Session = sessionmaker()

@contextmanager
def session(**kwargs):
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception as e:
        print(e)
        new_session.rollback()
    finally:
        new_session.close()