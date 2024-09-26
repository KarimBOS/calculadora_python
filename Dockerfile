# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo calculator.py al directorio de trabajo
COPY calculadora.py /app

# Comando para ejecutar el archivo Python
CMD ["python", "calculadora.py"]
