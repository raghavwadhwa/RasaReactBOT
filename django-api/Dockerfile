# Use an official Python runtime as a parent image
FROM python:3.8

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /app/django-api

# Install Python dependencies
COPY requirements.txt /app/django-api
RUN pip3 install --no-deps --upgrade pip -r requirements.txt

# Add the rest of the code
COPY . /app/django-api

# Make port 8000 available for the app
EXPOSE 8000

# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
CMD python3 manage.py runserver 0.0.0.0:8000
