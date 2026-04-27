from fastapi import FastAPI
from asyncio 

app = FastAPI()

async def simulated_io_task():
    # Simulate an I/O-bound task (e.g., database query, API call)
    await asyncio.sleep(1)  # Simulating a delay of 1 second
    return "I/O task completed"


@app.get("/async-data")
async def get_data():
    result = await simulated_io_task()
    return {"message": result}