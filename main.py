from typing import Optional

import uvicorn

from fastapi import FastAPI

import requests



app = FastAPI()
ceps = [12250480, 12220430, 12230380, 12230460]

@app.get("/")
def root():
    return {"key": "value"}

@app.get("/ceps")
def get_ceps():
    return {"data": ceps}


@app.get("/ceps/{cep}")
def get_cep(cep: int):
    data = requests.get(f"https://viacep.com.br/ws/{cep}/json")
    data = data.json()
    print(data)
    return {"data": data}
