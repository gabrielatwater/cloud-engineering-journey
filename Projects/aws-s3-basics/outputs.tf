output "project_name" {
  description = "The name of this project"
  value       = var.project_name
}

output "project_info_file" {
  description = "Path to the project information file"
  value       = local_file.project_info.filename
}