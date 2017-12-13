
vault {
  address = "http://localhost:8200"
  grace = "1m"
  token = "4a670457-daa6-c7fc-bb6e-c690ede49a30"
  renew_token = true
}

exec {
  command = "python3 app.py"
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
