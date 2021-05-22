from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class UName(Base):
    __tablename__ = 'u-name'
    u_id = Column(Integer, primary_key=True)
    u_farm_name = Column(String(128))
    u_name = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, u_id=None, u_farm_name=None, u_name=None, created_at=None, updated_at=None):
        self.u_id = u_id
        self.u_farm_name = u_farm_name
        self.u_name = u_name
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<U_FARM_NAME %r>' % (self.u_farm_name)

class URaceSchedule(Base):
    __tablename__ = 'u-race-schedule'
    u_id = Column(Integer, primary_key=True)
    class_id = Column(Integer)
    race_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, u_id=None, class_id=None, race_id=None, created_at=None, updated_at=None):
        self.u_id = u_id
        self.class_id = class_id
        self.race_id = race_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<U_id %r>' % (self.u_id)

class RaceCalendar(Base):
    __tablename__ = 'race-calendar'
    race_id = Column(Integer, primary_key=True)
    class_id = Column(Integer)
    calendar_id = Column(Integer)
    race_grade_id = Column(Integer)
    race_grade = Column(String(128))
    race_course_id = Column(Integer)
    race_course = Column(String(128))
    race_name = Column(String(128))
    race_meters = Column(Integer)
    race_type_distance_id = Column(Integer)
    race_type_distance = Column(String(128))
    race_type_ground_id = Column(Integer)
    race_type_ground = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self,
                      race_id=None,
                      class_id=None,
                      calendar_id=None,
                      race_grade_id=None,
                      race_grade=None,
                      race_course_id=None,
                      race_course=None,
                      race_name=None,
                      race_meters=None,
                      race_type_distance_id=None,
                      race_type_distance=None,
                      race_type_ground=None,
                      race_type_ground_id=None,
                      created_at=None,
                      updated_at=None
    ):
        self.race_id = race_id
        self.class_id = class_id
        self.calendar_id = calendar_id
        self.race_grade_id = race_grade_id
        self.race_grade = race_grade
        self.race_course_id = race_course_id
        self.race_course = race_course
        self.race_name = race_name
        self.race_meters = race_meters
        self.race_type_distance_id = race_type_distance_id
        self.race_type_distance = race_type_distance
        self.race_type_ground_id = race_type_ground_id
        self.race_type_ground = race_type_ground
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<race_name %r>' % (self.race_name)

class Calender(Base):
    __tablename__ = 'calendar'
    class_id = Column(Integer, primary_key=True)
    calendar_id = Column(Integer, primary_key=True)
    calendar_name = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, calendar_id=None, class_id=None, calendar_name=None, created_at=None, updated_at=None):
        self.class_id = class_id
        self.calendar_id = calendar_id
        self.calendar_name = calendar_name
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<calendar_name %r>' % (self.calendar_name)
