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
    self.user_agent = 'Paymentsds/M-Pesa'
    self.timeout = 0
    self.verify_ssl = False
    self.debugging = True
    self.environment = Environment.from_url(Environment.SANDBOX)

    for key, value in kwargs.items():
      if key in self.PARAMS:
        if key == 'host':
          self.environment = Environment.from_url(value)
        elif key == 'environment':
          self.environment = Environment.from_url(value)
        else:
          self.__dict__[key] = value