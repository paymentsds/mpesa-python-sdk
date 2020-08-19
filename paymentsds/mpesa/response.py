from collections import namedtuple

class Response:
    def __init__(self, status, data):
        self.success = status
        self.status = namedtuple('ResponseStatus', 'code description')(
            data['output_ResponseCode'],
            data['output_ResponseDesc']
        )

        self.data = {#namedtuple('ResponseData' , 'transaction conversation reference')(
            # 'transaction': data['output_TransactionID'],
            'conversation': data['output_ConversationID'],
            'reference': data['output_ThirdPartyReference']
        }#)
        if hasattr(data, 'output_TransactionID'): self.data['transaction'] = data['output_TransactionID']
