import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import datetime
import database
import uuid
import re

router = APIRouter(
    prefix="/payments",
    tags=["payments"]
)


@router.get("/{paymentId}", response_model=schema.PaymentWithId)
async def get_payment(paymentId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    payment = db.query(model.Payment).filter(model.Payment.id == paymentId).first()
    paymentWithId = schema.PaymentWithId(id=payment.id, price=payment.price, taxAmount=payment.taxAmount, tips=payment.tips, cardId=payment.cardId,
    paymentType=payment.paymentType, paymentDate=payment.paymentDate)
    return paymentWithId



@router.post("/order/{orderId}", response_model=schema.Payment, status_code=201)
def create_menu(orderId: uuid.UUID, payment: schema.PaymentCreate, db: database.SessionLocal = Depends(database.get_db)):
    db_payment = model.Payment(orderId=orderId, price=payment.price, taxAmount=payment.taxAmount, tips=payment.tips, cardId=payment.cardId,
    paymentType=payment.paymentType, paymentDate=payment.paymentDate)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

