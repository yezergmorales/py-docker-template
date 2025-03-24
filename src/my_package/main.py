from fastapi import FastAPI
from typing import Dict, Union
from src.my_package.services.hello_world_service import HelloWorldService

app = FastAPI()
service = HelloWorldService()

@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint that returns a hello world message."""
    return {"message tal": service.say_hello()}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def read_item(item_id: Union[int, str] = None):
    return {"item_id": item_id}

