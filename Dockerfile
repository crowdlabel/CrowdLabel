FROM python:3.11
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/backend .
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80"]