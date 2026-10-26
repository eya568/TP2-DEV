import socket
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "it works!"};
@app.get("/addition")
def addition(a: float, b: float):
    return {"result": a + b}
def home():
    return {"message": "it works!"}


@app.get("/greeting")
def greeting(name: str):
    # Nom du PC qui héberge l'application
    hostname = socket.gethostname()

    # Adresse IPv4 de l'interface utilisée pour sortir vers Internet
    ip = "Unavailable"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    except OSError:
        pass
    finally:
        sock.close()

    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "IP": ip
    }
class Numbers(BaseModel):
    a: float
    b: float

@app.post("/multiply")
def multiply(numbers: Numbers):
    return {"result": numbers.a * numbers.b, "developper": "Dev1"}


class DivideRequest(BaseModel):
    a: float
    b: float


@app.post("/divide")
def divide(payload: DivideRequest):
    if payload.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": payload.a / payload.b}
