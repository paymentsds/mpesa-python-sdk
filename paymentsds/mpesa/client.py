from .service import Service

class Client:
  def __init__(self,**kwargs):
    self.service = Service(**kwargs)

  def send(self, data):
    return self.service.handle_send(data)

  def receive(self, data):
    return self.service.handle_receive(data)


  def revert(self, data):
    return self.service.handle_revert(data)

  def query(self, data):
    return self.service.handle_query(data)
