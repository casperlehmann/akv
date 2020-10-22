import os
import logging
from azure.keyvault.secrets import SecretClient
from azure.identity import EnvironmentCredential
from azure.core import exceptions

class Secrets():
    def __init__(self):
        for env_var in ('AZURE_TENANT_ID', 'AZURE_CLIENT_ID',
                        'KEY_VAULT_NAME', 'AZURE_CLIENT_SECRET'):
            if not os.environ.get(env_var):
                logging.error((
                    'The environment variables "AZURE_TENANT_ID", '
                    '"AZURE_CLIENT_ID", "KEY_VAULT_NAME" and '
                    '"AZURE_CLIENT_SECRET" all need to be set '
                    'in your environment.'
                ))
                raise ValueError((f'Environment variable {env_var} '
                                   'not set. Cannot authenticate with Azure.'))
        self.key_vault_name = os.environ.get('KEY_VAULT_NAME')
        KVUri = f'https://{self.key_vault_name}.vault.azure.net'
        credential = EnvironmentCredential()
        self.client = SecretClient(vault_url=KVUri, credential=credential)

    def get(self, secret_name):
        logging.info(f'Getting secret "{secret_name}" from "{self.key_vault_name}"')
        try:
            retrieved_secret = self.client.get_secret(secret_name)
            return retrieved_secret.value
        except exceptions.ResourceNotFoundError:
            raise KeyError(f'Secret "{secret_name}" does not exist in "{self.key_vault_name}"')

    def set(self, secret_name, secret_value):
        logging.info(f'Creating secret "{secret_name}" in {self.key_vault_name}. Value: "{secret_value}"')
        self.client.set_secret(secret_name, secret_value)

    def delete(self, secret_name):
        logging.info(f'Deleting secret "{secret_name}" from "{self.key_vault_name}"')
        try:
            self.client.begin_delete_secret(secret_name)
            logging.info(f'Deleted')
        except exceptions.ResourceNotFoundError:
            logging.info(f'Secret "{secret_name}" does not exist in "{self.key_vault_name}"')
