FROM python:3.8
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app
ADD . /app
RUN export FLASK_APP=stock_flask.py
RUN pip3 install -r requirements.txt
EXPOSE 5555
CMD [ "flask","run", "--host=0.0.0.0","--port=5555"]
