FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server .

CMD ["python", "server.py"]
EXPOSE 50051