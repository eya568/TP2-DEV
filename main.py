from fastapi import FastAPI;

app = FastAPI();

@app.get("/")
def read_root():
    return {"message": "it works!"};
@app.get("/addition")
def addition(a: float, b: float):
    return {"result": a + b}
