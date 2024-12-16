variable "subscription_id" {
  type        = string
  description = "ID da assinatura da Azure"
}

variable "tenant_id" {
  type        = string
  description = "ID do tenant da Azure"
}

variable "resource_group_name" {
  type        = string
  description = "Nome do grupo de recursos onde os recursos serão criados"
  default     = "MeuGrupoDeRecursos"
}

variable "location" {
  type        = string
  description = "Região da Azure"
  default     = "East US"
}
