import uvicorn
from app import app
from app import config


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.get("host_name"),
        port=config.get("port"),
    )
