# Dockerized Python Redirect App
This GitHub repository contains a Dockerized Python application that accepts incoming connections and redirects them to another website while also saving the redirection count locally. The application is built using Flask and Docker for easy deployment and management.

### Table of Contents
- Prerequisites
- Getting Started
- Running the Application
- Usage
- Configuration
- Contributing

___
### Prerequisites

Before you begin, ensure you have met the following requirements:

Docker installed on your system.
Getting Started
To get started with this project, follow these steps:

Running the Application
Clone this GitHub repository to your local machine.

``` bash
git clone https://github.com/metahedgehog/dockerized-link-redirection.git
```

Navigate to the project directory.

```bash
cd dockerized-link-redirection
```

Build the docker container

```bash
docker-compose build
```

Run container in background

```bash
docker-compose up -d
```

The application will start and be accessible at http://localhost:6100/. You can change the port in the docker-compose.yml file if needed.

___
### Usage

Once the application is up and running, you can access it through a web browser or make HTTP requests to it. Here are the available routes:

- '/': Accessing this route will redirect you to the target link specified in the environment variable TARGET_LINK. The redirection count will be saved locally, and the count will be incremented with each redirection.

- '/counter': Accessing this route will return the current redirection count.

Example usage with curl:

```bash
# Redirect to the target link
curl http://localhost:6100/

# Get the current redirection count
curl http://localhost:6100/counter
```

___
### Configuration

You can configure the application by modifying the environment variables in the .env file. The following variables are available:

- __TARGET_LINK__: The URL to which incoming connections will be redirected.

___
### Contributing



Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
