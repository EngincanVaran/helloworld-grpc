FROM python:3.10-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "server.py"]
EXPOSE 50051
