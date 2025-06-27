# Etapa 1: imagem base completa (não é slim)
FROM python:3.11

# Etapa 2: define diretório de trabalho
WORKDIR /app

# Etapa 3: copia os arquivos necessários
COPY backend/ ./backend/
COPY backend/manage.py ./
COPY backend/requirements.txt ./

# Etapa 4: instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: expõe a porta do servidor
EXPOSE 8000

# Etapa 6: comando para rodar o servidor com Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
