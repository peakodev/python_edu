# Websocket chat with Exchanger

## Description

This project is a web application that includes a web server and a WebSocket server. The web server is responsible for handling HTTP requests and serving static files, while the WebSocket server is responsible for real-time communication between the client and the server.

The project is structured as follows:

- `web_server.py`: This is the main script for the web server.
- `websocket_server.py`: This is the main script for the WebSocket server.
- `requirements.txt`: This file lists the Python dependencies that need to be installed.
- `Dockerfile`: This file is used to build a Docker image for the project.
- `start_servers.sh`: This is a shell script that starts both the web server and the WebSocket server.

## Running the Project with Docker

To run the project with Docker, you first need to build the Docker image. You can do this with the following command:

```bash
docker build -t homework_05 .
```

This command builds a Docker image from the Dockerfile and tags it with the name homework_05.

```bash
docker run --name homework_05_container -d -p 8080:8080 -p 7070:7070 homework_05
```

This command starts a container from the myproject image and maps ports 8080 and 7070 in the container to ports 8080 and 7070 on the host machine.

Now, you should be able to access the web server at http://localhost:8080 and the WebSocket server at ws://localhost:7070.

