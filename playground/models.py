import datetime
import pytz

from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
	Boolean,
	Column,
	DECIMAL,
	DateTime,
	Integer,
	String,
	ForeignKey
)

Base = declarative_base()


class Account(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    create_at = Column(DateTime, default=datetime.datetime.now(tz=pytz.timezone('UTC')))
    last_signed_at = Column(DateTime)
    # member = relationship("Member", uselist=False, backref='accounts')


class Member(Base):
    __tablename__ = 'memberships'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    # account_id = Column(Integer, ForeignKey('accounts.id'))
    
    def __repr__(self):
         return "<User(name='%s')>" % self.name