from sqlalchemy import Column, Integer, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class SensorLog(Base):
    __tablename__ = 'sensor_logs'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    temperature = Column(Float)
    humidity = Column(Float)
    co2 = Column(Float)
    pressure = Column(Float)

# Настройка подключения к SQLite
engine = create_engine('sqlite:///iot.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
