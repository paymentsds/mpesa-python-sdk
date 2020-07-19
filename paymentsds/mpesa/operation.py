class Operation:
  PARAMS = [
    'name',
    'method',
    'port',
    'path',
    'expects',
    'returns'
  ]

  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      if key in self.PARAMS:
        self.__dict__[key] = value