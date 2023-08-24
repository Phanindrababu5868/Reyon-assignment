from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Enum as DBEnum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()

# Define the Item type enum
class ItemType(str, Enum):
    Domestic = "Domestic"
    Imported = "Imported"

# Define the database model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    quantity = Column(Integer)
    type = Column(DBEnum(ItemType))

# Create the database and tables
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Pydantic model for Item
class ItemCreate(BaseModel):
    name: str
    description: str
    quantity: int
    type: ItemType

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None
    type: Optional[ItemType] = None

@app.post("/item")
def add_item(item: ItemCreate):
    db = SessionLocal()
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.patch("/item/{item_id}")
def update_item(item_id: int, updates: ItemUpdate):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in updates.dict().items():
        if value is not None:
            setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    db.close()
    return {"message": "Item deleted"}

@app.get("/item")
def get_item_by_name(name: str):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.name == name).first()
    db.close()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
