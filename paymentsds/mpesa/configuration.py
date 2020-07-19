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
    'host'
  ]

  def __init__(self, **kwargs):
    self.user_agent = 'Paysuite/MPesa'
    self.timeout = 0
    self.verify_ssl = False
    self.debugging = True
    self.environment = Environment.from_url(Environment.SANDBOX)

    for key, value in kwargs.items():
      if key in self.PARAMS:
        if key == 'host':
          self.environment = Environment.from_url(value)
        else:
          self.__dict__[key] = value

  def build_default_operations(self)
    pass

  def build_default_headers(self):
    pass

  def generate_headers(self):
    pass

  def generate_authorization_header(self):
    pass

  def generate_url(self, operation):
    pass

  def is_valid(self):
    pass

  def generate_base_url(self, operation):
    pass
