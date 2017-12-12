
vault {
  address = "http://localhost:8200"
  grace = "1m"
  token = "c34db5da-5d4e-2525-115e-cad1b99382a7"
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
