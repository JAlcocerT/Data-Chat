FROM python:3.12.3-slim
# https://hub.docker.com/_/python

# LABEL org.opencontainers.image.source https://github.com/JAlcocerT/Data-Chat
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

#EXPOSE 8000

# Run the Streamlit app
#CMD ["streamlit", "run", "app.py"]

# docker build -t langchain_mem0 .
# podman build -t langchain_mem0 .