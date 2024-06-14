# Usa la imagen base de Python
FROM python:3.9


# Copia los archivos necesarios al contenedor
COPY . /app
# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Expone el puerto 5000 para que Flask pueda ser accedido externamente
EXPOSE 5000

# Define la variable de entorno FLASK_APP
ENV FLASK_APP=main.py

# Define el nombre del contenedor
LABEL name="comparador"

# Ejecuta la aplicación Flask al iniciar el contenedor
ENTRYPOINT python main.py