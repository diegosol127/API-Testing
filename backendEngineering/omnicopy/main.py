from datetime import datetime
from fastapi import FastAPI, HTTPException
from typing import Any

# Create an instance of FastAPI
app = FastAPI(root_path="/api/v1")


# Decorator describing how we associate a webpage visit to a certain function
# Path operation function
@app.get("/")
async def root():
    return {"message": "Hello world!"}


data: Any = [
    {
        "campaign_id": 1,
        "name": "Summer Launch",
        "due_date": datetime.now(),
        "created_at": datetime.now(),
    },
    {
        "campaign_id": 2,
        "name": "Black Friday",
        "due_date": datetime.now(),
        "created_at": datetime.now(),
    },
]

"""
Campaigns
 - campaign_id
 - name
 - due_date
 - created_at
 """


@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns": data}


@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404)
