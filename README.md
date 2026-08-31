# API-Testing

Learn to work with APIs.

## Backend Engineering

Following lessons from [this YouTube playlist](https://www.youtube.com/playlist?list=PL_c9BZzLwBRIHUNeoywVJXViXGEsk6PDr) that shows how to use APIs in backend engineering.

**FastAPI**

- Following the tutorial [FastAPI Intro - Full CRUD REST API Tutorial](https://www.youtube.com/watch?v=k5abZLzsQc0)

FastAPI
- A popular framework for web development in Python
- Fast performance and fast to code
- [FastAPI](https://fastapi.tiangolo.com) website
- Built with Pydantic
  - Data validation library for Python

Goals
- CRUD capability API endpoints for campaigns
  - Create, read, update, delete
- See response codes
  - Success and error
- Schemas of data that we'll be working with

Project outline
- App that will help with copy writing content for marketing campaigns

**Launching the Web Server**

1. Navigate to the project.

```bash
cd backendEngineering/omnicopy
```

2. Activate the Python environment.

```bash
. ./.venv/bin/activate
```

3. Launch FastAPI.

```bash
fastapi dev main.py
```

4. Open browser to the server documentation page to inspect and test the interface.

**SQL Database**

You can inspect the contents of the SQL database by running `sqlite3 database.db` and then

```sql
SELECT * from campaign;
```

