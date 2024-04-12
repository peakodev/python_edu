# Homework 4

## Description

Web app with ability to store messages from /message URL to data.json unsing websocket in seperate thread

The project is structured as follows:

- `main.py`: This is the main script for the web server and web socket server.
- `file_handler.py`: This file for working with html files (read/write) and json file for storing data
- `logger.py`: logger conf
- `requirements.txt`: This file lists the Python dependencies that need to be installed.
- `Dockerfile`: This file is used to build a Docker image for the project.
- `entrypoint.sh`: This is a shell script that starts both the web server and the WebSocket server.

## Running the Project with Docker

To run the project with Docker, you first need to build the Docker image. You can do this with the following command:

```bash
docker build -t homework_04 .
```

This command builds a Docker image from the Dockerfile and tags it with the name homework_04.

```bash
docker run --name homework_04_container -d -p 8080:3000 -v $(pwd)/front-init/storage:/app/front-init/storage homework_04
```

This command starts a container from the myproject image and maps ports 3000 in the container to ports 8080 on the host machine.

Now, you should be able to access the web server at http://localhost:8080

