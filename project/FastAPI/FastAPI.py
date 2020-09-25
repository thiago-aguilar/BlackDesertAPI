from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
from project.json_creator import create_item_json
import pandas as pd
import uvicorn

class Item(BaseModel):
    item_id: int
    item_enhancement: int

app = FastAPI()
dataframe = None



@app.on_event("startup")
async def startup_event():
    dataframe = pd.read_csv('data/items.csv')


@app.post('/get_item')
async def create_item(item: Item):
    dataframe = pd.read_csv('data/items.csv')
    return create_item_json(item_id=item.item_id, dataframe=dataframe)[1]


@app.get("/items/{item_id}/{item_enhancement}")
async def read_items(item_id: str, item_enhancement: str):
    if not (isinstance(item_id, str) and isinstance(item_enhancement,str)):
        raise HTTPException(status_code=404, detail="Wrong request")
    dataframe = pd.read_csv('data/items.csv')
    item_id = int(item_id)
    item_enhancement = int(item_enhancement)
    item = Item(item_id=item_id, item_enhancement=item_enhancement)
    return_tuple = create_item_json(item_id=item.item_id, dataframe=dataframe, item_enhancement=item_enhancement)

    if return_tuple[0]:
        return return_tuple[1]
    else:
        raise HTTPException(status_code=404, detail="Item not found in database")


if __name__ == '__main__':

    uvicorn.run("FastAPI:app", host='0.0.0.0', port=5000, workers=2)