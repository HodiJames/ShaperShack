FROM python:3.11-slim

WORKDIR /app

# Upgrade pip first
RUN pip install --upgrade pip

# Copy and install requirements with Emergent's private package index
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/ -r requirements.txt

COPY backend/ ./backend/

ENV PORT=8001

CMD ["python", "-m", "uvicorn", "backend.server:app", "--host", "0.0.0.0", "--port", "8001"]
