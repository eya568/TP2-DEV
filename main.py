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

@app.delete("/remove/{id}")
def remove_item(id: int):
    return {"message": f"Item {id} removed"}

# ---------- PUT /update/{id} ----------

class UpdateRequest(BaseModel):
    name: str
    value: float


# "base de données" en mémoire (simulée)
items_db: dict[int, dict] = {
    1: {"name": "item1", "value": 10.0},
    2: {"name": "item2", "value": 20.0},
}


@app.put("/update/{id}")
def update_item(id: int, payload: UpdateRequest):
    if id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[id] = {"name": payload.name, "value": payload.value}
    return {"id": id, "item": items_db[id]}
