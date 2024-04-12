# Use a base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 3000

RUN chmod +x /app/entrypoint.sh

# Run the shell script
CMD ["/app/entrypoint.sh"]