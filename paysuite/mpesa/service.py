class Service:
    DEFAULT_OPERATIONS = {
        'B2C_PAYMENT': Operation(
            name='b2cPayment',
            method='POST',
            port='18345',
            path='/ipg/v1x/b2cPayment',
            expects={
                'mapping': {
                    'from': 'input_ServiceProviderCode',
                    'to': 'input_CustomerMSISDN',
                    'amount': 'input_Amount',
                    'transaction': 'input_TransactionReference',
                    'reference': 'input_ThirdPartyReference'
                },
                'validation': {
                    'from': '^[0-9]{5,6}$',
                    'to': '^((00|\+)?258)?8[45][0-9]{7}$',
                    'amount': '^[1-9][0-9]*(\.[0-9])*$',
                    'transaction': '\\w+',
                    'reference': '\\w+'                
                },
                'required': [
                    'to', 
                    'amount', 
                    'transaction', 
                    'reference'
                ],
                'optional': [
                    'from'
                ],
                'body': 'body'
            },
            returns={
                'mapping': {
                    'output_': 'output_'
                }
            }
        ),

        'B2C_PAYMENT': '',
        'B2B_PAYMENT': '',
        'REVERSAL': '',
        'QUERY_TRANSACTION_STATUS': ''
    }

    def __init__(self, **args):
        pass

    def handle_request(self, operation, data):
        complete_data = self.complete_request_data(operation, data)
        
        missing_properties = self.detecting_missing_properties(operation, complete_data)
        if len(missing_properties):
            # return errors
        
        errors = self.detect_errors(operation, complete_data)
        if len(errors):
            # return errors
        
        # continue
        def build_request:
            pass
        
        def make_request:
            pass

    def handle_send(self, data):
        operation = self.detect_operation(data)
        if operation
            self.handle_request(operation, data)
        return 'error'

    def handle_c2b_payment(self, data):
        self.handle_request(self.DEFAULT_OPERATIONS['C2B_PAYMENT'], data)

    def handle_b2c_payment(self, data):
        self.handle_request(self.DEFAULT_OPERATIONS['B2C_PAYMENT'] data)

    def handle_b2b_payment(self, data):
        self.handle_request(self.DEFAULT_OPERATIONS['B2B_PAYMENT'], data)

    def handle_query_transaction_status(self, data):
        self.handle_request(self.DEFAULT_OPERATIONS['QUERY_TRANSACTION_STATUS'], data)

    def handle_reversal(self, data):
        self.handle_request(self.DEFAULT_OPERATIONS['REVERSAL'], data)

    def detect_operation(self, data):
        phone_number = re.compile('^((00|\+)?258)?8[45][0-9]{7}$')
        service_provider_code = re.compile('^[0-9]{5,6}$')
            
        if phone_number.match(data['to'])
            return self.DEFAULT_OPERATIONS['B2C_PAYMENT']

        if service_provider_code.match(data['to'])
            return self.DEFAULT_OPERATIONS['B2B_PAYMENT']
            
        return None        
    
    def detect_errors(self, operation, data):
        errors = []
          
        for k, v in data.items():
            regex = re.compile(operation.expects['mapping']['validation'][k])
            if not regex.match(v):
                errors.append(k)    
        
        return errors
    
    def detect_missing_properties(self, operation, data):
        required_properties = set(operation.expects['mapping']['required']) + set(operation.expects['mapping']['optional'])
        given_properties = set(data.items())
        missing_properties = required - given_properties
        
        return list(missing)  
        
    def complete_request_data(self, operation, data)
        def complete_to(to_complete):
            if 'to' not in to_complete.keys():
                if 'service_provider_code' in self.config.__dict__.keys()
                    to_complete['to'] = self.config.service_provider_code
            
            return to_complete
            
        def complete_from(to_complete):          
            if 'from' not in to_complete.keys():
                if 'service_provider_code' in self.config.__dict__.keys()
                    to_complete['from'] = self.config.service_provider_code
            
            return to_complete
            
        def complete_reversal_data(to_complete):
            if 'initiator_identifier' not in to_complete.keys():
                if 'service_provider_code' in self.config.__dict__.keys()
                    to_complete['to'] = self.config.service_provider_code
            
            if 'initiator_identifier' not in to_complete.keys():
                if 'initiator_identifier' in self.config.__dict__.keys()
                    to_complete['initiator_identifier'] = self.config.initiator_identifier
            
            if 'security_credetial' not in to_complete.keys():
                if 'security_credetial' in self.config.__dict__.keys()
                to_complete['security_credetial'] = self.config.security_credetial
            
            return to_complete

        if operation is self.DEFAULT_OPERATION['C2B_PAYMENT']:
            return complete_to(data)
        elif operation in self.DEFAULT_OPERATION['B2B_PAYMENT']:
            return complete_from(data)
        elif operation is self.DEFAULT_OPERATION['B2C_PAYMENT']:
            return complete_from(data)
        elif operation is self.DEFAULT_OPERATION['REVERSAL']:
            return = complete_reversal_data(data)
       elif operation is self.DEFAULT_OPERATION['QUERY_TRANSACTION_STATUS']:
            return complete_to(data)
        else:
            return data
            
