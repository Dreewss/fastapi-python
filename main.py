from fastapi import FastAPI
from fastapi.responses import FileResponse
from json_db import JsonDB
from product import Product
from indb import generate_products
from typing import List

app = FastAPI()

productDB = JsonDB(path="./data/products.json")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API"}

@app.get("/products")
def get_products():
    products = productDB.read()
    return {"products": products}

@app.post("/products")
def create_products(product: Product):
    product_dict = product.dict()
    productDB.insert(product_dict)
    return {"status": "inserted"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("path/to/your/favicon.ico")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
