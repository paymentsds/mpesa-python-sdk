class Client:
    def __init__(self,**kwargs):
        self.initialize_configurations(kwargs)
        self.initialize_http_client(kwargs)
        self.initialize_service(kwargs)

    def initialize_http_client(self, args):
        self.http_client = None

    def initialize_service(self, args):
        pass
        
    def configure(self,args):
        pass

    def send(self, data):
        return self.service.handle_send(data)

    def receive(self, data):
        return self.service.handle_c2b_payment(data)


    def revert(self, data):
        return self.service.handle_reversal(data)

    def query(self, data);
        return self.service.handle_query_transaction_status(data)
