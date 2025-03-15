# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /backend

# Copy the project files to the container
COPY . /backend/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Django runs on
EXPOSE 8000

# Run migrations and start Django server
CMD ["sh", "-c", "cd backend && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]