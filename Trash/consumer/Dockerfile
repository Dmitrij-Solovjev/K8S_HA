FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install pika
ENV PYTHONUNBUFFERED=1

COPY consumer.py app.py
EXPOSE 5672

CMD ["python", "app.py" ]
