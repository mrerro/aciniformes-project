import uvicorn
from .routes import app


if __name__ == "__main__":
    uvicorn.run(app)
