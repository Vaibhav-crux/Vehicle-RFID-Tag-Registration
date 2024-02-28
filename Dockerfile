FROM python:3.11-slim as builder

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY app/main.py .

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app .

CMD ["python", "main.py"]
