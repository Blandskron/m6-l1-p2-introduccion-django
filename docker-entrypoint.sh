#!/bin/sh

# Terminar ejecución inmediatamente si algún comando falla
set -e

echo "============================================="
echo "⚙️  Iniciando script de entrada Docker..."
echo "============================================="

echo "==> 1. Aplicando migraciones de base de datos..."
python manage.py migrate --noinput

echo "==> 2. Verificando integridad de Django..."
python manage.py check

echo "==> 3. Iniciando servidor web de desarrollo..."
echo "Servidor activo en: http://localhost:8000"
echo "============================================="

# Reemplaza el proceso actual con el comando del servidor
exec python manage.py runserver 0.0.0.0:8000
