# Este é um exemplo. O conteúdo real dependerá da versão e dos hashes dos provedores baixados.
provider "registry.terraform.io/hashicorp/azurerm" {
  version     = "3.73.0"
  constraints = "~> 3.0"
  hashes = [
    "h1:XNkZg2Q...",
    "zh:7e5d2...",
    # mais hashes de verificação para garantir integridade
  ]
}
