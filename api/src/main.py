from fastapi import FastAPI, File, UploadFile
from db.base import Session
from db.models import Task
from tasks import gen_md5
import binascii

app = FastAPI()

# Getting task info by ID
@app.get("/api/item/{item_id}")
async def read_item(item_id):
    session = Session()
    item = session.query(Task).get(item_id)
    return item

# Adding new task to queue and DB
@app.post("/api/item/")
async def add_item(file: UploadFile = File(...)):
    
    # Creating DB entry
    session = Session()
    task = Task(
        hash_ready = False
    )
    session.add(task)
    session.commit()
    
    # Getting DB entry ID (PK)
    task_id = task.id
    session.close()

    # Decoding data for serialisation
    data = binascii.b2a_base64(file.file.read()).decode()

    # Adding data to queue
    promise = gen_md5.delay(data, task_id)
    
    # Returning database ID and promise ID
    return {"id": task_id, "promise_id": promise.id}
