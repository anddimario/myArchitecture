from fastapi import FastAPI  

app = FastAPI()   

@app.get("/") 
async def main_route():
  print("ciao mod")
  return {"message": "Hey, It is me And! - mod"}