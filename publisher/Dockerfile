FROM python:3.12

RUN pip install pika
RUN pip install pyserial
RUN pip install PySide6
RUN pip install redis

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY publisher.py .

CMD ["python", "/usr/src/app/publisher.py"]
