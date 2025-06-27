# Etapa 1: imagem base
FROM python:3.11-slim

# Etapa 2: define diretório de trabalho
WORKDIR /app

# Etapa 3: copia os arquivos
COPY backend/ ./backend/
COPY backend/manage.py ./
COPY backend/requirements.txt ./

# Etapa 4: instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: coleta arquivos estáticos (opcional se usar Django staticfiles)
# RUN python manage.py collectstatic --noinput

# Etapa 6: expõe a porta
EXPOSE 8000

# Etapa 7: comando para rodar o servidor com Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
