# Imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app/api

# Copia TODO o conteúdo da pasta 'api' (inclui manage.py, requirements.txt, web_app, etc)
COPY api/ ./

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Coleta os arquivos estáticos para produção
RUN python manage.py collectstatic --noinput

# Aplica as migrations
RUN python manage.py migrate

# Expõe a porta usada pelo Gunicorn
EXPOSE 8000

# Inicia o servidor Django com Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
