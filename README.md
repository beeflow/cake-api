# Cake API

[![](application/coverage.svg)]()

This Cake API project allows users to manage a collection of cakes. It meets the specified requirements and provides
endpoints for listing all cakes, adding a new cake, and deleting an existing cake. The API returns an OpenAPI or Swagger
spec for easy integration and client implementation.

## Requirements

* Docker and docker-compose
* Git

## Getting Started

To run this API locally, follow these steps:

### Prerequisites

Make sure you have Docker installed on your machine. If you don't have Docker installed, you
can [download it here](https://www.docker.com/get-started/).

### Installation

1. Clone the repository:
    ```shell
    $ git clone https://github.com/beeflow/cake-api
    ```

2. Navigate to the project directory:
    ```shell
    $ cd cake-api
    ```

3. Copy `env.dist` file to `.env` file in the `environment` directory
4. Edit `.env` file in the `environment` directory changing credentials, setting proper SECRET_KEY and removing comments
5. Build and run the Docker images using a command from the `bin` directory
   ```shell
   $ ./bin/start
   ```
   or docker-compose command
   ```shell
   $ docker-compose up -d
   ```

The API documentation should now be running locally at http://localhost

## Running tests

### Test coverage
Use `test-coverage` command from the  `bin` directory
```shell
$ ./bin/test-coverage
```

### Code quality
First install pre-commit hooks:
```shell
$ pre-commit install
```

The code quality will be checked and partially fixed before every commit.

## Technologies Used

* Server Framework: Django 5
* Data Persistence: PostgreSQL 12.4
* Language: Python 3.12
* Git
* Docker and docker-compose
