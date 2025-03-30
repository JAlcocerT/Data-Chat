FROM python:3.10.12
#https://hub.docker.com/_/python

LABEL org.opencontainers.image.source https://github.com/JAlcocerT/Data-Chat
LABEL maintainer="Jesus Alcocer Tagua"
LABEL org.opencontainers.image.description="Talk with Your Data with Python and LLMs"
LABEL org.opencontainers.image.licenses=GPL-3.0

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# Install production dependencies.
RUN pip install -r requirements.txt

EXPOSE 8501

###podman build -t st_datachat .
#docker build -t st_datachat .