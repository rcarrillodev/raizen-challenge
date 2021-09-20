FROM python:3.9-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

ENTRYPOINT ["gunicorn"]

CMD ["-b 0.0.0.0:8000","sensors.app"]