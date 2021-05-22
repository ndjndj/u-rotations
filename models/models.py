from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class UName(Base):
    __tablename__ = 'u-name'
    u_id = Column(Integer, primary_key=True)
    u_name = Column(String(128))
    u_name_ex = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, u_id=None, u_name=None, u_name_ex=None, created_at=None, updated_at=None):
        self.u_id = u_id
        self.u_name = u_name
        self.u_name_ex = u_name_ex
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<U_NAME_EX %r>' % (self.u_name_ex)

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

class RaceCalendar(Base):
    __tablename__ = 'race-calendar'
    race_id = Column(Integer, primary_key=True)
    calendar_id = Column(Integer)
    race_name = Column(String(128))
    race_meters = Column(Integer)
    race_type_distance = Column(String(128))
    race_type_ground = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, race_id=None, calendar_id=None, race_name=None, race_meters=None, race_type_distance=None, race_type_ground=None, created_at=None, updated_at=None):
        self.race_id = race_id
        self.calendar_id = calendar_id
        self.race_name = race_name
        self.race_meters = race_meters
        self.race_type_distance = race_type_distance
        self.race_type_ground = race_type_ground
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<race_name %r>' % (self.race_name)

class Calender(Base):
    __tablename__ = 'calendar'
    calendar_id = Column(Integer, primary_key=True)
    calendar_name = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, calendar_id=None, calendar_name=None, created_at=None, updated_at=None):
        self.calendar_id = calendar_id
        self.calendar_name = calendar_name
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<calendar_name %r>' % (self.calendar_name)
