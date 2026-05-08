from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from jose import JWTError, jwt
from app.payments import PaymentService, PaymentGateway

api = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret"

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@api.get("/")
def index():
    return "Hello"

@api.post("/pay")
def process_payment(method:str, token: dict = Depends(verify_token)):

    payment_service: PaymentService = PaymentGateway.build(method=method)

    return payment_service.process()
            