FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema necessárias para psycopg2 e outras libs Python
RUN apt-get update && apt-get install -y gcc libpq-dev

COPY backend/ ./backend/
COPY backend/manage.py ./
COPY backend/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
