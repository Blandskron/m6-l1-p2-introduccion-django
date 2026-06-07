# Usar una imagen oficial de Python ligera
FROM python:3.13-slim

# Evitar la escritura de archivos .pyc en el disco del contenedor
ENV PYTHONDONTWRITEBYTECODE=1
# Evitar que Python almacene en búfer la salida de stdout/stderr
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto Django al contenedor
COPY djangotutorial/ /app/

# Copiar y dar permisos al script de entrada
COPY docker-entrypoint.sh /app/
RUN chmod +x /app/docker-entrypoint.sh

# Exponer el puerto por defecto de Django
EXPOSE 8000

# Definir el script de entrada que automatiza migraciones y levanta el servidor
ENTRYPOINT ["/app/docker-entrypoint.sh"]
