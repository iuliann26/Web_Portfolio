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



