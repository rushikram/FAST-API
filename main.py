from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # Replace with your actual data fetching logic
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    item = {"item_id": item_id, "name": f"Item {item_id}"}
    return item 
