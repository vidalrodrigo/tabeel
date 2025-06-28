FROM python:3.11

WORKDIR /app/api

COPY api/ ./
COPY api/manage.py ./
COPY api/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
