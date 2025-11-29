# provider.tf
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  # Aici vom configura backend-ul mai târziu (pentru tfstate în cloud)
}

provider "azurerm" {
  features {}
}