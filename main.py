from fastapi import FastAPI
from settings import init

app = FastAPI()

def startups():
    settings = init()
