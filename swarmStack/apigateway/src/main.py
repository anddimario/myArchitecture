from fastapi import FastAPI  

app = FastAPI()   

@app.get("/") 
async def main_route():
  print("ciao mod")
  return {"message": "Hey, It is me And! - green"}

@app.get("/health") 
async def health_route():
  return {"status": "Alive"}