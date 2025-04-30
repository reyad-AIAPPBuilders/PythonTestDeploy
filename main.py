from fastapi import FastAPI
from routes import items

app = FastAPI()

# Include routes
app.include_router(items.router)
