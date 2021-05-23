from sqlalchemy import Column, Integer, String
from models.database import Base

class UName(Base):
    __tablename__ = 'u-name'
    u_id = Column(Integer, primary_key=True)
    u_farm_name = Column(String(128))
    u_name = Column(String(128))
    created_at = Column(String(128))
    updated_at = Column(String(128))

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
    created_at = Column(String(128))
    updated_at = Column(String(128))

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
    race_name = Column(String(128))
    meters = Column(Integer)
    grade_id = Column(Integer)
    grade = Column(String(128))
    course_id = Column(Integer)
    course = Column(String(128))
    roll_id = Column(Integer)
    roll = Column(String(128))
    type_distance_id = Column(Integer)
    type_distance = Column(String(128))
    type_ground_id = Column(Integer)
    type_ground = Column(String(128))
    created_at = Column(String(128))
    updated_at = Column(String(128))

    def __init__(self,
                      race_id=None,
                      class_id=None,
                      calendar_id=None,
                      race_name=None,
                      meters=None,
                      grade_id=None,
                      grade=None,
                      course_id=None,
                      course=None,
                      roll_id=None,
                      roll=None,
                      type_distance_id=None,
                      type_distance=None,
                      type_ground_id=None,
                      type_ground=None,
                      created_at=None,
                      updated_at=None
    ):
        self.race_id = race_id
        self.class_id = class_id
        self.calendar_id = calendar_id
        self.race_name = race_name
        self.meters = meters
        self.grade_id = grade_id
        self.grade = grade
        self.course_id = course_id
        self.course = course
        self.roll_id = roll_id
        self.roll = roll
        self.type_distance_id = type_distance_id
        self.type_distance = type_distance
        self.type_ground_id = type_ground_id
        self.type_ground = type_ground
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<race_name %r>' % (self.race_name)

class Calender(Base):
    __tablename__ = 'calendar'
    class_id = Column(Integer, primary_key=True)
    calendar_id = Column(Integer, primary_key=True)
    calendar_name = Column(String(128))
    created_at = Column(String(128))
    updated_at = Column(String(128))

    def __init__(self, calendar_id=None, class_id=None, calendar_name=None, created_at=None, updated_at=None):
        self.class_id = class_id
        self.calendar_id = calendar_id
        self.calendar_name = calendar_name
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<calendar_name %r>' % (self.calendar_name)
