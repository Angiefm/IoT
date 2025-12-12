from fastapi import FastAPI
from service.database import get_data_environment, save_data, get_data_history
from fastapi import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "IoT Final Capstone Project – Environmental Monitoring API. This service collects, decodes, and exposes real-time environmental metrics for industrial settings."}

@app.get("/environment")
async def metrics() :  
    return get_data_environment()

@app.get("/environment/history")
async def metrics() :  
    return get_data_history()

@app.post("/environment")
async def process_data(data: dict = Body(...)):
    save_data(data)
    return {"message": "success"}
