FROM python:3.8-alpine
RUN apk add --update py-pip
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY ./src /app
RUN export FLASK_APP=app.py
EXPOSE 5555
CMD [ "flask","run", "--host=0.0.0.0","--port=5050"]
