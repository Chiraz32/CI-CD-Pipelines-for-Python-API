# CI/CD Pipelines for Python API - DevOps Project

This project demonstrates a robust CI/CD pipeline implementation for a Python API. The API is built using FastAPI, containerized with Docker, and automated through GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD). The project automates pull request creating, unit tests running, Docker image building, and deployment to the cloud via Railway.

## DevOps Focused Features

- **Automated CI/CD Pipelines**: Leverages GitHub Actions for automated workflows, including testing, Docker image builds, and deployments.
- **Containerization**: Application is containerized using Docker for platform-independent deployments.
- **Cloud Deployment**: Continuous deployment to [Railway](https://railway.app/), a cloud-hosting platform, using GitHub Actions.
- **Version Control Integration**: Pull requests automatically created on new feature branches and tested before being merged into `master`.

## Project Architecture

```
📂 Project Root
├── 📄 main.py               # Core FastAPI app.
├── 📄 test_main.py          # Unit tests.
├── 📄 requirements.txt      # Python dependencies.
├── 📄 Dockerfile            # Docker container configuration.
├── 📂 .github/workflows     # GitHub Actions workflow files.
│   ├── create-pull-request.yml   # Automates pull request creation.
│   ├── deploy.yml                # Automates deployment to Railway.
│   ├── docker_build.yml          # Builds and pushes Docker images to Docker Hub.
│   └── run-test.yml              # Runs tests on pull requests.
└── 📄 README.md            # Project documentation.
```

## CI/CD Pipelines Overview

The project employs multiple GitHub Actions workflows to automate key aspects of the development and deployment lifecycle:

### 1. Automated Pull Request Creation

- **Trigger**: Pushing to the `api_feature` branch.
- **Workflow**: `create-pull-request.yml`
- **Description**: Automatically creates a pull request to merge feature branch changes into the `master` branch. This workflow helps streamline the code review and integration process.
  
### 2. Continuous Deployment to Railway

- **Trigger**: Pushing changes to the `master` branch.
- **Workflow**: `deploy.yml`
- **Description**: Deploys the latest code to [Railway](https://railway.app/) using the Railway CLI. Upon every push to `master`, the latest version of the application is redeployed to Railway, ensuring continuous and seamless updates to the live environment.

### 3. Docker Image Build and Push

- **Trigger**: Pushing changes to the `master` branch.
- **Workflow**: `docker_build.yml`
- **Description**: This workflow builds a Docker image for the application and pushes it to Docker Hub. The image is tagged with the short SHA of the corresponding commit, ensuring each version is uniquely identifiable and traceable.

### 4. Running Tests on Pull Requests

- **Trigger**: Creating a pull request to `master`.
- **Workflow**: `run-test.yml`
- **Description**: This workflow runs unit tests on each pull request using `pytest`. It ensures that changes submitted for review do not break existing functionality. The tests must pass successfully before the code is allowed to be merged into `master`.

- ### Environment Variables

To securely handle authentication and deployment in CI/CD pipelines, the following environment variables need to be configured as GitHub Secrets:

- `DOCKER_USERNAME`: Docker Hub username.
- `DOCKER_PASSWORD`: Docker Hub password.
- `RAILWAY_TOKEN`: Authentication token for Railway.

These variables allow the automation scripts to build Docker images and deploy them to Railway securely.

- ### Repository Configuration

To ensure the GitHub Actions workflows run smoothly, make sure the following repository settings are configured:

1. **Workflow Permissions**: 
   - Enable **Read and Write permissions** for GitHub Actions so they can modify code and create pull requests.
   - Enable the option **Allow GitHub Actions to create and approve pull requests** in repository settings.

   ![Workflow Permissions](./images/workflow_permissions.png)

2. **Branch Protection Rules**: 
   - Configure branch protection rules on the `master` branch to require pull requests before merging.
   - Enable **Require status checks to pass before merging** to ensure that tests are successfully executed before merging new changes.

   ![Branch Protection Rule](./images/branch_protection_rule.png)

## How CI/CD Works

### Workflow Triggers

- **Push to `api_feature` branch**: Automatically creates a pull request for review.
- **Push to `master` branch**: Triggers a deployment to Railway and a Docker image build and push to Docker Hub.
- **Pull requests to `master`**: Automatically runs the test suite to ensure no broken code is merged into the main branch.

### Key Benefits

- **Automated Testing**: Ensures that all new code changes are automatically tested, maintaining code quality.
- **Continuous Delivery**: New features and bug fixes are automatically deployed to the live environment without manual intervention, reducing deployment time.
- **Traceable and Reproducible Builds**: Docker images tagged with commit SHAs make it easy to track which version of the code is deployed at any given time.
- **Secure Secrets Management**: GitHub Secrets handle environment variables securely, reducing the risk of exposing sensitive information.

## How to Run the Project

### Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/devops-project.git
    cd devops-project
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
    docker build -t devops_project .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 devops_project
    ```

3. Access the API at `http://127.0.0.1:8000`.

## Conclusion

This project demonstrates a complete CI/CD pipeline implementation using GitHub Actions for a Python-based API. The pipeline automates pull request creation, testing, Docker image building, and cloud deployment, making it a practical demonstration of DevOps principles. It is designed for efficient, secure, and scalable deployment with minimal manual intervention, providing a real-world DevOps use case.
