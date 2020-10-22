# Azure Key Vault (akv)

This is a simple package for accessing secrets in Azure Key Vault.

## Setup

The environment variables `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` and `KEY_VAULT_NAME` all need to be set in your environment.

- The Tenant ID aka the Directory ID of your Azure tenant.
- The Client ID aka the Application ID of the app identity. Go to App Registrations in the Azure Portal to create an app.
- The Client Secret aka the secret used to request a authorization token for the app. Client Secrets can be defined under `App Registrations` > `App Name` > `Certificates & secrets`.
- The Key Vault name is the literal name of the Azure Key Vault resource defined.

Note that the client needs permissions to access the secrets in the vault. In the Azure Portal, navigate to `Key Vaults` > `Key Vault Name` > `Access policies` and click on `Add Access Policy`.

## Use

Set the four required environment variables:

```
export AZURE_TENANT_ID='somethin-glik-ethi-ssss-ssssssssssss'
export AZURE_CLIENT_ID='134kmg50-af2g-2qq2-g3ag-q2f[p30jgsl2'
export KEY_VAULT_NAME='Key-Vault-Name-From-Azure-Portal'
export AZURE_CLIENT_SECRET='2_2rfammunoia3befg_402?w].e'
```

Use in code:

``` python
>>> from akv import Secrets
>>> my_secrets = Secrets()
>>> my_secrets.set('TestSecret', 'Hunter2')
>>> my_secrets.get('TestSecret')
'*******'
>>> my_secrets.delete('TestSecret')
```

## Contribute

Go ahead:

``` bash
$ git clone https://github.com/casperlehmann/akv.git
$ cd akv
$ pip install -r requirements.txt
```
