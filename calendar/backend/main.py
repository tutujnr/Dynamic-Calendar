from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
import motor.motor_asyncio
from bson import ObjectId

app = FastAPI()

# Database setup
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.calendar_db
collection = db.events

# Event model
class Event(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime

class EventInDB(Event):
    id: str

@app.post("/events/", response_model=EventInDB)
async def create_event(event: Event):
    result = await collection.insert_one(event.dict())
    event_id = result.inserted_id
    return EventInDB(id=str(event_id), **event.dict())

@app.get("/events/", response_model=List[EventInDB])
async def get_events():
    events = []
    async for event in collection.find():
        events.append(EventInDB(id=str(event["_id"]), **event))
    return events

@app.get("/events/{event_id}", response_model=EventInDB)
async def get_event(event_id: str):
    event = await collection.find_one({"_id": ObjectId(event_id)})
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventInDB(id=str(event["_id"]), **event)

@app.put("/events/{event_id}", response_model=EventInDB)
async def update_event(event_id: str, event: Event):
    result = await collection.update_one({"_id": ObjectId(event_id)}, {"$set": event.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventInDB(id=event_id, **event.dict())

@app.delete("/events/{event_id}", response_model=dict)
async def delete_event(event_id: str):
    result = await collection.delete_one({"_id": ObjectId(event_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"status": "success"}
