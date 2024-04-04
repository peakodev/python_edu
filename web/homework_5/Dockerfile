# Use a base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the code into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8080
EXPOSE 7070

# Add a shell script to start both servers
COPY start_servers.sh /app/start_servers.sh
RUN chmod +x /app/start_servers.sh

# Run the shell script
CMD ["/app/start_servers.sh"]