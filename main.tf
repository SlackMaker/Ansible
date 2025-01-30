terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Criar uma rede Docker personalizada
resource "docker_network" "gitlab_network" {
  name = "gitlab-network"
}

# Criar um contêiner Prometheus
resource "docker_container" "prometheus" {
  name  = "prometheus"
  image = "prom/prometheus:latest"
  ports {
    internal = 9090
    external = 9090
  }
  volumes {
    host_path      = "/etc/prometheus/prometheus.yml"
    container_path = "/etc/prometheus/prometheus.yml"
  }
  networks_advanced {
    name = docker_network.gitlab_network.name
  }
  restart = "unless-stopped"
}

# Criar um contêiner Grafana
resource "docker_container" "grafana" {
  name  = "grafana"
  image = "grafana/grafana:latest"
  ports {
    internal = 3000
    external = 3000
  }
  env = [
    "GF_SECURITY_ADMIN_PASSWORD=admin",
    "GF_SERVER_ROOT_URL=http://localhost:3000"
  ]
  networks_advanced {
    name = docker_network.gitlab_network.name
  }
  restart = "unless-stopped"
}

# Criar um contêiner GitLab com credenciais automatizadas
resource "docker_container" "gitlab" {
  name  = "gitlab"
  image = "gitlab/gitlab-ce:latest"
  ports {
    internal = 80
    external = 80
  }
  networks_advanced {
    name = docker_network.gitlab_network.name
  }
  env = [
    "GITLAB_OMNIBUS_CONFIG=external_url 'http://192.168.1.6'",
    "GITLAB_ROOT_PASSWORD=5iveL!fe"  # Senha padrão do root do GitLab
  ]
  restart = "unless-stopped"
}

# Expondo os IPs e as URLs
output "prometheus_url" {
  value = "http://${docker_container.prometheus.network_data[0].ip_address}:9090"
}

output "grafana_url" {
  value = "http://${docker_container.grafana.network_data[0].ip_address}:3000"
}

output "gitlab_url" {
  value = "http://192.168.1.6"
}