FROM python:3.9-slim

WORKDIR /app
RUN apt-get -y update 
RUN apt-get -y install curl
COPY requirement.txt .
RUN pip install --upgrade pip
RUN pip install -r requirement.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]