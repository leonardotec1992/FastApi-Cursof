from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

#creacion de una aplicacion
app = FastAPI()

class Item(BaseModel):
    name:str
    price: float
    is_offer:Union[bool, None]= None

@app.get("/")
def read_root():
    return {"Hello": "Mundo leonardo genial"}


@app.get("/hola")
def read_root():
    return {"Hola": "Mundo leonardo 2"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}     

@app.get("/calculadora")
def calcular(operando_1: float, operando_2:float):
    return {'suma':operando_1+operando_2 }