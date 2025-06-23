
FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    build-essential # gcc

WORKDIR /app

COPY deploy/app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
COPY run.py /app/run.py


ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000


EXPOSE 5000

RUN wait-for-it.sh db:3306 --timeout=30 --strict

RUN flask db init
RUN flask db migrate -m "Initial migration."
RUN flask db upgrade

CMD ["flask", "run"]