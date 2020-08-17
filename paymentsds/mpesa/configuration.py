from Crypto.PublicKey import RSA
from .environment import Environment
from Crypto.Cipher import PKCS1_v1_5

import base64

class Configuration:
  PARAMS = [
    'user_agent',
    'api_key',
    'public_key',
    'timeout',
    'verify_ssl',
    'debugging',
    'access_token',
    'environment',
    'host',
    'service_provider_code',
    'initiator_identifier',
    'security_credential',
    'origin'
  ]

  def __init__(self, **kwargs):
    self.user_agent = 'Paymentsds/M-Pesa'
    self.timeout = 0
    self.verify_ssl = False
    self.debugging = True
    self.environment = Environment.from_url(Environment.SANDBOX),
    self.origin = '*'

    for key, value in kwargs.items():
      if key in self.PARAMS:
        if key == 'host':
          self.environment = Environment.from_url(value)
        elif key == 'environment':
          self.environment = Environment.from_url(value)
        else:
          self.__dict__[key] = value
  
  def generate_access_token(self):
    has_keys = hasattr(self, 'api_key') and hasattr(self, 'public_key')
    has_access_token = hasattr(self, 'access_token')

    if has_keys:
      formated_rsa_public_key = self.format_public_key(self.public_key)
      rsa_public_key_buffer = formated_rsa_public_key.encode()

      rsa_public_key = RSA.importKey(rsa_public_key_buffer)
      cipher = PKCS1_v1_5.new(rsa_public_key)
      encrypted_api_key = cipher.encrypt(self.api_key.encode())
      self.auth = base64.b64encode(encrypted_api_key).decode()

    if has_access_token:
      self.auth = self.access_token

  def format_public_key(self, public_key):
    header = '-----BEGIN PUBLIC KEY-----'
    footer = '-----END PUBLIC KEY-----'
    
    return '{}\n{}\n{}'.format(header, public_key, footer)
