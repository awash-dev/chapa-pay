from fastapi import FastAPI, HTTPException
from chapaConfig import Payment
from pydantic import BaseModel, EmailStr, PositiveInt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define allowed origins for CORS
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://chapa-pay-ier8.onrender.com",  # Added new origin
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowed origins
    allow_credentials=True,   # Allow credentials
    allow_methods=["*"],      # Allow all methods
    allow_headers=["*"],      # Allow all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Payit(BaseModel):
    amount: PositiveInt  # Ensure amount is a positive integer
    fname: str
    lname: str
    email: EmailStr  # Validate email format

@app.post("/pay")
def pay(payit: Payit):
    try:
        data = Payment.pay(amount=payit.amount, fname=payit.fname, lname=payit.lname, email=payit.email)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class Txnum(BaseModel):
    ref_num: str

@app.post("/ver")
def verify(txnum: Txnum):
    try:
        ver = Payment.verify(tx_num=txnum.ref_num)
        return ver
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
