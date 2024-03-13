FROM python:3.10-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
