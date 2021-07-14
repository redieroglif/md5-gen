FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./src /app
CMD celery -A tasks worker -D && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 80 --reload