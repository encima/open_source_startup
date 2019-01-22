from sqlalchemy import Column, DateTime, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class Bike(Base):
    __tablename__ = 'bikes'
    id = Column(String(20), primary_key=True)
    name = Column(String(100))
    model = Column(String(20))
    age = Column(Integer())

    def update(self, id=None, name=None, model=None, age=None):
        if name is not None:
            self.name = name
        if model is not None:
            self.model = model
        if age is not None:
            self.age = age

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
