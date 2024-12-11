FROM python:3.10

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências e instalar
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar código e arquivos de configuração necessários
COPY app/ /app/

# Expor a porta e iniciar a aplicação
EXPOSE 8080
CMD ["python", "analysis_with_flask.py"]