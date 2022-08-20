import requests
import logging.config

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator 

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__) 
logger.info("fdffffffffffff")

app = FastAPI()

@app.get("/")
def read_root():
    response = api1()
    return {"InfoUsers": response }

@app.get("/API1Taller2/{idUsuario}")
def read_user(idUsuario : str):
    list=api1()
    for usr in list:
        print(usr)
        if usr["idUsuario"]==idUsuario:
            return usr

def api1():
    url='https://62fc67e61e6a530698a5ee17.mockapi.io/API1Taller2'
    response = requests.get(url, {}, timeout=5)
    return response.json()


Instrumentator().instrument(app).expose(app)