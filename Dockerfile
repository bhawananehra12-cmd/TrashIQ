
FROM python:3.10.11-slim


RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 10000


CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
