FROM python:3.11

WORKDIR /app/backend

COPY backend/ ./
COPY backend/manage.py ./
COPY backend/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
