import re

PATTERNS = {
  'PHONE_NUMBER': re.compile('^((00|\+)?258)?8[45][0-9]{7}$'),
  'SERVICE_PROVIDER_CODE': re.compile('^[0-9]{5,6}$'),
  'WORD': re.compile('\\w+'),
  'MONEY_AMOUNT': re.compile( '^[1-9][0-9]*(\.[0-9])*$')
}

DEFAULT_OPERATIONS = {
  'C2B_PAYMENT': {
      'method': 'POST',
      'port':'18352',
      'path':'/ipg/v1x/c2bPayment/singleStage/',
      'mapping': {
        'from': 'input_CustomerMSISDN',
        'to': 'input_ServiceProviderCode',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': PATTERNS['PHONE_NUMBER'],
        'to': PATTERNS['SERVICE_PROVIDER_CODE'],
        'amount': PATTERNS['MONEY_AMOUNT'],
        'transaction': PATTERNS['WORD'],
        'reference': PATTERNS['WORD']
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
        'to'
      ]
  },
  'B2B_PAYMENT': {
      'method': 'POST',
      'port':'18349',
      'path':'/ipg/v1x/b2bPayment/',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'to': 'input_ReceiverPartyCode',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': PATTERNS['SERVICE_PROVIDER_CODE'],
        'to': PATTERNS['SERVICE_PROVIDER_CODE'],
        'amount': PATTERNS['MONEY_AMOUNT'],
        'transaction': PATTERNS['WORD'],
        'reference': PATTERNS['WORD']
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
       'from'
      ]
  },
  'B2C_PAYMENT': {
      'method': 'POST',
      'port':'18345',
      'path':'/ipg/v1x/b2cPayment/',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'to': 'input_CustomerMSISDN',
        'amount': 'input_Amount',
        'transaction': 'input_TransactionReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
        'from': PATTERNS['SERVICE_PROVIDER_CODE'],
        'to': PATTERNS['PHONE_NUMBER'],
        'amount': PATTERNS['MONEY_AMOUNT'],
        'transaction': PATTERNS['WORD'],
        'reference': PATTERNS['WORD']
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference'
      ],
      'optional': [
        'from'
      ]
  },
  'REVERSAL': {
      'method': 'PUT',
      'port':'18354',
      'path':'/ipg/v1x/reversal/',
      'mapping': {
        'to': 'input_ServiceProviderCode',
        'amount': 'input_ReversalAmount',
        'transaction': 'input_TransactionID',
        'reference': 'input_ThirdPartyReference',
        'security_credential': 'input_SecurityCredential',
        'initiator_identifier': 'input_InitiatorIdentifier'
      },
      'validation': {
        'to': PATTERNS['SERVICE_PROVIDER_CODE'],
        'amount': PATTERNS['MONEY_AMOUNT'],
        'transaction': PATTERNS['WORD'],
        'reference': PATTERNS['WORD'],
        'security_credential': PATTERNS['WORD'],
        'initiator_identifier': PATTERNS['WORD']
      },
      'required': [
        'to',
        'amount',
        'transaction',
        'reference',
        'security_credential',
        'initiator_identifier'
      ],
      'optional': [
        'to',
        'security_credential',
        'initiator_identifier'
      ]
  },
  'QUERY_TRANSACTION_STATUS': {
      'method': 'GET',
      'port':'18353',
      'path':'/ipg/v1x/queryTransactionStatus/',
      'mapping': {
        'from': 'input_ServiceProviderCode',
        'subject': 'input_QueryReference',
        'reference': 'input_ThirdPartyReference'
      },
      'validation': {
       'from': PATTERNS['SERVICE_PROVIDER_CODE'],
        'subject': PATTERNS['WORD'],
        'reference': PATTERNS['WORD']
      },
      'required': [
        'from',
        'subject',
        'reference'
      ],
      'optional': [
        'from' 
      ]
  }
}
