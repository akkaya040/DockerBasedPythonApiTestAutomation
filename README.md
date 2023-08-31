# Docker Based MockAPI and API Test Automation Project

This project enables you to create a mock API server and a basic automation test project to test this API and Validate Responses.

## Requirements
Docker

## Usage

1. Open a terminal in the root directory of the project.

2. To start the mock API server, use the following commands:

```bash
   % cd mock-api
   % ./mock-api> docker build -t mock-api-server . 
   % ./mock-api> docker run -p 8080:8080 mock-api-server
```

### To run the API test automation, use the following commands:

```bash
   % cd api-test-automation
   % ./api-test-automation> docker build -t api-test-automation .
   % ./api-test-automation>  docker run --network="host" api-test-automation
```


## Project Directory Structure
- mock-api: Contains the code for the mock API server.
- * app.py: Main application file for the mock API server.
- * data.json: Sample data for mock API responses.
- * Dockerfile: File to package the mock API application into a Docker container.

- api-test-automation: Contains the code for the API test automation project.
- * test_api.py: File containing API test scenarios.
- * Dockerfile: File to run the API tests within a Docker container.
- * schemas: Contains JSON schema files.
- * * product_schema.json: JSON schema file to validate product responses.
- * * unauthorized_schema.json: JSON schema file to validate 401 error responses.
- * * service_unavailable_schema.json: JSON schema file to validate 503 error responses.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


