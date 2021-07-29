FROM python:3.6.14-alpine as base
RUN mkdir -p /home/vernacular
WORKDIR /home/vernacular
COPY . .
RUN ["pip3", "install", "-r", "requirements.txt"]
RUN python3 manage.py migrate
ENTRYPOINT ["python3", "manage.py","runserver","0.0.0.0:8000"]

