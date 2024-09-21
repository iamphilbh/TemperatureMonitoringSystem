import datetime
from typing import Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.params import Depends

from .database_models import create_db_and_tables, session, Location, Sensor, TemperatureReading
# from sqlalchemy import desc
# from sqlalchemy.orm import Session
# from database_models import create_db_and_tables, engine, session

app = FastAPI()

@app.on_event("startup")
async def startup():
    create_db_and_tables()

def get_db():
    database = session
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def root() -> Dict:
    return {"message": "Hello, World! This is the database API."}

@app.get("/locations")
def get_locations(db: session = Depends(get_db)):
    locations = db.query(Location).all()
    return locations

@app.get("/sensors")
def get_sensors(db: session = Depends(get_db)):
    sensors = db.query(Sensor).all()
    return sensors

@app.get("/temperature_readings")
def get_temperature_readings(db: session = Depends(get_db)):
    temperature_readings = db.query(TemperatureReading).all()
    return temperature_readings
