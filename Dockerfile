# Imagen base con Python 3.13 y sistema liviano
FROM python:3.13-slim-bookworm

# Ensure all system packages are up to date to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Evita preguntas interactivas
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza el sistema y agrega dependencias necesarias
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        tesseract-ocr \
        poppler-utils \
        libgl1 \
        libglib2.0-0 \
        build-essential \
        libsm6 \
        libxext6 \
        libxrender-dev \
        python3-dev \
        libpoppler-cpp-dev \
        git \
        curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias primero
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Puerto para Flask/Gunicorn
EXPOSE 5000

# Comando de inicio
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
