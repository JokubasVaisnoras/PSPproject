from fastapi import APIRouter, Depends, HTTPException, Response
import schema
import uuid
import database
import model
import datetime

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.get("/{employeeId}/paginated", response_model=schema.NotificationPaginated)
def get_notification_paginated(employeeId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):

    notification = db.query(model.Notification).filter(model.Notification.id == employeeId).all()
    return schema.NotificationPaginated(totalPages=1, id=employeeId, items=notification)


@router.post("/{employeeId}", response_model=schema.NotificationWithReceiver)
def send_notification_to_coworker(employeeId: uuid.UUID, info: schema.NotificationResponse ,db: database.SessionLocal = Depends(database.get_db)):
    db_table_item = model.Notification(id = employeeId, sender = info.sender, content = info.content, timestamp = datetime.datetime.now() , receiver = info.receiver)
    db.add(db_table_item)
    db.commit()
    db.refresh(db_table_item)
    return db_table_item