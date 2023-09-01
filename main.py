from fastapi import FastAPI
import uvicorn
import mysql.connector

app = FastAPI()

# Connect to MySQL database 
db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="demo"
)
cursor = db.cursor()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items")
async def get_items():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return {"data": items}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    return {"data": item}

@app.post("/items") 
async def add_item(name: str):
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
    db.commit()
    return {"message": "Item added"}
    
if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)