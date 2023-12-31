from fastapi import FastAPI
from typing import Union

#creacion de una aplicacion
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Mundo leonardo"}


@app.get("/hola")
def read_root():
    return {"Hola": "Mundo leonardo 2"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}     

@app.get("/calculadora")
def calcular(operando_1: float, operando_2:float):
    return {'suma':operando_1+operando_2 }