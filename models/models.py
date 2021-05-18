from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import base
from datetime import datetime

class UName(Base):
    __tablename__ = 'u-name'
    u_id = Column(Integer, primary_key=True)
    u_name = Column(String(128))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
\
