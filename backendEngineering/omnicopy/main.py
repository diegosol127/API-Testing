from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()


# Decorator describing how we associate a webpage visit to a certain function
# Path operation function
@app.get("/")
async def root():
    return {"message": "Hello world!"}
