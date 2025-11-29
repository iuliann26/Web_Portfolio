# infra/variables.tf

# --- general settings ---
variable "resource_group_name" {
  description = "Numele grupului de resurse"
  type        = string
}

variable "location" {
  description = "main locatio (pentru App Service, ACR)"
  type        = string
  default     = "Spain Central"
}

variable "sql_location" {
  description = "Locația pentru baza de date (diferită din cauza restricțiilor de student)"
  type        = string
  default     = "France Central"
}

# --- Naming (Numele Resurselor) ---
variable "acr_name" {
  description = "Numele unic al Container Registry"
  type        = string
}

variable "app_service_plan_name" {
  description = "Numele App Service Plan"
  type        = string
}

variable "web_app_name" {
  description = "Numele Web App (trebuie să fie unic global)"
  type        = string
}

variable "sql_server_name" {
  description = "Numele Serverului SQL (unic global)"
  type        = string
}

variable "sql_db_name" {
  description = "Numele Bazei de Date"
  type        = string
}

# --- Secrete (Sensibile) ---
variable "sql_admin_user" {
  description = "Utilizatorul de admin SQL"
  type        = string
  default     = "iulianadmin"
}

variable "sql_admin_password" {
  description = "Parola de admin SQL"
  type        = string
  sensitive   = true
}