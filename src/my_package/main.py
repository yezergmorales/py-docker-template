from fastapi import FastAPI
import uvicorn
from my_package.services.hello_world_service import HelloWorldService

app = FastAPI()
service = HelloWorldService()

@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint that returns a hello world message."""
    return {"message": service.say_hello()}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)