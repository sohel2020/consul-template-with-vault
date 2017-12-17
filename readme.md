# Vault with consul-template Demo
---


# Prerequisite

- [x] vault >=  v0.8.3
- [x] postgresql >= 9.3
- [x] consul-template >= v0.19.4
- [x] jq

![vaultandconsul](images/vaultconsul.jpeg)
### Run vault as a dev mode

```shell
$ vault server -dev
$ export VAULT_ADDR='http://127.0.0.1:8200'
```
Get the root token and then:
```shell
$ vault auth [root_token]
```

## Create a new root token 
It's good Practice not to use root token

```shell
$ vault token-create -policy="root" -display-name="tarikur"

# Login using new token
$ vault auth [new_token]
```

# Enable Auditing

```shell
$ vault audit-enable file file_path=vault_audit.log log_raw=true hmac_accessor=false
$ tail -F vault_audit.log | while read line; do echo "$line" | jq; done 
```

# Dynamic Backend (postgresql)

```shell
$ vault mount database

$ docker rm -f postgres ; docker run -d -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=12345678 postgres

$ vault write database/config/myapplication-prod \
    plugin_name=postgresql-database-plugin \
    allowed_roles="admin" \
    connection_url="postgresql://postgres:12345678@localhost:5432/postgres?sslmode=disable"


$ vault write database/roles/admin \
    db_name=myapplication-prod \
    creation_statements="CREATE ROLE \"{{name}}\"
    WITH SUPERUSER LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';" \
    revocation_sql="SELECT revoke_access('{{name}}'); DROP user \"{{name}}\";"  \
    default_ttl="360" \
    max_ttl="600"

# skip for the sake for some test
$ vault read database/creds/admin


### write policy and create token

$ vault policy-write vault-demo postgresql/postgres-policy.hcl

$ vault token-create -policy="vault-demo" -period='10m' -renewable=true -display-name="myapplication"
```

## Consul-template

```shell
$ cd application
$ vim config.hcl # change your token and creds path
$ consul-template -config=config.hcl
```



## Missing piece:
Consul template is not getting new data from vault before lease time. Let's say you have write new data after run `consul-template` new changes will take effect either restart `consul-template` or `lease time expire` 


### Useful Document:
* https://www.vaultproject.io/docs/index.html
* https://github.com/hashicorp/vault
* https://github.com/hashicorp/consul-template
