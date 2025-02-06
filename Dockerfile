FROM python:3.11

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Model download with optimizations
RUN python3 download_models.py

EXPOSE 8080
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
