# Using official python runtime base image
FROM python:3.10
ENV PYTHONUNBUFFERED=1
# Set the application directory
WORKDIR /restaurant
COPY requirements.txt /restaurant/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /restaurant/

