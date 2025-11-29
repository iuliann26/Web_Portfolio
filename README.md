# Cloud-Native Portfolio Architecture

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
[![CI/CD Pipeline](https://github.com/iuliann26/Web_Portfolio/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/iuliann26/Web_Portfolio/actions)

> **Live Demo:** [https://portofoliu-iulian.azurewebsites.net/](https://portofoliu-iulian.azurewebsites.net/)

## 📖 About the Project

This repository hosts more than just a portfolio website. It serves as a comprehensive **DevOps Lab**, built to demonstrate the implementation of a modern, end-to-end Software Development Life Cycle (SDLC) using **Infrastructure as Code (IaC)**, **Containerization**, and **CI/CD** practices on Microsoft Azure.

The project started as a monolithic Flask application and evolved into a cloud-native, scalable, and secure architecture, solving real-world production challenges along the way (system drivers, network security, state management).

---

## 🏗️ Architecture & Tech Stack

The system is deployed on **Microsoft Azure**, leveraging PaaS services for scalability and reduced maintenance overhead.

![DevOps Lifecycle](https://upload.wikimedia.org/wikipedia/commons/0/05/Devops-toolchain.svg)

### Tech Stack
| Category | Technologies Used |
| :--- | :--- |
| **Backend** | Python 3.10, Flask, SQLAlchemy, Gunicorn |
| **Database** | **Azure SQL Database** (Serverless Tier - Auto-pause enabled for cost optimization) |
| **Infrastructure** | **Azure Web App for Containers**, Azure Container Registry (ACR) |
| **IaC** | **Terraform** (State Management & Provisioning) |
| **CI/CD** | **GitHub Actions** (Build, Test, Security Scan, Deploy) |
| **Quality & Security** | **Ruff** (Linting), **Black** (Formatting), **Trivy** (Container Security), **Pre-commit hooks** |

---

## 🚀 DevOps & CI/CD Pipeline

The pipeline is defined in `.github/workflows/ci-cd.yml`, automating code delivery from commit to production.

### Pipeline Stages:
1.  **Continuous Integration (CI):**
    * **Linting:** Enforcing code quality standards using `Ruff`.
    * **Testing:** Running unit and integration tests (Smoke Tests) using `pytest`.
    * **Security Scan:** Vulnerability scanning for code dependencies.
2.  **Continuous Delivery (CD):**
    * **Docker Build:** Building the container image (based on `python:3.11-slim`, optimized with ODBC drivers).
    * **Push:** Uploading the image to **Azure Container Registry (ACR)**.
    * **Deploy:** Updating the **Azure Web App** instance with the latest image.

---

## 🛠️ Infrastructure as Code (Terraform)

The infrastructure is not created manually ("ClickOps"), but defined as code in the `/infra` directory. This ensures:
* **Reproducibility:** The environment can be destroyed and recreated identically in minutes.
* **Versioning:** Infrastructure changes are tracked in Git.
* **State Management:** Managing resources like Resource Groups, App Service Plans, SQL Servers, and Firewall Rules via Terraform State.

```hcl
# Example snippet from main.tf
resource "azurerm_linux_web_app" "webapp" {
  name                = "app-portfolio"
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id
  
  site_config {
    always_on = false # Cost optimization for Dev plan
    application_stack {
      docker_image     = "${azurerm_container_registry.acr.login_server}/portfolio"
      docker_image_tag = "latest"
    }
  }
}


## Engineering Challenges & Solutions
Sigur, iată varianta în Engleză, gata de folosit.

Referitor la întrebarea ta: DA, neapărat pune secțiunea "Engineering Challenges" în README. Pentru un proiect de portofoliu, README-ul nu este doar "manual de instrucțiuni", este broșura ta de prezentare. Un recrutor tehnic va citi acea secțiune și va spune: "Wow, omul ăsta înțelege ce se întâmplă 'sub capotă', nu a dat doar copy-paste la un tutorial." Este cea mai valoroasă secțiune din tot documentul.

Iată codul complet pentru README.md. Am reparat link-ul către diagrama CI/CD cu o imagine publică standard și am tradus totul într-o engleză tehnică profesională.

README.md (Copy & Paste)
Markdown

# Cloud-Native Portfolio Architecture

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
[![CI/CD Pipeline](https://github.com/[YOUR_GITHUB_USERNAME]/[YOUR_REPO_NAME]/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/[YOUR_GITHUB_USERNAME]/[YOUR_REPO_NAME]/actions)

> **Live Demo:** [https://[YOUR-APP-NAME].azurewebsites.net](https://[YOUR-APP-NAME].azurewebsites.net)

## 📖 About the Project

This repository hosts more than just a portfolio website. It serves as a comprehensive **DevOps Lab**, built to demonstrate the implementation of a modern, end-to-end Software Development Life Cycle (SDLC) using **Infrastructure as Code (IaC)**, **Containerization**, and **CI/CD** practices on Microsoft Azure.

The project started as a monolithic Flask application and evolved into a cloud-native, scalable, and secure architecture, solving real-world production challenges along the way (system drivers, network security, state management).

---

## 🏗️ Architecture & Tech Stack

The system is deployed on **Microsoft Azure**, leveraging PaaS services for scalability and reduced maintenance overhead.

![DevOps Lifecycle](https://upload.wikimedia.org/wikipedia/commons/0/05/Devops-toolchain.svg)

### Tech Stack
| Category | Technologies Used |
| :--- | :--- |
| **Backend** | Python 3.10, Flask, SQLAlchemy, Gunicorn |
| **Database** | **Azure SQL Database** (Serverless Tier - Auto-pause enabled for cost optimization) |
| **Infrastructure** | **Azure Web App for Containers**, Azure Container Registry (ACR) |
| **IaC** | **Terraform** (State Management & Provisioning) |
| **CI/CD** | **GitHub Actions** (Build, Test, Security Scan, Deploy) |
| **Quality & Security** | **Ruff** (Linting), **Black** (Formatting), **Trivy** (Container Security), **Pre-commit hooks** |

---

## 🚀 DevOps & CI/CD Pipeline

The pipeline is defined in `.github/workflows/ci-cd.yml`, automating code delivery from commit to production.

### Pipeline Stages:
1.  **Continuous Integration (CI):**
    * **Linting:** Enforcing code quality standards using `Ruff`.
    * **Testing:** Running unit and integration tests (Smoke Tests) using `pytest`.
    * **Security Scan:** Vulnerability scanning for code dependencies.
2.  **Continuous Delivery (CD):**
    * **Docker Build:** Building the container image (based on `python:3.11-slim`, optimized with ODBC drivers).
    * **Push:** Uploading the image to **Azure Container Registry (ACR)**.
    * **Deploy:** Updating the **Azure Web App** instance with the latest image.

---

## 🛠️ Infrastructure as Code (Terraform)

The infrastructure is not created manually ("ClickOps"), but defined as code in the `/infra` directory. This ensures:
* **Reproducibility:** The environment can be destroyed and recreated identically in minutes.
* **Versioning:** Infrastructure changes are tracked in Git.
* **State Management:** Managing resources like Resource Groups, App Service Plans, SQL Servers, and Firewall Rules via Terraform State.

```hcl
# Example snippet from main.tf
resource "azurerm_linux_web_app" "webapp" {
  name                = "app-portfolio"
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id
  
  site_config {
    always_on = false # Cost optimization for Dev plan
    application_stack {
      docker_image     = "${azurerm_container_registry.acr.login_server}/portfolio"
      docker_image_tag = "latest"
    }
  }
}
🔧 Engineering Challenges & Solutions
During development, I encountered and resolved several complex integration issues common in production environments:

1. Database Drivers in Linux Containers
The Issue: The Docker container (Linux Alpine/Slim) failed to communicate with Azure SQL, throwing libodbc.so.2: file not found errors.

The Solution: I re-engineered the Dockerfile to explicitly install Microsoft ODBC 18 system drivers (msodbcsql18) and unixodbc-dev dependencies before installing Python packages.

2. Network Security (Firewall)
The Issue: The application timed out (Login timeout expired) when attempting to connect to the database.

The Diagnosis: The Web App and Database were running in different regions/contexts, and the SQL Firewall was blocking the traffic.

The Solution: Diagnosed the outbound traffic flow and whitelisted the Web App's Outbound IPs in the SQL Server Firewall rules (now managed via Terraform).

3. Database Schema Management (Schema Drift)
The Issue: Deployment failures (Invalid object name 'user') on the first run because database tables did not exist.

The Solution: Implemented a custom initialization script (init_db.py) triggered conditionally via the Startup Command to ensure schema consistency without requiring manual SSH intervention.

💻 Local Development Setup
To run this project locally:

Clone the repository:

Bash

git clone [https://github.com/](https://github.com/)[YOUR_GITHUB_USERNAME]/[YOUR_REPO_NAME].git
cd [YOUR_REPO_NAME]
Configure environment:

Bash

# Install dependencies (using uv for speed)
pip install uv
uv pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install
Set environment variables (.env):

Bash

SECRET_KEY="local-dev-key"
DATABASE_URL="sqlite:///site.db" # Use local SQLite for dev
Run the application:

Bash

flask run