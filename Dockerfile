# Step 1: official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Install system dependencies for the app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Step 4: Copy only the requirements.txt first (for caching dependency installation)
COPY ./requirements.txt /app/requirements.txt

# Step 5: dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Step 6: Copy the rest of the application code
COPY . /app

# Step 7: port where FastAPI app will run on
EXPOSE 8000

# Step 8: environment variables for production environments
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ENV production
#ENV MONGO_URI mongodb://alex24:alextheroot24@mongo:27017/mydatabase
ENV MONGO_URI mongodb://mongo:27017/mydatabase

# Step 9: Uvicorn to run the FastAPI app
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]

