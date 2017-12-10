
vault {
  address = "http://localhost:8200"
  grace = "2m"
  token = "56ef8d68-cd8f-e5e0-bfa5-b8b29a6bf722"
  renew_token = true
}
template {
  source = "env.ctmpl"
  destination = "env"
  create_dest_dirs = true
  command_timeout = "10s"
  error_on_missing_key = false
  perms = 0600
  left_delimiter  = "{{"
  right_delimiter = "}}"
  wait {
    min = "2s"
    max = "10s"
  }
}