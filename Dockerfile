FROM python:3.8-alpine
RUN apk add --update py-pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY ./src /app
RUN set FLASK_APP=src/app.py
RUN export FLASK_ENV=development
EXPOSE 5050
CMD [ "python","app.py"]
