# Cloud-Native Portfolio Architecture

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
[![CI/CD Pipeline](https://github.com/[USER_TAU]/[NUME_REPO]/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/[USER_TAU]/[NUME_REPO]/actions)

> **Live Demo:** [https://[NUME-APP].azurewebsites.net](https://[NUME-APP].azurewebsites.net)

## 📖 Despre Proiect

Acesta nu este doar un simplu website de portofoliu. Este un **laborator de DevOps** construit pentru a demonstra implementarea unui ciclu complet de dezvoltare software (SDLC) modern, folosind practici de **Infrastructure as Code (IaC)**, **Containerizare** și **CI/CD** pe platforma Microsoft Azure.

Proiectul a început ca o aplicație monolitică Flask și a evoluat într-o arhitectură cloud-native, scalabilă și sigură, rezolvând provocări reale de producție (networking, drivere de sistem, securitate).

---

## 🏗️ Arhitectura & Tech Stack

Sistemul este găzduit în **Microsoft Azure**, utilizând servicii PaaS pentru scalabilitate și mentenanță redusă.



[Image of DevOps CI/CD pipeline diagram]


### Stack Tehnologic
| Categorie | Tehnologii Folosite |
| :--- | :--- |
| **Backend** | Python 3.10, Flask, SQLAlchemy, Gunicorn |
| **Database** | **Azure SQL Database** (Serverless Tier - Auto-pause enabled pentru optimizare costuri) |
| **Infrastructure** | **Azure Web App for Containers**, Azure Container Registry (ACR) |
| **IaC** | **Terraform** (Gestionarea stării infrastructurii) |
| **CI/CD** | **GitHub Actions** (Build, Test, Security Scan, Deploy) |
| **Quality & Security** | **Ruff** (Linting), **Black** (Formatting), **Trivy** (Container Security), **Pre-commit hooks** |

---

## 🚀 DevOps & CI/CD Pipeline

Pipeline-ul este definit în `.github/workflows/ci-cd.yml` și automatizează livrarea codului de la commit până în producție.

### Etapele Pipeline-ului:
1.  **Continuous Integration (CI):**
    * **Linting:** Verificarea calității codului cu `Ruff`.
    * **Testing:** Rularea testelor unitare și de integrare (Smoke Tests) folosind `pytest`.
    * **Security Scan:** Scanarea vulnerabilităților în cod și dependențe.
2.  **Continuous Delivery (CD):**
    * **Docker Build:** Crearea imaginii containerului (bazată pe `python:3.11-slim`, optimizată cu drivere ODBC).
    * **Push:** Urcarea imaginii în **Azure Container Registry (ACR)**.
    * **Deploy:** Actualizarea instanței **Azure Web App** cu noua imagine.

---

## 🛠️ Infrastructure as Code (Terraform)

Infrastructura nu este creată manual ("ClickOps"), ci este definită prin cod în directorul `/infra`. Acest lucru asigură:
* **Reproductibilitate:** Mediul poate fi distrus și recreat identic în câteva minute.
* **Versioning:** Istoricul modificărilor de infrastructură este păstrat în Git.
* **State Management:** Urmărirea stării resurselor (Resource Groups, App Service Plans, SQL Servers, Firewall Rules).

```hcl
# Exemplu din main.tf
resource "azurerm_linux_web_app" "webapp" {
  name                = "app-portofoliu"
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id
  
  site_config {
    always_on = false # Optimizare costuri pentru planul Dev
    application_stack {
      docker_image     = "${azurerm_container_registry.acr.login_server}/portofoliu"
      docker_image_tag = "latest"
    }
  }
}