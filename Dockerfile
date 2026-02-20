FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 3004
ENV PORT=3004
CMD ["gunicorn", "-b", "0.0.0.0:3004", "-w", "2", "wsgi:app"]
