
import socket
from fastapi import FastAPI

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
