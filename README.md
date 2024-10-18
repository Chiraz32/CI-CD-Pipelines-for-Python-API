# CI/CD Pipelines For Temperature Converter - Mini Project

This project is a Python-based temperature conversion API built using FastAPI. It supports conversions between Celsius, Fahrenheit, and Kelvin. The project is containerized using Docker and employs GitHub Actions for CI/CD automation, including testing, Docker image building, and deployment to Railway.

## Features

- Convert temperatures between Celsius, Fahrenheit, and Kelvin.
- Built with FastAPI for creating lightweight RESTful APIs.
- Automated tests using pytest.
- CI/CD pipelines using GitHub Actions for:
  - Automatically creating pull requests on feature branch pushes.
  - Deploying to [Railway](https://railway.app/) on pushes to the `master` branch.
  - Running tests during pull requests.
  - Building and pushing Docker images to Docker Hub.

## Architecture

```
📂 Project Root
├── 📄 main.py               # Core FastAPI app with temperature conversion logic.
├── 📄 test_main.py          # Unit tests for temperature conversion API.
├── 📄 requirements.txt      # Python dependencies for building the project.
├── 📄 Dockerfile            # Dockerfile for building the container.
├── 📂 .github/workflows     # GitHub Actions workflow files.
│   ├── create-pull-request.yml   # Workflow to automate pull request creation.
│   ├── deploy.yml                # Workflow to deploy the application to Railway.
│   ├── docker_build.yml          # Workflow to build and push Docker image on `master`.
│   └── run-test.yml              # Workflow to run tests on pull requests.
└── 📄 README.md            # Project documentation.
```

### FastAPI API Endpoints

| Method | Endpoint                    | Description                                |
|--------|-----------------------------|--------------------------------------------|
| `GET`  | `/celsius-to-fahrenheit`     | Convert Celsius to Fahrenheit.             |
| `GET`  | `/fahrenheit-to-celsius`     | Convert Fahrenheit to Celsius.             |
| `GET`  | `/celsius-to-kelvin`         | Convert Celsius to Kelvin.                 |
| `GET`  | `/kelvin-to-celsius`         | Convert Kelvin to Celsius.                 |
| `GET`  | `/fahrenheit-to-kelvin`      | Convert Fahrenheit to Kelvin.              |


## CI/CD Pipelines

### 1. Automated Pull Request Creation

When code is pushed to the `api_feature` branch, the `create-pull-request.yml` workflow automatically creates a pull request to merge into the `master` branch.

### 2. Automated Deployment to Railway

On pushing to the `master` branch, the `deploy.yml` workflow deploys the latest version of the API to Railway using the Railway CLI.

### 3. Docker Image Build and Push

The `docker_build.yml` workflow builds a Docker image of the API and pushes it to Docker Hub, tagged with the commit’s short SHA hash.

### 4. Running Tests on PRs

The `run-test.yml` workflow runs all unit tests via `pytest` on every pull request to the `master` branch.

## Environment Variables

For Docker Hub and Railway deployments, the following environment variables are required:

- `DOCKER_USERNAME`: Docker Hub username.
- `DOCKER_PASSWORD`: Docker Hub password.
- `RAILWAY_TOKEN`: Railway authentication token.

These variables should be set in the GitHub repository secrets for use in the CI/CD workflows.
### Required Permissions

In order to run the GitHub Actions workflows effectively, some permissions need to be enabled in your repository settings:

1. **Workflow Permissions**: 
   - Set **Read and Write permissions** for GitHub Actions to allow them to modify and push code.
   - Check the box for **Allow GitHub Actions to create and approve pull requests** (as shown in the first image below).

   ![Workflow Permissions](./images/workflow_permissions.png)

2. **Branch Protection Rules**: 
   - Set up branch protection rules for the `master` branch to require pull requests before merging.
   - Enable **Require status checks to pass before merging** to ensure that tests are successful before merging changes into `master` (as shown in the second image below).

   ![Branch Protection Rule](./images/branch_protection_rule.png)

## Testing

Unit tests are included in `test_main.py`. To run the tests, simply execute:

```bash
pytest test_main.py
```

## Deployment

The project is deployed automatically to [Railway](https://railway.app/) using the `deploy.yml` GitHub Actions workflow. Once a push is made to the `master` branch, the app will be redeployed using the Railway CLI.

## Requirements

The `requirements.txt` file contains all necessary Python dependencies:

```
fastapi
uvicorn
pytest
```

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## How to Run the Project

### Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/temperature-converter.git
    cd temperature-converter
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

4. Access the API at `http://127.0.0.1:8000`.

### Using Docker

1. Build the Docker image:
    ```bash
    docker build -t temperature_converter .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 temperature_converter
    ```

3. Access the API at `http://127.0.0.1:8000`.




