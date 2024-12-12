FROM python:3.12

WORKDIR /usr/src/app

# Set environment variables used by the flask command
#ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Install gcc and other dependencies
#RUN apk add --no-cache gcc musl-dev linux-headers
# Copy requirements.txt and install the Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --root-user-action=ignore

COPY app.py .

# Add metadata to the image to describe that the container is listening on port 5672
EXPOSE 5672

CMD ["python", "app.py" ]
