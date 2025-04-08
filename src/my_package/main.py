from dotenv import load_dotenv
import logging
from fastapi import FastAPI
from typing import Dict, Union, Any
from src.my_package.services.hello_world_service import HelloWorldService
from src.my_package.types.main_types import Item

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
def read_item(item_id: int, q: Union[str, None] = None) -> Dict[str, Union[int, str, None]]:
    """
    GET endpoint that retrieves an item by ID with an optional query parameter.
    - Takes a required path parameter item_id (integer)
    - Takes an optional query parameter q (string)
    - Returns a dictionary with the item_id and query parameter value
    """
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> Dict[str, Union[int, str]]:
    """
    PUT endpoint that updates an item by ID.
    - Takes a required path parameter item_id (integer)
    - Takes a required request body of type Item (with name, price, is_offer fields)
    - Returns a dictionary with the updated item name and ID
    """
    return {"item_name": item.name, "item_id": item_id}
