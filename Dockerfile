# 1️⃣ Python version fix
FROM python:3.10.11-slim

# 2️⃣ System dependencies (TensorFlow ke liye)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3️⃣ Working directory
WORKDIR /app

# 4️⃣ Requirements copy & install
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 5️⃣ Project files copy
COPY . .

# 6️⃣ Expose port (Render uses 10000 internally)
EXPOSE 10000

# 7️⃣ Start command (Render compatible)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
