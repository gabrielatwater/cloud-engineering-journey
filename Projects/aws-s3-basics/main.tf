terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

resource "local_file" "project_info" {
  filename = "${path.module}/project-info.txt"
  content  = "Project name: ${var.project_name}"
}