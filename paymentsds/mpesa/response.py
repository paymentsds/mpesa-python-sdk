from collections import namedtuple

class Response:
    def __init__(self, status, data):
        self.success = status
        self.status = namedtuple('ResponseStatus', 'code description')(
            data['output_ResponseCode'],
            data['output_ResponseDesc']
        )

        self.data = namedtuple('ResponseData' , 'transaction conversation reference')(
            data['output_TransactionID'],
            data['output_ConversationID'],
            data['output_ThirdPartyReference']
        )
