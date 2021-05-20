from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class UName(Base):
    __tablename__ = 'u-name'
    u_id = Column(Integer, primary_key=True)
    u_name = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, u_id=None, u_name=None, created_at=None, updated_at=None):
        self.u_id = u_id
        self.u_name = u_name
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<U_NAME %r>' % (self.u_name)

class URaceSchedule(Base):
    __tablename__ = 'u-race-schedule'
    u_id = Column(Integer, primary_key=True)
    race_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, u_id=None, race_id=None, created_at=None, updated_at=None):
        self.u_id = u_id
        self.race_id = race_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<U_id %r>' % (self.u_id)
