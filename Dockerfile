FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

EXPOSE 8080

CMD ["sh", "-c", "uvicorn backend.server:app --host 0.0.0.0 --port $PORT"]
