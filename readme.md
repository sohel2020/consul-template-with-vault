# Vault with consul-template Demo

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

### write policy and create token
```shell
$ vault policy-write secret policy.hcl
$ vault token-create -policy="secret" -period='7m' -renewable=true
```
login using new `token`

```shell
$ vault auth 9666ff3e-56e5-53f0-a295-33aafb911a80
$ vault write secret/tonic-report/prod/cred username=tarikur password=abc123
```

See the status of the token
```shell
$ vault token-lookup 9666ff3e-56e5-53f0-a295-33aafb911a80
```

Token Revoke:

```shell
$ vault token-revoke 9666ff3e-56e5-53f0-a295-33aafb911a80
```

### Missing piece:
Consul template is not getting new data from vault before lease time. Let's say you have write new data after run `consul-template` new changes will take effect either restart `consul-template` or `lease time expire` 

### Useful Document:
* https://www.vaultproject.io/docs/index.html
* https://github.com/hashicorp/vault
* https://github.com/hashicorp/consul-template
