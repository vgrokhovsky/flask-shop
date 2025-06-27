FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    build-essential  
WORKDIR /app

COPY deploy/app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
COPY run.py /app/run.py

# Для start.sh
COPY start.sh /app/start.sh
RUN sed -i 's/\r$//' /app/start.sh && \
    chmod +x /app/start.sh

# Для wait-for-it.sh
COPY deploy/app/wait-for-it.sh /app/wait-for-it.sh
RUN sed -i 's/\r$//' /app/wait-for-it.sh && \
    chmod +x /app/wait-for-it.sh

COPY migrations /app/migrations


ENV FLASK_APP=run.py
ENV FLASK_ENV=production

EXPOSE 5000

# Запуск через start.sh
CMD ["./start.sh"]
