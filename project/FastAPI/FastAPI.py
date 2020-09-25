from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from project.json_creator import create_item_json
import pandas as pd
import uvicorn


class Item(BaseModel):
    item_id: int

app = FastAPI()
dataframe = None



@app.on_event("startup")
async def startup_event():
    dataframe = pd.read_csv('data/items.csv')


@app.post('/get_item')
async def create_item(item: Item):
    dataframe = pd.read_csv('data/items.csv')
    return create_item_json(item_id=item.item_id, dataframe=dataframe)[1]


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    dataframe = pd.read_csv('data/items.csv')
    item_id = int(item_id)
    item = Item(item_id=item_id)
    return create_item_json(item_id=item.item_id, dataframe=dataframe)[1]

if __name__ == '__main__':

    uvicorn.run("FastAPI:app", host='0.0.0.0', port=5000, workers=2)