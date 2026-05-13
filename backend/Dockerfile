FROM python:3.12-alpine

WORKDIR /app

RUN adduser -D appuser

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
