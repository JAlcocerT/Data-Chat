FROM python:3.10.12
# https://hub.docker.com/_/python

# LABEL org.opencontainers.image.source https://github.com/JAlcocerT/Streamlit-MultiChat
# LABEL maintainer="Jesus Alcocer Tagua"

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    nano \
    g++ 
    # \
    # && rm -rf /var/lib/apt/lists/*

# Install production dependencies.
RUN pip install -r requirements.txt

EXPOSE 8000

# Run the Streamlit app
#CMD ["streamlit", "run", "app.py"]

# docker build -t py_test_pandasai_groqapi .
# podman build -t py_test_pandasai_groqapi .


#docker exec -it py_3_10_paigroq /bin/bash
#podman exec -it py_3_10_paigroq /bin/bash

# export GROQ_API_KEY=""
# export GROQ_API_KEY=""

# version: '3.8'

# services:
#   my_python_dev_container:
#     image: py_test_pandasai_groqapi #python:3.10
#     container_name: py_3_10_paigroq
#     ports:
#       - "8701:8501"
#     working_dir: /app
#     #command: python3 app.py
#     command: tail -f /dev/null #keep it running