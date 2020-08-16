class Response:
    def __init__(self, status, data):
        self.success = status
        self.status = {
            'code': data['output_ResponseCode'],
            'description': data['output_ResponseDesc']
        }
        self.data = {
            'transaction': data['output_TransactionID'],
            'conversation': data['output_ConversationID'],
            'reference': data['output_ThirdPartyReference'],
        }
    