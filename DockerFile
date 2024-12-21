# Usar una imagen base de Python
FROM python:3.12.3

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Actualizar pip y instalar dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Asegurar que el script entrypoint.sh tenga permisos de ejecución
RUN chmod +x entrypoint.sh

# Definir el entrypoint para ejecutar el script cuando se inicie el contenedor
CMD ["bash", "entrypoint.sh"]
