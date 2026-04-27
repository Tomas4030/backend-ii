from fastapi import FastAPI
from pydantic import BaseModel
from typing import List  

app = FastAPI()

class Cart(BaseModel):
    items: List[str]
    total_price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/Pay/")
def pay(email: str, cart: str, payment_method: str, payload: int):
    return {"email": email, "cart": cart, "payment_method": payment_method, "payload": payload}