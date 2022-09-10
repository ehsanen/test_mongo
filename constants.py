import os

SERVER_PORT = int(os.getenv('SERVER_PORT', 9292))
TOKEN_TYPE = 'Bearer'

# TODO: Should move to a secret manager of the CI/CD pipeline
TOKEN = 'B1n0FlddHVnfBLeAkC'
