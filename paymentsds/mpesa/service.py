#import .constants
from .configuration import Configuration

class Service:
  def __init__(self, **kwargs):
    self.config = Configuration(**kwargs)

  def handle_request(self, opcode, intent):
    data = self.fill_optional_properties(opcode, intent)

    missing_properties = self.detecting_missing_properties(opcode, data)
    if len(missing_properties):
        # return errors

    errors = self.detect_errors(opcode, data)
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

  def handle_receive(self, data):
    self.handle_request(constants.DEFAULT_OPERATIONS['C2B_PAYMENT'], data)

  def handle_query(self, data):
    self.handle_request(constants.DEFAULT_OPERATIONS['QUERY_TRANSACTION_STATUS'], data)

  def handle_revert(self, data):
    self.handle_request(constants.DEFAULT_OPERATIONS['REVERSAL'], data)

  def detect_operation(self, data):
    if constants.PATTERNS['PHONE_NUMBER'].match(data['to'])
      return constants.DEFAULT_OPERATIONS['B2C_PAYMENT']

    if constants.PATTERNS['SERVICE_PROVIDER_CODE'].match(data['to'])
      return constants.DEFAULT_OPERATIONS['B2B_PAYMENT']

    return None

  def detect_errors(self, operation, data):
    errors = []

    for k, v in data.items():
      regex = operation['validation'][k]
      if not regex.match(v):
        errors.append(k)

    return errors

  def detect_missing_properties(self, operation, data):
    required_properties = set(operation['required'])
    given_properties = set(data.items())
    missing_properties = required - given_properties

    return list(missing_properties)

  def fill_optional_properties(self, operation, data)
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

  def perform_request(opcode, intent):
    self.generate_access_token()

    if hasattr(self.config, 'environment'):
      if hasattr(self.config, 'auth'):
        operation = self.DEFAULT_OPERATION[opcode]
        headers = self.build_request_headers()
        body = build_request_body(opcode, intent)

        request_data = {
          'base_url': '{}://{}',
          'path': operation['path'],
          'method': operation['method'],
          'headers': headers,
        }

        if operation['method'] == 'post'
          request_data['data'] = body
        else
          request_data['params'] = body

        return request_data
      else:
        return {
          'error': [
          'No auth'
          ]
        }
    else:
      return {
        'error': [
        'No environment'
        ]
      }

  def generate_access_token():
    self.config.generate_access_token()

  def build_request_headers():
    return {
      'User-Agent': self.config.user_agent,
      'Origin': self.config.origin,
      'Authorization': 'Bearer {}'.format(self.config.auth)
    }

  def build_request_body(opcode, intent):
    pass