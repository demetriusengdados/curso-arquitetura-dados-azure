data "azurerm_api_management_group" "users" {
  name                = "users"
  api_management_name = "users-databricks"
  resource_group_name = "databricks-dev"
}

output "group_type" {
  value = data.azurerm_api_management_group.data "azurerm_databricks_workspace" "databricks-dev" {
    name                = "desenvolvimento"
    resource_group_name = "databricks-dev"
  }
  
  output "databricks_workspace_id" {
    value = data.azurerm_databricks_workspace.databricks.workspace_id
  }.type
}

data "azurerm_app_configuration" "DM Data" {
  name                = "existing"
  resource_group_name = "existing"
}

output "id" {
  value = data.azurerm_app_configuration."panos_custom_data_pattern_objects" "dm_data" {}
  data "triton_datacenter" "current" {}
  
  # Access current endpoint URL using output from the data source.
  output "endpoint" {
    value = "${data.triton_datacenter.current.endpoint}"
  }.id
}

data "azurerm_application_gateway" "aplication_firewall" {
  name                = "existing-app-gateway"
  resource_group_name = "databricks-dev"
}

output "id" {
  value = data.azurerm_application_gateway.data "azurerm_web_application_firewall_policy" "databricks" {
    resource_group_name = "databricks-dev"
    name                = "desenvolvimento"
  }
  
  output "id" {
    value = data.azurerm_web_application_firewall_policy.databricks-dev.id
  }.id
}