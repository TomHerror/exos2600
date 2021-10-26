from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    login = Column(String(20))
    desc = Column(String(500))

    def __repr__(self):
        return 'Account(id={id}, name={name!r}, lastname={lastname!r}, login={login!r}, desc={desc!r})'.format(**vars(self))
