from celery import Celery
from db.base import Session
from db.models import Task
import hashlib
import binascii

app = Celery('tasks', backend='rpc://', broker='pyamqp://rabbitmq:rKrSaDXJRe4cmDFn@rabitmq:5672//')

# MD5-generator task
@app.task
def gen_md5(data, db_id):
    
    # Encoding data
    data = binascii.a2b_base64(data)

    # Calculating hash
    hash = hashlib.md5(data).hexdigest()
    
    # Updating DB entry
    session = Session()
    item = session.query(Task).get(db_id)
    item.hash = hash
    item.hash_ready = True
    session.commit()
    session.close()

    return hash