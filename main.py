from fastapi import FastAPI
from fastapi.responses import FileResponse
from json_db import JsonDB
from product import Product

app = FastAPI()
productDB = JsonDB(path="./data/products.json")

@app.get("/")
def read_root():
    return {"message": "Olá, você acessou sua api"}

@app.get("/products")
def get_products():
    return {"products": productDB.read()}

@app.post("/products")
def create_products(product: Product):
    productDB.insert(product.dict())
    return {"status": "inserted"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("path/to/your/favicon.ico")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
