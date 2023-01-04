# Here, we started with a slim-buster-based Docker image for Python 3.10.3. 
# We then set a working directory along with two environment variables:

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)

# pull official base image
FROM python:3.10.3-slim-buster

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
# RUN chmod +x /usr/src/app/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"] 
ENTRYPOINT ["./entrypoint.sh"]