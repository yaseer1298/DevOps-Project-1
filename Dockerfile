# Use an official lightweight Python image
FROM python:3.11-slim

WORKDIR /app

# copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# default port
EXPOSE 5000

CMD ["python", "app.py"]
