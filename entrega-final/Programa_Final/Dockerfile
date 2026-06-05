FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias necesarias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente y el dataset
COPY . .

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando por defecto para correr la app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
