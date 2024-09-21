from typing import Optional
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine

# Tables
class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    floor: int
    description: str

class Sensor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    location_id: int = Field(foreign_key="location.id")

class TemperatureReading(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sensor_id: int = Field(foreign_key="sensor.id")
    temperature: float
    timestamp: datetime

# Engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
session = Session(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def insert_locations():
    location_1 = Location(floor=1, description="First floor (RDC).")
    location_2 = Location(floor=2, description="Second floor.")

    session.add(location_1)
    session.add(location_2)

    session.commit()

    session.close()

def insert_sensors():
    sensor_1 = Sensor(name="Sensor 1", location_id=1)
    sensor_2 = Sensor(name="Sensor 2", location_id=2)

    session.add(sensor_1)
    session.add(sensor_2)

    session.commit()

    session.close()

def insert_temperature_readings():
    temperature_reading_1 = TemperatureReading(sensor_id=1, temperature=20.5, timestamp=datetime.now())
    temperature_reading_2 = TemperatureReading(sensor_id=2, temperature=21.5, timestamp=datetime.now())

    session.add(temperature_reading_1)
    session.add(temperature_reading_2)

    session.commit()

    session.close()

if __name__ == "__main__":
    create_db_and_tables()
    insert_locations()
    insert_sensors()
    insert_temperature_readings()