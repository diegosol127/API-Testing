from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI(root_path="/api/v1")


# Decorator describing how we associate a webpage visit to a certain function
# Path operation function
@app.get("/")
async def root():
    return {"message": "Hello world!"}


"""
Campaigns
 - campaign_id
 - name
 - due_date
 - created_at
 """


@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns": "example"}
